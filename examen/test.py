import unittest
from main import get_file_extension

class TestGetFileExtension(unittest.TestCase):

    def test_normal_file(self):
        self.assertEqual(get_file_extension("document.txt"), "txt")
        self.assertEqual(get_file_extension("archive.tar.gz"), "gz")  # останнє розширення

    def test_no_extension(self):
        self.assertEqual(get_file_extension("README"), "")

    def test_hidden_file(self):
        self.assertEqual(get_file_extension(".gitignore"), "")
        self.assertEqual(get_file_extension(".env.local"), "local")  # якщо є ще крапка після першої

if __name__ == "__main__":
    unittest.main()
