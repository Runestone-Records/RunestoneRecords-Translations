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

## Test locally

1. Install Runestone Records 1.5.0-beta or a later localization-enabled release.
2. Launch Valheim once, then close it.
3. Copy your language file to `Valheim/BepInEx/config/RunestoneRecords/Translations/<Language>.json`.
4. Restart Valheim and select your language in the game's settings.
5. Check Achievements and Statistics, search, categories, buttons, expanded requirements, progress summaries and the tracker. Resize both windows and test long labels and special characters.

Files beside the plugin are reference copies. Runtime customizations belong in the **config** directory. Edits require restarting Valheim. Do not edit the managed `.bundled-baselines` directory; it lets untouched entries follow updated bundled translations.

## Submit

Fork the repository, edit the language file and open a pull request. GitHub's browser editor can create a branch and pull request for you. No local Git setup is required.

Include your language, a short explanation, in-game testing results (if any), and your preferred credit. Automated checks catch structural mistakes; a human still reviews wording and layout. An untested or partial translation is welcome when clearly described.

By submitting a contribution, you agree to include it under this repository's MIT license. Submit only text you are entitled to contribute.

## Maintainer process

Review the translation and passing checks before merging. Keep English and `languages.json` coordinated with the mod's current key and installed-language lists. Protect canonical files with CODEOWNERS and require the validation check where repository settings permit it.

For a release, sync a full approved commit SHA into the private mod project, then build using `tools/build_localized_beta.py`. Do not build directly from an unreviewed pull request or a moving branch.
