from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = ""))

    app.group.edit_group()
