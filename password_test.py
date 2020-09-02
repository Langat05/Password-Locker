import unittest
from password import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Langat","justo01","justo1234")


if __name__ == '__main__':
    unittest.main()        