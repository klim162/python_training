import re
from random import randrange
from model.contact import Contact

def test_contact_filds_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="ewfweqf", middlename="erferfg", lastname="wfqwvdv",
                    nickname="wfefr", title="wfewqc", company="cwef", address="wfeqrr",
                    phonehome="2343", phonemobile="5432", phonework="34345", phonefax="3453",
                    email="rr@tt.oo", email2="dsfd@err.yy", email3="dvdfwe@tt.yy", homepage="fewfrew",
                    bday="28", bmonth="October", byear="4000", aday="28", amonth="October", ayear="1000"))
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = contacts_from_home_page[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_mail_from_homepage == merge_email_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phonehome, contact.phonemobile, contact.phonework]))))

def merge_email_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))