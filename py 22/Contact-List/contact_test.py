import sys
print(sys.executable)
import unittest # Importing the unittest module
from contact import Contact # Importing the contact class
import pyperclip

class TestContact(unittest.TestCase):
    
    def setUp(self):
    
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object
    #first test1
    def test_init(self):
    
        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    if __name__ == '__main__':
        unittest.main()
    #second test1
    def test_save_contact(self):  #METHOD 
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)
    
    if __name__ == '__main__':
        unittest.main()
    #third test1
    def tearDown(self):
        Contact.contact_list = []
        # other test cases here
    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    if __name__ == '__main__':
        unittest.main()
    #fourth test1
    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()

        self.new_contact.delete_contact()# Deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)

    

    if __name__ == '__main__':
        unittest.main()

    #fifth test1
    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()
        found_contact = Contact.find_by_number("0711223344")
        self.assertEqual(found_contact.email,test_contact.email)
    
    #end1

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)
        

    #end2

   #assertTrue
    def test_contact_exists(self):
        #setattr(new_contact , '0711223344' )
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()
        contact_exists = Contact.contact_exist("0711223344")
        self.assertTrue(contact_exists)

  
    #pyperclip    #had troubles installing this module on my device.
    def test_copy_email(self):
        self.new_contact.save_contact()
        Contact.copy_email("0712345678")
        self.assertEqual(self.new_contact.email,pyperclip.paste())
    
    
    