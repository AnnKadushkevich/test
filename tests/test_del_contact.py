
from model.contact import Contact
from random import  randrange

def test_delete_some_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname='test'))
    old_contact = app.contacts.get_contact_list ()
    index = randrange ( len ( old_contact ) )
    app.contacts.delete_contact_by_index(index)
    new_contact = app.contacts.get_contact_list ()
    assert len ( old_contact - 1 ) == len ( new_contact )
    old_contact[index:index+1] = []
    assert old_contact == new_contact
