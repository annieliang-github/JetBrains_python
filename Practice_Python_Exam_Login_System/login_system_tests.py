import unittest

from login_system import *

class LoginSystem_Tests(unittest.TestCase):

    # this will run before every test function
    def setUp(self):

        #dictionaries for testing
        self.users, self.loggedin = init_db('users.csv')

    def test_init_db(self):

        # test total number of users in file
        self.assertEqual(10, len(self.users.keys()))

        # test for couple of users
        self.assertIn('lbrandon', self.users)
        self.assertIn('chenyunw', self.users)

        # test their passwords
        self.assertEqual('t39iSd_', self.users['kjain20'])
        self.assertEqual('_.R43sW2', self.users['caizhe'])

    def test_check_username_password(self):

        #TODO Write at least 3 test cases
        pass

    def test_is_valid_password(self):

        #TODO Write at least 3 test cases
        pass

    def test_sign_up(self):

        #TODO Write at least 3 test cases
        pass

    def test_log_in(self):

        #TODO Write at least 3 test cases
        pass

    def test_change_password(self):

        #TODO Write at least 3 test cases
        pass

    def test_delete_account(self):

        #TODO Write at least 3 test cases
        pass


if __name__ == '__main__':
    unittest.main()