import re
from model.contact import Contact

def test_contact_filds_on_home_page(app, db):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="ewfweqf", middlename="erferfg", lastname="wfqwvdv",
                    nickname="wfefr", title="wfewqc", company="cwef", address="wfeqrr",
                    phonehome="2343", phonemobile="5432", phonework="34345", phonefax="3453",
                    email="rr@tt.oo", email2="dsfd@err.yy", email3="dvdfwe@tt.yy", homepage="fewfrew",
                    bday="28", bmonth="October", byear="4000", aday="28", amonth="October", ayear="1000"))
    def clear1(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address, all_mail=merge_email_on_home_page(contact),
                       all_phones=merge_phones_like_on_home_page(contact))

    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(map(clear1, db.get_contact_list()), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_db[i].lastname == contacts_from_home_page[i].lastname
        assert contacts_from_db[i].firstname == contacts_from_home_page[i].firstname
        assert contacts_from_db[i].address == contacts_from_home_page[i].address
        assert contacts_from_db[i].all_mail == contacts_from_home_page[i].all_mail_from_homepage
        assert contacts_from_db[i].all_phones == contacts_from_home_page[i].all_phones_from_homepage

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(
        lambda x: x != "",
        map(lambda x: clear(x),
            filter(lambda x: x is not None,
                   [contact.phonehome, contact.phonemobile, contact.phonework]))))

def merge_email_on_home_page(contact):
    return "\n".join(filter(
        lambda x: x != "",
        map(lambda x: x.strip(),
            filter(lambda x: x is not None,
                   [contact.email, contact.email2, contact.email3]))))