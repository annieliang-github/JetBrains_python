import unittest

# from file_name import *
from login_system import *

class LoginSystem_Tests(unittest.TestCase):

    #this will run before every test function
    def setUp(self):

        #dictionaries for testing
        self.users, self.loggedin = init_db('users.csv')

    def test_init_db_user(self):

        # test total number of users in file
        self.assertEqual(10, len(self.users.keys()))

        #test for couple of users
        self.assertIn('lbrandon', self.users)
        self.assertIn('chenyunw', self.users)

        #test their passwords
        self.assertEqual('t39iSd_', self.users['kjain20'])
        self.assertEqual('_.R43sW2', self.users['caizhe'])
    
    def test_init_db_loggin(self):
        self.assertFalse(bool(self.loggedin))

    def test_check_username_password_valid_user(self):
        self.assertTrue(check_username_password(self.users, 'lbrandon', '2w3e4r5T'))
        self.assertTrue(check_username_password(self.users, 'chenyunw', '9i8u7y6T'))
        self.assertFalse(check_username_password(self.users, 'chenyun','9i8u7y6T'))

    def test_check_username_password_valid_password(self):

        #wrong passwords
        self.assertFalse(check_username_password(self.users, 'huize', '9i2w6tqw1'))
        self.assertFalse(check_username_password(self.users, 'haicao', 'QwertyuiI'))

    def test_is_valid_password_length(self):
        self.assertTrue(is_valid_password('s.34r3T5'))
        self.assertTrue(is_valid_password('8i7u6_T4'))
        self.assertFalse(is_valid_password('0oiu87H'))

    def test_is_valid_password(self):

        #no lowercase char
        self.assertFalse(is_valid_password('W2E3R4T5'))

        #no uppercase char
        self.assertFalse(is_valid_password('6y5t4r3e_'))

        #no number
        self.assertFalse(is_valid_password('sewdRty_'))

    def test_sign_up_valid_cases(self):
        #successfully sign somebody in
        sign_up(self.users, self.loggedin, 'steddy', 'b3rs6eR9')

        #in db
        self.assertIn('steddy', self.users)
        self.assertEqual(self.users["steddy"],"b3rs6eR9")

        # don't test logged_in as someone may not put not logged_in users into logged_in

    def test_sign_up_invalid_cases(self):

        #user exists
        sign_up(self.users, self.loggedin, 'dingyis', '8d3wTR4_')
        # check original username and password in db
        self.assertEqual(self.users["dingyis"], "2w9i4oT")

        #no uppercase in pwd
        sign_up(self.users, self.loggedin, 'bryanj', '3267rt_o')
        # not in db
        self.assertNotIn("bryanj", self.users)

        #no lowercase in pwd
        sign_up(self.users, self.loggedin, 'bryanj', '3267RT_O')
        # still not in db
        self.assertNotIn("bryanj", self.users)

        #no number in pwd
        sign_up(self.users, self.loggedin, 'bryanj', 'REDDrt_o')
        # still not in db
        self.assertNotIn("bryanj", self.users)

        #no enough chars in pwd
        sign_up(self.users, self.loggedin, 'bryanj', '123ascD')
        # still not in db
        self.assertNotIn("bryanj", self.users)

    def test_log_in(self):

        #successfully log somebody in
        log_in(self.users, self.loggedin, 'caizhe', '_.R43sW2')
        #logged in
        self.assertIn('caizhe', self.loggedin)
        self.assertTrue(self.loggedin['caizhe'])

        # the same user log in
        log_in(self.users, self.loggedin, 'caizhe', '_.R43sW2')
        # still logged in
        self.assertIn('caizhe', self.loggedin)
        self.assertTrue(self.loggedin['caizhe'])

        #user doesn't exist
        log_in(self.users, self.loggedin, 'william', '9i8u7y65DW3')
        # not logged in
        self.assertNotIn('william', self.loggedin)

        #bad pwd
        log_in(self.users, self.loggedin, 'kjain20', '_t39iSd_')
        #not logged in
        self.assertNotIn('kjain20', self.loggedin)

    def test_change_password(self):

        #successfully change password
        change_password(self.users, 'paranyaj', 'bvcxZs43', 'rwt23eWW1')
        #check password
        self.assertEqual('rwt23eWW1', self.users['paranyaj'])

        #wrong old password
        change_password(self.users, 'paranyaj', 'bvcxZs43', '0o9i8u7Y')
        # check password again
        self.assertEqual('rwt23eWW1', self.users['paranyaj'])

    def test_delete_account(self):

        delete_account(self.users, self.loggedin, 'chenyunw','9i8u7y6T')
        #user should be removed from db
        self.assertNotIn('chenyunw', self.users)
        self.assertNotIn('chenyunw', self.loggedin)

        #bad password
        delete_account(self.users, self.loggedin, 'kjain20', 't39iSd')
        # user should not be removed
        self.assertIn('kjain20', self.users)

        # user doesn't exist
        delete_account(self.users, self.loggedin, 'sarahq', '1234rftY')
        # obviously, not in
        self.assertNotIn('sarahq', self.users)
        self.assertNotIn('sarahq', self.loggedin)

    def test_get_sign_ups(self):
        # init
        names = ["lbrandon","chenyunw","dingyis","caizhe","chuanrui","kjain20","huize","paranyaj","caor","tianshiw"]
        self.assertCountEqual(names, get_sign_ups(self.users))

        # sign up one user
        sign_up(self.users, self.loggedin, 'steddy', 'b3rs6eR9')
        names.append("steddy")
        self.assertCountEqual(names, get_sign_ups(self.users))

        # delete one user
        delete_account(self.users, self.loggedin, 'steddy','b3rs6eR9')
        names = ["lbrandon","chenyunw","dingyis","caizhe","chuanrui","kjain20","huize","paranyaj","caor","tianshiw"]
        self.assertCountEqual(names, get_sign_ups(self.users))
    
    def test_get_log_in(self):
        # sign up one user, but not log in
        # sign_up(self.users, self.loggedin, 'steddy', 'b3rs6eR9')
        # self.assertEqual(0,len(get_log_ins(self.loggedin)))

        # log in
        log_in(self.users, self.loggedin, 'caizhe', '_.R43sW2')
        log_in(self.users, self.loggedin, 'chenyunw', '9i8u7y6T')
        self.assertCountEqual(["caizhe", "chenyunw"], get_log_ins(self.loggedin))

        #delete 
        delete_account(self.users, self.loggedin, 'chenyunw','9i8u7y6T')
        self.assertCountEqual(["caizhe"], get_log_ins(self.loggedin))

    def test_write(self):
        write_users_db(self.users, "output.txt")

if __name__ == '__main__':
    unittest.main()