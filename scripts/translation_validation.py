"""Validate community catalogs without Valheim or third-party Python packages."""
import argparse
import json
import re
from pathlib import Path

PREFIX = "runestonerecords_"
PLACEHOLDER = re.compile(r"\{(\d+)(?:,-?\d+)?(?::[^{}]*)?\}")


def placeholders(value):
    indexes = set()
    i = 0
    while i < len(value):
        char = value[i]
        if char in "{}" and value[i:i + 2] == char * 2:
            i += 2
            continue
        if char == "{":
            match = PLACEHOLDER.match(value, i)
            if not match or int(match[1]) > 31:
                raise ValueError("invalid numbered placeholder")
            indexes.add(int(match[1]))
            i = match.end()
            continue
        if char == "}":
            raise ValueError("unmatched closing brace")
        i += 1
    return indexes


def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_catalog(text):
    result = json.loads(text.lstrip("\ufeff"), object_pairs_hook=_unique_pairs)
    if not isinstance(result, dict):
        raise ValueError("catalog must be a JSON object")
    for key, value in result.items():
        if not key.startswith(PREFIX):
            raise ValueError(f"invalid translation key: {key}")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key}: value must be a nonempty string")
        if re.search(r"</?[a-zA-Z][^>]*>", value):
            raise ValueError(f"{key}: use plain text, without markup tags")
        placeholders(value)
    return result


def validate_catalog(values, english, complete=False):
    unknown = values.keys() - english.keys()
    if unknown:
        raise ValueError("unknown keys: " + ", ".join(sorted(unknown)))
    if complete and values.keys() != english.keys():
        raise ValueError("missing keys: " + ", ".join(sorted(english.keys() - values.keys())))
    for key, value in values.items():
        if placeholders(value) != placeholders(english[key]):
            raise ValueError(f"{key}: placeholders differ from English")


def validate_directory(directory, languages, complete=False):
    directory = Path(directory)
    paths = {p.stem: p for p in directory.glob("*.json")}
    if set(paths) != set(languages):
        raise ValueError("language filenames do not match languages.json")
    english = parse_catalog(paths["English"].read_text(encoding="utf-8-sig"))
    if not english:
        raise ValueError("English catalog is empty")
    catalogs = {}
    for language in languages:
        values = parse_catalog(paths[language].read_text(encoding="utf-8-sig"))
        validate_catalog(values, english, complete)
        catalogs[language] = values
    return catalogs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    languages = json.loads((args.root / "languages.json").read_text(encoding="utf-8"))
    catalogs = validate_directory(args.root / "Translations", languages, args.require_complete)
    english = catalogs["English"]
    for language, values in catalogs.items():
        different = sum(value != english[key] for key, value in values.items())
        print(f"{language}: {len(values)}/{len(english)} keys, {different} values different from English")
    print("Translation validation passed. Differences measure text changes, not translation quality.")


if __name__ == "__main__":
    main()
