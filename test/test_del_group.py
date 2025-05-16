from model.group import Group


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    old_groups = app.group.get_grout_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_grout_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
