# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contacts.get_contact_list ()
    contact =  Contact( firstname ='anna', lastname = ' koz', homephone='5431', mobilephone= '4545121',workphone='2415445',
                        secondaryphone='54544' )
    app.contact.create( contact )
    assert len ( old_contact + 1 ) == app.contact.count()
    new_contact = app.contacts.get_contact_list ()
    old_contact.append ( contact )
    assert sorted ( old_contact, key=Contact.id_or_max ) == sorted ( new_contact, key=Contact.id_or_max )


