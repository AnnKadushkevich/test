from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
from fixture import orm

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
     groups = db.get_group_list()
     contacts = db.get_contact_list()

     if len(groups) == 0:
         app.group.create(Group(name="test"))

     if len(contacts) == 0:
         app.contact.contact(Contact(firstname="test"))

     contacts_without_groups = orm.contacts_without_groups()
     groups_without_contacts = orm.groups_without_contacts()

     if len(groups_without_contacts) == 0:
         app.group.create(Group(name="test"))
         groups_without_contacts = orm.groups_without_contacts ()

     if len(contacts_without_groups) == 0:
         app.contact.contact(Contact(firstname="test"))
         contacts_without_groups = orm.contacts_without_groups ()
         
     # добавление первого свободного контакта в первую свободную группу
     app.contact.add_contact_to_group(contacts_without_groups[0], groups_without_contacts[0])

     new_contacts_without_groups = orm.contacts_without_groups()
     new_groups_without_contacts = orm.groups_without_contacts()

     # проверяем, что список свободных групп и контактов изменился на 1
     assert len(contacts_without_groups) == len(new_contacts_without_groups) + 1
     assert len(groups_without_contacts) == len(new_groups_without_contacts) + 1
