from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=''))

    app.contact.edit_contact()
