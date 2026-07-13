# Techmech keys

Independent keyboard designer and maker based in Japan.

I design compact custom keyboards that combine ortholinear layouts, standard keycap compatibility, and integrated pointing-stick input. My projects extend from physical products to firmware, documentation, and software for real-world demonstrations.

日本で自作キーボードの設計・製造・販売を行っています。格子配列、標準キーキャップ互換、ポインティングスティックによる操作体験を軸に、実機で検証しながら製品を開発しています。

**Primary links:** [OLSK60 v2](https://github.com/techmech-keeb/OLSK60_v2) · [X updates](https://x.com/techmech_) · [BOOTH](https://techmech.booth.pm/items/5896343) · [遊舎工房](https://shop.yushakobo.jp/products/11324) · [Community](#community-and-updates)

![OLSK60 v2.1 ortholinear keyboard with an integrated pointing stick](https://github.com/user-attachments/assets/2aa9d79e-fb0d-4367-8551-9987699a8846)

## What I build

- Compact custom keyboard products centered on the OLSK60 series.
- Ortholinear layouts designed to work with commonly available keycap sets.
- Integrated pointing-stick user experiences that keep pointer movement close to typing.
- Firmware, documentation, and demonstration software for physical products.

## Design principles

- Keep keyboard and pointer interaction close to the home row.
- Preserve compatibility with commonly available keycaps and GH60-compatible cases.
- Validate ideas on physical hardware, repeated prototypes, and real use.
- Design the product, documentation, and demonstration experience together.

## Featured projects

### OLSK60 v2.1

[OLSK60 v2](https://github.com/techmech-keeb/OLSK60_v2) is the main Techmech keys product: a 60% ortholinear keyboard with standard keycap compatibility and an integrated pointing stick. It is designed for GH60-compatible cases, so users can combine the keyboard with a broad range of cases and keycap sets while keeping pointer input within the keyboard. OLSK60 v2.1 is designed, produced, and sold by Techmech keys, with purchase pages available on [BOOTH](https://techmech.booth.pm/items/5896343) and [遊舎工房](https://shop.yushakobo.jp/products/11324).

### OLSK60 INPUT LAB

[OLSK60 INPUT LAB](https://github.com/techmech-keeb/keyboard_and_pointer_tester) is demonstration software for exhibitions and retail settings. It visualizes keyboard and pointer input, provides typing tests, and supports kiosk-style Windows operation so visitors can experience the product without setup friction. The project also connects with Raw HID and Vial workflows without documenting the product's internal input implementation.

### 1U Rotary Encoder Switch — KiCad Library

[1U Rotary Encoder Switch](https://github.com/techmech-keeb/1U_Rotary_Encoder_Footprint) is a reusable KiCad symbol and footprint for placing a rotary encoder in a Cherry MX switch position. The library was independently measured and created, is used in OLSK60, and is published as an open-hardware asset under CERN-OHL-P-2.0. This does not mean the full OLSK60 product design is open hardware.

## Open-source contributions

- Fixed extended user-keycode conversion in RMK so User16 through User31 are handled correctly in VIA/Vial conversion ([HaoboGu/rmk#928](https://github.com/HaoboGu/rmk/pull/928)).
- Added ClearEeprom handling and VIA/Vial mapping to RMK ([HaoboGu/rmk#931](https://github.com/HaoboGu/rmk/pull/931)).

Both changes were submitted with corresponding tests and merged upstream.

## Community and updates

- **GitHub** is used for public projects, documentation, releases, and upstream open-source contributions.
- **X** is the main place for product photos, event notes, sales updates, completed builds, prototypes, and short progress updates: <https://x.com/techmech_>.
- **Reddit** is used to share keyboard builds and design discussions with English-language communities such as MechanicalKeyboards, OLKB, and ErgoMechKeyboards.

## Contact

- For updates, follow [X](https://x.com/techmech_).
- For reproducible issues in public software or documentation, use the Issues page of the relevant GitHub repository.
- For purchase and shipping questions, use the contact channel of the purchase destination where appropriate.

Techmech keys is an independent maker project. Support is provided on a best-effort basis.
