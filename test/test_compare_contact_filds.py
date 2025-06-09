import re
from random import randrange
from model.contact import Contact

def test_contact_filds_on_home_page(app, db):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="ewfweqf", middlename="erferfg", lastname="wfqwvdv",
                    nickname="wfefr", title="wfewqc", company="cwef", address="wfeqrr",
                    phonehome="2343", phonemobile="5432", phonework="34345", phonefax="3453",
                    email="rr@tt.oo", email2="dsfd@err.yy", email3="dvdfwe@tt.yy", homepage="fewfrew",
                    bday="28", bmonth="October", byear="4000", aday="28", amonth="October", ayear="1000"))
    contacts_from_home_page = app.contact.get_contact_list()
    def clear(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address, all_mail=contact.all_mail, all_phones=contact.all_phones)
    contacts_from_db = db.get_contact_list()
    assert (sorted(map(clear, contacts_from_db), key=Contact.id_or_max) ==
            sorted(contacts_from_home_page, key=Contact.id_or_max))