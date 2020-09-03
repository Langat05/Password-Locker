import unittest
from password import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Langat", "justo01", "justo1234")

    def test_init(self):
        self.assertEqual(self.new_user.name, "Langat")
        self.assertEqual(self.new_user.username, "justo01")
        self.assertEqual(self.new_user.password, "justo1234")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        User.user_list = []

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo1234")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo12345")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_name(self):

        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo1234")
        test_user.save_user()

        found_user = User.find_user_by_name("Langat")

        self.assertEqual(found_user.username,test_user.username) 


if __name__ == '__main__':
    unittest.main()
