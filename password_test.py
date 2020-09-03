import unittest
from password import User , Credential


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Langat", "justo01", "justo1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name, "Langat")
        self.assertEqual(self.new_user.username, "justo01")
        self.assertEqual(self.new_user.password, "justo1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''

        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo1234")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''

        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo12345")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by name and display information
        '''

        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo1234")
        test_user.save_user()

        found_user = User.find_user_by_name("Langat")

        self.assertEqual(found_user.username,test_user.username) 

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Langat", "justo01", "justo1234")
        test_user.save_user()
        
        user_exists = User.user_exist("Langat")

        self.assertTrue(user_exists)

    class TestCredential(unittest.TestCase):
        def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_credential = Credential("Langat","twitter", "justo01","justo1234")

        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_credential.name,"Langat")
            self.assertEqual(self.new_credential.account,"twitter")
            self.assertEqual(self.new_credential.username,"justo01")
            self.assertEqual(self.new_credential.password,"justo12345")        

if __name__ == '__main__':
    unittest.main()
