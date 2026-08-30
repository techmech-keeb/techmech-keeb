#!/usr/bin/env python3
"""Regenerate the external-contributions block in README.md.

Searches GitHub for pull requests authored by this account that were merged
in repositories outside the account, and rewrites the README section between
the EXTERNAL-CONTRIBUTIONS markers. Uses only the Python standard library.

Environment:
  GITHUB_TOKEN              token for the GitHub search API (recommended;
                            unauthenticated requests are heavily rate-limited)
  GITHUB_REPOSITORY_OWNER   account to report on (default: techmech-keeb)

Content rules honored here (see AGENTS.md):
  - Only merged pull requests are listed; open or closed-unmerged ones are
    excluded (content-sources policy: defer unmerged contributions).
  - A PR title containing "TrackPoint" is not used as link text; the
    owner/repo#number reference is used instead (terminology rule).
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "techmech-keeb")
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")
START = "<!-- EXTERNAL-CONTRIBUTIONS:START -->"
END = "<!-- EXTERNAL-CONTRIBUTIONS:END -->"
API = "https://api.github.com/search/issues"


def fetch_merged_prs():
    """Return raw search items for merged PRs outside the account."""
    token = os.environ.get("GITHUB_TOKEN", "")
    query = "is:pr is:merged author:{0} -user:{0}".format(OWNER)
    items = []
    for page in range(1, 11):  # search API caps results at 1000
        params = urllib.parse.urlencode(
            {
                "q": query,
                "per_page": 100,
                "page": page,
                "sort": "created",
                "order": "asc",
                "advanced_search": "true",
            }
        )
        req = urllib.request.Request("{}?{}".format(API, params))
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        if token:
            req.add_header("Authorization", "Bearer {}".format(token))
        with urllib.request.urlopen(req) as resp:
            data = json.load(resp)
        batch = data.get("items", [])
        items.extend(batch)
        if not batch or len(items) >= data.get("total_count", 0):
            break
    return items


def normalize(items):
    """Convert search items to a list of PR dicts, newest repo group first."""
    prs = []
    for item in items:
        pr_info = item.get("pull_request") or {}
        if not pr_info.get("merged_at"):
            continue  # search said merged, but double-check
        repo = "/".join(item["repository_url"].rstrip("/").split("/")[-2:])
        if repo.split("/")[0].lower() == OWNER.lower():
            continue  # own repository; defensive, the query already excludes
        prs.append(
            {
                "repo": repo,
                "number": item["number"],
                "title": (item.get("title") or "").strip(),
                "url": item["html_url"],
                "merged": pr_info["merged_at"][:10],
            }
        )
    return prs


def _link_text(pr):
    title = pr["title"]
    if not title or "trackpoint" in title.lower():
        # Terminology rule: never surface "TrackPoint" as visible link text.
        return "{}#{}".format(pr["repo"], pr["number"])
    return title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def render(prs):
    """Render the markdown block that goes between the markers."""
    if not prs:
        return "_No merged external pull requests found._"
    groups = {}
    for pr in prs:
        groups.setdefault(pr["repo"], []).append(pr)
    # Repositories with the most recent merge first; PRs chronologically.
    ordered = sorted(
        groups.items(),
        key=lambda kv: max(p["merged"] for p in kv[1]),
        reverse=True,
    )
    lines = []
    for repo, repo_prs in ordered:
        lines.append("### [{}](https://github.com/{})".format(repo, repo))
        lines.append("")
        for pr in sorted(repo_prs, key=lambda p: (p["merged"], p["number"])):
            lines.append(
                "- [{}]({}) — merged {}".format(_link_text(pr), pr["url"], pr["merged"])
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_block(readme_text, block):
    """Return readme_text with the marker block replaced by `block`."""
    if START not in readme_text or END not in readme_text:
        raise SystemExit(
            "README.md is missing the {} / {} markers".format(START, END)
        )
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END), flags=re.DOTALL
    )
    return pattern.sub(START + "\n" + block + "\n" + END, readme_text, count=1)


def main():
    try:
        items = fetch_merged_prs()
    except urllib.error.URLError as exc:
        print("GitHub search request failed: {}".format(exc), file=sys.stderr)
        return 1
    prs = normalize(items)
    with open(README, encoding="utf-8") as fh:
        old = fh.read()
    new = replace_block(old, render(prs))
    if new == old:
        print("README.md unchanged ({} merged external PRs).".format(len(prs)))
        return 0
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)
    print("README.md updated ({} merged external PRs).".format(len(prs)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
