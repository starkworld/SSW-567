import unittest
from HW04a import get_user_repos, get_commit_counts


class TestGitHub(unittest.TestCase):
    """Test cases for github repo program"""
    def testGitHub01(self):
        self.assertIn("SSW-567", get_user_repos("starkworld"))

    def testGitHub02(self):
        self.assertNotIn("HelloWorld", get_user_repos("starkworld"))

    def testGitHub03(self):
        self.assertEqual(20, get_commit_counts("starkworld", "Student_DB_Repository"))

    def testGitHub04(self):
        self.assertIn("Future-Sales-Prediction", get_user_repos("starkworld"))

    def testGitHub05(self):
        self.assertNotIn("Empire", get_user_repos("starkworld"))

    def testGitHub06(self):
        self.assertNotEqual(42, get_commit_counts("starkworld", "SSW-567"))

    def testGitHub07(self):
        self.assertEqual([], get_user_repos("FakeUser099"))


if __name__ == '__main__':
    print('Unittest are Running')
    unittest.main()
