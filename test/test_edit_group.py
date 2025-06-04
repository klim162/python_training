from model.group import Group
import random


def test_edit_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name="name", header="header", footer="footer", id=group_random.id)
    app.group.edit_group_by_id(group, group_random.id)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_random)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
