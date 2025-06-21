from selenium.webdriver.support.ui import Select
from model.contact import Contact
from selenium.webdriver.common.by import By
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def filling_contact_form(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, fild_name).click()
            wd.find_element(By.NAME, fild_name).clear()
            wd.find_element(By.NAME, fild_name).send_keys(text)

    def fild_select_list(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, fild_name).click()
            Select(wd.find_element(By.NAME, fild_name)).select_by_visible_text(text)

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
        wd.find_element(By.NAME, "submit").click()
        self.return_home_page()
        self.contact_cashe = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def open_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_contact_by_id(self, id):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element(By.CSS_SELECTOR, 'a[href="edit.php?id=%s"]' % id).click()

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        self.filling_fields(contact)
        # sending the result
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.contact_cashe = None

    def edit_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contact_by_id(id)
        self.filling_fields(contact)
        # sending the result
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.contact_cashe = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        self.return_home_page()
        self.contact_cashe = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        self.return_home_page()
        self.contact_cashe = None

    def return_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.return_home_page()
            self.contact_cashe = []
            for element in wd.find_elements(By.NAME, "entry"):
                sub_elements = element.find_elements(By.TAG_NAME, "td")
                # id = sub_elements[0].get_attribute("id")
                id = sub_elements[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                lastname_text = sub_elements[1].text
                firstname_text = sub_elements[2].text
                address = sub_elements[3].text
                all_mail = sub_elements[4].text
                all_phones = sub_elements[5].text
                self.contact_cashe.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id,
                                                  address=address, all_mail_from_homepage=all_mail,
                                                  all_phones_from_homepage=all_phones))
        return list(self.contact_cashe)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        phonehome = wd.find_element(By.NAME, "home").get_attribute("value")
        phonemobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        phonework = wd.find_element(By.NAME, "work").get_attribute("value")
        phonefax = wd.find_element(By.NAME, "fax").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2,
                       email3=email3, phonehome=phonehome, phonemobile=phonemobile, phonework=phonework, phonefax=phonefax)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        text = wd.find_element(By.ID, "content").get_attribute("innerHTML")
        phonehome = re.search(r'name="home"\s+value="([^"]+)"', text).group(1)
        phonemobile = re.search(r'name="mobile"\s+value="([^"]+)"', text).group(1)
        phonework = re.search(r'name="work"\s+value="([^"]+)"', text).group(1)
        phonefax = re.search(r'name="fax"\s+value="([^"]+)"', text).group(1)
        return Contact(phonehome=phonehome, phonemobile=phonemobile,
                       phonework=phonework, phonefax=phonefax)

    def select_add_group_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element(By.NAME, "to_group").click()
        wd.find_element(By.CSS_SELECTOR, 'select[name="to_group"] option[value="%s"]' % group_id).click()

    def select_group_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element(By.NAME, "group").click()
        wd.find_element(By.CSS_SELECTOR, 'select[name="group"] option[value="%s"]' % group_id).click()


    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(contact_id)
        self.select_add_group_by_id(group_id)
        wd.find_element(By.NAME, "add").click()
        self.return_home_page()

    def del_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_home_page()
        self.select_group_by_id(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element(By.NAME, "remove").click()
        self.return_home_page()
