# Contributing translations

Translate custom interface text in `Translations/<Language>.json`. Use natural wording for your language and Valheim's terminology where possible. Keep **Runestone Records** unchanged.

## Editing

- Save UTF-8 JSON. Translate values, never keys or filenames.
- English is the reference. Change it only when coordinating new text or correcting a mistake with the maintainer.
- Preserve numbered placeholders and their format, such as `{0}`, `{1}` or `{0:0.0}`. You may reorder them.
- Use `{{` and `}}` for literal braces, `\n` for line breaks and `\"` for quotation marks.
- Use plain text, without HTML, BBCode or TextMeshPro tags.
- Leave unfamiliar text in English, or omit it for English fallback. Do not add empty values.
- Keep the native language filenames listed in `languages.json`.

Example:

```json
{
  "runestonerecords_tab_achievements": "Logros",
  "runestonerecords_tab_statistics": "Estadísticas",
  "runestonerecords_tracker_more": "… +{0} más"
}
```

## Test a translation before merging

You can test your own changes or someone else's open pull request **without merging it or rebuilding the mod**. No Git installation or compiler is needed.

### 1. Get a localization-enabled build

Install Runestone Records **1.5.0-beta or a later localization-enabled release**, with its required BepInEx and Jötunn dependencies. Earlier releases do not load these language files. If a localization-enabled build is not available in the mod's downloads yet, request the beta from the maintainer.

Launch Valheim once with that build, then close the game. The mod creates editable language files in its config directory.

### 2. Download the translation from the PR

Open the pull request and find `Translations/<Language>.json` under **Files changed**. Open the file from the PR's source branch and download its **raw JSON**. Downloading from `main` instead gives you the currently merged version, not the proposed translation.

You can also use the JSON you are editing locally. Keep its exact filename, for example `Portuguese_Brazilian.json`. Save it as UTF-8 JSON, not an HTML page or a file ending in `.json.txt`.

### 3. Put it in the active config directory

Back up your existing language JSON outside the `Translations` directory if you have personal edits. Copy the downloaded file into:

```text
Valheim/BepInEx/config/RunestoneRecords/Translations/<Language>.json
```

For Brazilian Portuguese, the full relative path is:

```text
Valheim/BepInEx/config/RunestoneRecords/Translations/Portuguese_Brazilian.json
```

If you use a mod manager, use the **active profile's** `BepInEx/config` directory. Files in this repository or beside the plugin DLL are reference copies; runtime customizations must go in **config**.

Do not edit the managed `.bundled-baselines` subdirectory. It lets untouched entries follow updated bundled translations while preserving your actual edits.

### 4. Check it in game

Restart Valheim, select the matching language in the game's settings, load a character, and press **F7**.

- Check both **Achievements** and **Statistics**: categories, filters, buttons, search results and progress summaries.
- Expand achievements and statistics to check requirements, collection entries, difficulty labels and combat methods.
- Pin a goal to check the HUD tracker. Resize both windows to look for clipped or awkwardly wrapped text.
- Check accents and special characters. Switch the game language to confirm the journal and tracker refresh correctly.

Native achievement names, descriptions, items, creatures and building pieces still use Valheim's translations. The JSON translates the mod's custom interface text, and **Runestone Records** stays unchanged.

### 5. Iterate and report results

After changing the JSON, **restart Valheim** to reload it. Switching the game language does not reload files edited on disk.

Missing entries fall back to bundled text or English. If text unexpectedly stays in English, check the filename, selected language and active config directory, then inspect `BepInEx/LogOutput.log` for Runestone Records warnings about malformed JSON or invalid placeholders.

Include testing results in your PR or review: build used, language, screens checked, and any wording or layout problems. If you could not test in game, say so; partial or untested contributions are still welcome when clearly described.

To stop testing, restore your backed-up JSON and restart. If you had no personal edits to preserve, delete the test language JSON; the next launch regenerates it from the bundled catalog.

## Submit

Fork the repository, edit the language file and open a pull request. GitHub's browser editor can create a branch and pull request for you. No local Git setup is required.

Include your language, a short explanation, in-game testing results (if any), and your preferred credit. Automated checks catch structural mistakes; a human still reviews wording and layout. An untested or partial translation is welcome when clearly described.

By submitting a contribution, you agree to include it under this repository's MIT license. Submit only text you are entitled to contribute.

## Maintainer process

Review the translation and passing checks before merging. Keep English and `languages.json` coordinated with the mod's current key and installed-language lists. Protect canonical files with CODEOWNERS and require the validation check where repository settings permit it.

For a release, sync a full approved commit SHA into the private mod project, then build using `tools/build_localized_beta.py`. Do not build directly from an unreviewed pull request or a moving branch.
