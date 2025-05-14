from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_grout_list()
    group = Group(name="name", header="header", footer="footer")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    app.group.edit_first_group(group)
    new_groups = app.group.get_grout_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_first_group_name(app):
    old_groups = app.group.get_grout_list()
    group = Group(name="New name")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    app.group.edit_first_group(group)
    new_groups = app.group.get_grout_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0].name = group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_first_group_header(app):
    old_groups = app.group.get_grout_list()
    group = Group(header="New header")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(header="test_header"))
    app.group.edit_first_group(group)
    new_groups = app.group.get_grout_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0].header = group.header
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
