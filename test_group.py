# -*- coding: utf-8 -*-
import unittest
from group import Group
from selenium import webdriver

class TeatAddGroup ( unittest.TestCase ):
    def setUp(self):
        self.wd = webdriver.Firefox ()
        self.wd.implicitly_wait ( 30 )

    def open_home_page(self, wd):
        wd.get ( "http://localhost/addressbook/" )

    def login(self, wd, username, password):
        wd.find_element_by_name ( "user" ).clear ()
        wd.find_element_by_name ( "user" ).send_keys ( username )
        wd.find_element_by_name ( "pass" ).click ()
        wd.find_element_by_name ( "pass" ).clear ()
        wd.find_element_by_name ( "pass" ).send_keys ( password )
        wd.find_element_by_xpath ( "//input[@value='Login']" ).click ()

    def open_home_page(self, wd):
        wd.find_element_by_link_text ( "groups" ).click ()

    def create_group(self, wd, group):
        # init gpoup creation
        wd.find_element_by_name ( "new" ).click ()
        # fill group form
        wd.find_element_by_name ( "group_name" ).click ()
        wd.find_element_by_name ( "group_name" ).clear ()
        wd.find_element_by_name ( "group_name" ).send_keys ( group.name )
        wd.find_element_by_name ( "group_header" ).click ()
        wd.find_element_by_name ( "group_header" ).clear ()
        wd.find_element_by_name ( "group_header" ).send_keys ( group.header )
        wd.find_element_by_name ( "group_footer" ).click ()
        wd.find_element_by_name ( "group_footer" ).clear ()
        wd.find_element_by_name ( "group_footer" ).send_keys ( group.footer )
        # submit group creation
        wd.find_element_by_name ( "submit" ).click ()

    def retern_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page (wd)
        self.login(wd, username="admin", password ="secret" )
        self.open_home_page(wd)
        self.create_group(wd,Group(name="first group", header="hjklouhi", footer = "lhb" ))
        self.retern_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_home_page (wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.retern_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main ()