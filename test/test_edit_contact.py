from model.contact import Contact


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test_first"))
    app.contact.edit_first_contact(Contact(firstname="111111", middlename="2222", lastname="3333",
                    nickname="4444", title="5555", company="6666", address="7777",
                    phonehome="888", phonemobile="999", phonework="1010", phonefax="1111",
                    email="11@11.oo", email2="22@22.yy", email3="33@33.yy", homepage="44",
                    bday="27", bmonth="May", byear="1111", aday="11", amonth="July", ayear="2222"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_firstname_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test_first"))
    app.contact.edit_first_contact(Contact(firstname="new firstname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
