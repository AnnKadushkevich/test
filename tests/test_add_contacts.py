# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contacts.get_contact_list ()
    contact =  Contact( firstname ='anna', middlename =' alex',
                                 lastname = ' koz', nickname = ' an ', title = 'no', company = 'no',
                                 address = 'min', home='none', mobile = ' 35661', work = 'not',
                                 fax = ' 64131ftbr', email = ' uhui46@iby', email2='iuhi@jiyg', email3 = 'gugu@545trb',
                                 homepage = 'yuuh ', address2='ugy', phone2 = 'ugu', notes = 'ukhi' )
    app.contact.create( contact )
    assert len ( old_contact + 1 ) == app.contact.count()
    new_contact = app.contacts.get_contact_list ()
    old_contact.append ( contact )
    assert sorted ( old_contact, key=Contact.id_or_max ) == sorted ( new_contact, key=Contact.id_or_max )


