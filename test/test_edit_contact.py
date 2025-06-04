from model.contact import Contact
import random


def test_edit_contact_by_id(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="test_first"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = Contact(firstname="111111", middlename="2222", lastname="3333",
                    nickname="4444", title="5555", company="6666", address="7777",
                    phonehome="888", phonemobile="999", phonework="1010", phonefax="1111",
                    email="11@11.oo", email2="22@22.yy", email3="33@33.yy", homepage="44",
                    bday="27", bmonth="May", byear="1111", aday="11", amonth="July", ayear="2222", id=contact_random.id)
    app.contact.edit_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact_random)] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
