import re

def test_phone_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.phonehome == clear(contact_from_edit_page.phonehome)
    assert contact_from_home_page.phonemobile == clear(contact_from_edit_page.phonemobile)
    assert contact_from_home_page.phonework == clear(contact_from_edit_page.phonework)

def test_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phonehome == contact_from_edit_page.phonehome
    assert contact_from_view_page.phonemobile == contact_from_edit_page.phonemobile
    assert contact_from_view_page.phonework == contact_from_edit_page.phonework
    assert contact_from_view_page.phonefax == contact_from_edit_page.phonefax

def clear(s):
    return re.sub("[() -]", "", s)