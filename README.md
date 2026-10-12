# Runestone Records — Community Translations

Help make the Valheim achievement and statistics journal available in your language.

This repository contains the mod's custom interface text. Valheim supplies native achievement names, descriptions, items, creatures and building pieces. **Runestone Records** stays untranslated.

## Translate a language

1. Open your file in [Translations](Translations).
2. Edit the values on the right, leaving the `runestonerecords_` keys unchanged.
3. Keep all numbered placeholders, such as `{0}` and `{1}`. Reordering them is fine.
4. Submit a pull request with your language, a brief summary, and whether you tested it in game.

Partial translations are welcome. Missing entries fall back to English. You can edit a file directly through GitHub; no game assemblies, mod source or compiler are required to contribute.

See [CONTRIBUTING.md](CONTRIBUTING.md) for examples, local testing and review guidance. If you prefer, attach your JSON file to an issue instead.

## Current status

English is the canonical catalog. Spanish is fully translated. The other 34 game languages initially contain English templates and are waiting for contributors. A file's existence does **not** mean it has been translated.

[languages.json](languages.json) uses Valheim's exact language names, including `Portuguese_Brazilian` and `Chinese_Trad`. Each initial catalog has 306 keys.

## Validation

Pull requests and pushes run the **Validate translations** workflow. Locally, with Python 3.10 or later:

```shell
python scripts/validate.py
```

Checks cover JSON syntax, duplicate/unknown keys, empty values, plain text, matching numbered placeholders and language filenames. Missing keys are permitted outside English. Counts of values different from English describe text differences, not translation quality.

## Releases

Approved translations are included in normal mod releases. The maintainer syncs a specific reviewed commit and records it in `translations.lock.json`; the DLL embeds the resulting catalogs. Players do not need Git or an internet connection to use them.

New mod text is added to English first. The maintainer updates other templates without replacing existing translations. Community contributions never need to modify the mod's IDs or progress calculations.

## Credits

See [TRANSLATORS.md](TRANSLATORS.md). Include the name or handle you want credited in your pull request, or say that you prefer no attribution.

## Licensing

These catalogs and repository utilities use the [MIT license](LICENSE). Contributions are submitted under that license. No mod source code or game assets are included here; this license does not apply to the private mod project.
