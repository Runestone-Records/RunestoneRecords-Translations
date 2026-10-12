import unittest
from translation_validation import parse_catalog, placeholders, validate_catalog


class ValidationTests(unittest.TestCase):
    def test_placeholders(self):
        self.assertEqual(placeholders("{{text}} {1} {0}"), {0, 1})
        for value in ("{", "}", "{32}", "{name}"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                placeholders(value)

    def test_bad_json(self):
        for value in ('[]', '{bad', '{"runestonerecords_x":null}', '{"runestonerecords_x":""}',
                      '{"runestonerecords_x":"a","runestonerecords_x":"b"}',
                      '{"runestonerecords_x":"<b>text</b>"}'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_catalog(value)

    def test_partial_translation(self):
        english = {"runestonerecords_a": "Text", "runestonerecords_b": "{0}: {1}"}
        validate_catalog({"runestonerecords_b": "{1} de {0}"}, english)
        with self.assertRaises(ValueError):
            validate_catalog({"runestonerecords_b": "{0}"}, english)
        with self.assertRaises(ValueError):
            validate_catalog({"runestonerecords_unknown": "Text"}, english)


if __name__ == "__main__":
    unittest.main()
