import unittest
from credential import credential

class Testcredential(unittest.TestCase):

   
    def setUp(self):
        
        self.new_credential = credential("claudine","111") 


    def test_init(self):
        

        self.assertEqual(self.new_credential.username,"claudine")
        self.assertEqual(self.new_credential.password,"111")
        
    def test_save_credential(self):
        
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(credential.credential_list),1)
    #Items up here...
    def tearDown(self):
          
            credential.credential_list = []

    def test_save_multiple_credential(self):
            
            self.new_credential.save_credential()
            test_save_credential = credential("claudine","111") # new credential
            test_save_credential.save_credential()
            self.assertEqual(len(credential.credential_list),2)


if __name__ == '__main__':
    unittest.main()
