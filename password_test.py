import unittest
from password import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Langat","justo01","justo1234")

    def test_init(self):
        self.assertEqual(self.new_user.name,"Langat")
        self.assertEqual(self.new_user.username,"justo01")
        self.assertEqual(self.new_user.password,"justo1234")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        User.user_list = []


if __name__ == '__main__':
    unittest.main()        