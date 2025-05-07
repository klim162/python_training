from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def filling_contact_form(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(text)

    def fild_select_list(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fild_name).click()
            Select(wd.find_element_by_name(fild_name)).select_by_visible_text(text)

    def filling_fields(self, contact):
        wd = self.app.wd
        self.filling_contact_form("firstname", contact.firstname)
        self.filling_contact_form("middlename", contact.middlename)
        self.filling_contact_form("lastname", contact.lastname)
        self.filling_contact_form("nickname", contact.nickname)
        self.filling_contact_form("title", contact.title)
        self.filling_contact_form("company", contact.company)
        self.filling_contact_form("address", contact.address)
        self.filling_contact_form("home", contact.phonehome)
        self.filling_contact_form("mobile", contact.phonemobile)
        self.filling_contact_form("work", contact.phonework)
        self.filling_contact_form("fax", contact.phonefax)
        self.filling_contact_form("fax", contact.phonefax)
        self.filling_contact_form("email", contact.email)
        self.filling_contact_form("email2", contact.email2)
        self.filling_contact_form("email3", contact.email3)
        self.filling_contact_form("homepage", contact.homepage)
        self.fild_select_list("bday", contact.bday)
        self.fild_select_list("bmonth", contact.bmonth)
        self.filling_contact_form("byear", contact.byear)
        self.fild_select_list("aday", contact.aday)
        self.fild_select_list("amonth", contact.amonth)
        self.filling_contact_form("ayear", contact.ayear)

    def add_contact(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        #filling fields
        self.filling_fields(contact)
        # sending the result
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # edit first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #filling fields
        self.filling_fields(contact)
        # sending the result
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))