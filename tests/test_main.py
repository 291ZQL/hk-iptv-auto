import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import main


class MainConfigTests(unittest.TestCase):
    def test_source_urls_are_not_concatenated(self):
        self.assertTrue(main.SOURCE_URLS)
        for url in main.SOURCE_URLS:
            self.assertTrue(url.startswith("http"), f"Invalid URL entry: {url!r}")
            self.assertLessEqual(url.count("https://"), 1, f"Concatenated URL entry: {url!r}")


if __name__ == "__main__":
    unittest.main()
