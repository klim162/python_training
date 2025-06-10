from model.contact import Contact
from model.group import Group
import random


def test_dell_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="test_first"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    if contact not in orm.get_contacts_in_group(group):
        app.contact.add_contact_to_group(contact.id, group.id)
    app.contact.del_contact_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)

