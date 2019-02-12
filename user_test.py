import unittest # Importing the unittest module
from user import User# Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("marie claire","mukasine","0782586013","mclaremukasine@gmail.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"marie claire")
        self.assertEqual(self.new_user.last_name,"mukasine")
        self.assertEqual(self.new_user.phone_number,"0782586013")
        self.assertEqual(self.new_user.email,"mclaremukasine@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


# Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Ingabire","claudine","0784155924","ingabiclaunine@gmail.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

            # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Ingabire","claudine","0784155924","ingabiclaudine@gmail.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

# More tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Ingabire","claudine","0784155924","ingabiclaudine@gmail.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()