from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app, db):

    groups = db.get_group_list()
    contacts = db.get_contact_list()

    if len(groups) == 0:
        app.group.create ( Group ( name="group_to_delete" ) )

    if len(contacts) == 0:
        app.contact.contact(Contact(firstname="contact_to_delete"))

    contacts_in_groups = orm.contacts_in_groups()

    if len(contacts_in_groups) == 0:
        app.contact.add_contact_to_group ()
        contacts_in_groups = orm.contacts_in_groups ()


    contacts_in_groups = contacts_in_groups[0]
    group_in_contact = orm.get_groups_of_contact(contacts_in_groups)[0]

    app.contact.remove_contact_from_group(contacts_in_groups, group_in_contact)
    new_contacts_in_groups = orm.contacts_in_groups()

    # проверяем, что список свободных контактов изменился на 1
    assert len(contacts_in_groups)  == len(new_contacts_in_groups)+1

