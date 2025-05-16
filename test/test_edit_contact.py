from model.contact import Contact
from random import randrange


def test_edit_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test_first"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="111111", middlename="2222", lastname="3333",
                    nickname="4444", title="5555", company="6666", address="7777",
                    phonehome="888", phonemobile="999", phonework="1010", phonefax="1111",
                    email="11@11.oo", email2="22@22.yy", email3="33@33.yy", homepage="44",
                    bday="27", bmonth="May", byear="1111", aday="11", amonth="July", ayear="2222")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test_first"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="new firstname")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index].firstname = contact.firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

