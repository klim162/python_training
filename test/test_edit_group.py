from model.group import Group
from random import randrange


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    old_groups = app.group.get_grout_list()
    index = randrange(len(old_groups))
    group = Group(name="name", header="header", footer="footer")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_grout_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    old_groups = app.group.get_grout_list()
    index = randrange(len(old_groups))
    group = Group(name="New name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_grout_list()
    old_groups[index].name = group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test_header"))
    old_groups = app.group.get_grout_list()
    index = randrange(len(old_groups))
    group = Group(header="New header")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_grout_list()
    old_groups[index].header = group.header
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
