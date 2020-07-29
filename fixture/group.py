from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name ("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if group_name is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value( "group_name", group.name )
        self.change_field_value ( "group_header", group.header )
        self.change_field_value ( "group_footer", group.footer )


    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init gpoup creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.retern_to_groups_page()
        self.group_cashe = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name ( "selected[]" ).click ()

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name ( "selected[]" )[index].click ()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.retern_to_groups_page ()
        self.group_cashe = None

    def delite_first_group(self):
        self.delite_group_by_index(0)



    def edit_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group ( )
        # editing
        wd.find_element_by_name ( "Edet group" ).click ()
        self.fill_group_form()
        wd.find_element_by_name ( "update" ).click ()
        self.retern_to_groups_page ()


    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.retern_to_groups_page ()
        self.group_cashe = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def retern_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page ()
        return len(wd.find_elements_by_name ( "selected[]" ))

   contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page ()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath ( "//tr[@name='entry']" ):
                text = element.find_elements_by_tag_name ( "td" )
                text_lastname = text[1].text
                text_firstname = text[2].text
                text_address = text[3].text
                all_emails = text[4].text
                all_phones = text[5].text
                id = element.find_element_by_name ( "selected[]" ).get_attribute ( "value" )
                self.contact_cache.append ( Contact ( firstname=text_firstname, lastname=text_lastname, id=id,
                                                      all_phones_from_home_page=all_phones, address=text_address,
                                                      email=all_emails ) )
        return list ( self.contact_cache )
