# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import unittest
from contact import Contact
from application import Application

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.filling_fields(Contact(firstname="ewfweqf", middlename="erferfg", lastname="wfqwvdv",
                            nickname="wfefr", title="wfewqc", company="cwef", address="wfeqrr",
                            phonehome="2343", phonemobile="5432", phonework="34345", phonefax="3453",
                            email="rr@tt.oo", email2="dsfd@err.yy", email3="dvdfwe@tt.yy", homepage="fewfrew",
                            bday="28", bmonth="October", byear="4000", aday="28", amonth="October", ayear="1000"))
        self.app.logaut()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
