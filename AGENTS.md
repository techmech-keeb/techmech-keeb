# AGENTS.md

Guidance for future Codex and AI-agent updates in this repository.

## Scope

- This repository is dedicated to the GitHub profile README for Techmech keys.
- Product repositories are the source of truth for product specifications.
- Do not duplicate firmware, CAD, PCB, or design files here.
- Do not modify other repositories while updating this profile repository.

## Terminology

- Primary Japanese term: ポインティングスティック
- Primary English term: pointing stick
- TrackPoint must not be used as a product name.
- TrackPoint must not be used in headings, badges, alt text, or GitHub topics.
- TrackPoint may appear at most once in the README body as a recognition aid
  or trademark note. The single allowed mention is currently used in the
  introduction paragraph.
- URLs (for example Reddit permalinks) do not count toward the one-mention
  limit; visible link text does. Use descriptive link text instead of quoting
  post titles that contain TrackPoint.
- Do not imply Lenovo affiliation, endorsement, licensing, or compatibility.

## Confidentiality

Do not add unpublished or reproducible implementation details for proprietary product subsystems.

Do not add or summarize:

- schematics
- PCB routing
- part numbers
- pin assignments
- electrical interfaces
- initialization procedures
- calibration methods
- sensitivity algorithms
- firmware internals
- unpublished configuration files
- disassembled hardware images

## Source of truth

- Current OLSK60 specifications: `techmech-keeb/OLSK60_v2`
- OLSK60 INPUT LAB: `techmech-keeb/keyboard_and_pointer_tester`
- 1U encoder library: `techmech-keeb/1U_Rotary_Encoder_Footprint`
- RMK contributions: upstream pull requests in `rmk-rs/rmk`
- Sales status: product README files and sales pages
- X and Reddit: linked posts and profiles only
- Do not store dynamic statistics in the README.

## Privacy

Do not add:

- real names
- employers
- job titles
- addresses
- family information
- day-job responsibilities
- private repositories
- private email addresses

## Writing rules

- English first.
- Japanese content is limited to a short introduction near the top and one
  compact Japanese summary section (features, purchase, support). Do not
  fully duplicate the English content in Japanese.
- Keep wording factual and restrained.
- Put product value before technical details.
- Avoid generic AI marketing language.
- Do not add unverified claims.
- Reddit posts may be linked with descriptive link text; do not present
  invented text as a post title, and do not quote titles that contain
  TrackPoint (see Terminology).
- Do not include dynamic statistics. Stock states change between production
  runs, so describe restock paths (BOOTH restock notification, X) instead of
  asserting current availability.
- Do not disclose implementation details.
