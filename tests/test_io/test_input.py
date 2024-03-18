import os
import unittest
import app.io.input as inp


class DefaultFileInput(unittest.TestCase):

    def test_exist_file(self):
        """Check to see if an existing file is being read correctly.
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'test_table.csv')
        expected_text = "Hello,World,It's,me,!\n"
        self.assertEqual(inp.default_file_input(filename), expected_text)

    def test_not_exist_file(self):
        """Check to see if a non-existent file has been detected correctly.
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'test_table_new.csv')
        with self.assertRaises(FileNotFoundError):
            inp.default_file_input(filename)

    def test_empty_file(self):
        """Check for correct processing of an empty file.
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'empty_file.csv')
        self.assertEqual(inp.default_file_input(filename), "")


if __name__ == '__main__':
    unittest.main()
