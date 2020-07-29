from model.group import Contact
import  re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith ( "/" ) and len ( wd.find_elements_by_name ( "firstnam" ) ) > 0):
            wd.find_element_by_link_text ( "home" ).click ()

    contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name ( "firstname" ).click ()
        wd.find_element_by_name ( "firstname" ).clear ()
        wd.find_element_by_name ( "firstname" ).send_keys ( contact.firstname )
        wd.find_element_by_name ( "middlename" ).click ()
        wd.find_element_by_name ( "middlename" ).clear ()
        wd.find_element_by_name ( "middlename" ).send_keys ( contact.middlename )
        wd.find_element_by_name ( "lastname" ).click ()
        wd.find_element_by_name ( "lastname" ).clear ()
        wd.find_element_by_name ( "lastname" ).send_keys ( contact.lastname )
        wd.find_element_by_name ( "nickname" ).click ()
        wd.find_element_by_name ( "nickname" ).clear ()
        wd.find_element_by_name ( "nickname" ).send_keys ( contact.nickname )
        wd.find_element_by_name ( "title" ).click ()
        wd.find_element_by_name ( "title" ).clear ()
        wd.find_element_by_name ( "title" ).send_keys ( contact.titile )
        wd.find_element_by_name ( "company" ).click ()
        wd.find_element_by_name ( "company" ).clear ()
        wd.find_element_by_name ( "company" ).send_keys ( contact.compony )
        wd.find_element_by_name ( "address" ).click ()
        wd.find_element_by_name ( "address" ).clear ()
        wd.find_element_by_name ( "address" ).send_keys ( contact.address )
        wd.find_element_by_name ( "home" ).click ()
        wd.find_element_by_name ( "home" ).clear ()
        wd.find_element_by_name ( "home" ).send_keys ( contact.home )
        wd.find_element_by_name ( "mobile" ).click ()
        wd.find_element_by_name ( "mobile" ).clear ()
        wd.find_element_by_name ( "mobile" ).send_keys ( contact.mobile )
        wd.find_element_by_name ( "work" ).click ()
        wd.find_element_by_name ( "work" ).clear ()
        wd.find_element_by_name ( "work" ).send_keys ( contact.work )
        wd.find_element_by_name ( "fax" ).click ()
        wd.find_element_by_name ( "fax" ).clear ()
        wd.find_element_by_name ( "fax" ).send_keys ( contact.fax )
        wd.find_element_by_name ( "email" ).click ()
        wd.find_element_by_name ( "email" ).clear ()
        wd.find_element_by_name ( "email" ).send_keys ( contact.email )
        wd.find_element_by_name ( "email2" ).click ()
        wd.find_element_by_name ( "email2" ).clear ()
        wd.find_element_by_name ( "email2" ).send_keys ( contact.email2 )
        wd.find_element_by_name ( "email3" ).click ()
        wd.find_element_by_name ( "email3" ).clear ()
        wd.find_element_by_name ( "email3" ).send_keys ( contact.email3 )
        wd.find_element_by_name ( "homepage" ).click ()
        wd.find_element_by_name ( "homepage" ).clear ()
        wd.find_element_by_name ( "homepage" ).send_keys ( contact.homepage )
        wd.find_element_by_name ( "bday" ).click ()
        Select ( wd.find_element_by_name ( "bday" ) ).select_by_visible_text ( "14" )
        wd.find_element_by_name ( "bday" ).click ()
        wd.find_element_by_name ( "bmonth" ).click ()
        Select ( wd.find_element_by_name ( "bmonth" ) ).select_by_visible_text ( "August" )
        wd.find_element_by_name ( "bmonth" ).click ()
        wd.find_element_by_name ( "byear" ).click ()
        wd.find_element_by_name ( "byear" ).clear ()
        wd.find_element_by_name ( "byear" ).send_keys ( "1955" )
        wd.find_element_by_name ( "aday" ).click ()
        Select ( wd.find_element_by_name ( "aday" ) ).select_by_visible_text ( "18" )
        wd.find_element_by_name ( "aday" ).click ()
        wd.find_element_by_name ( "amonth" ).click ()
        Select ( wd.find_element_by_name ( "amonth" ) ).select_by_visible_text ( "October" )
        wd.find_element_by_name ( "amonth" ).click ()
        wd.find_element_by_name ( "ayear" ).click ()
        wd.find_element_by_name ( "ayear" ).clear ()
        wd.find_element_by_name ( "ayear" ).send_keys ( "2012" )
        wd.find_element_by_name ( "address2" ).click ()
        wd.find_element_by_name ( "address2" ).clear ()
        wd.find_element_by_name ( "address2" ).send_keys ( contact.address2 )
        wd.find_element_by_name ( "phone2" ).click ()
        wd.find_element_by_name ( "phone2" ).clear ()
        wd.find_element_by_name ( "phone2" ).send_keys ( contact.phone2 )
        wd.find_element_by_name ( "notes" ).click ()
        wd.find_element_by_name ( "notes" ).clear ()
        wd.find_element_by_name ( "notes" ).send_keys ( contact.notes )
        self.contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page ()
        # init contact creation
        wd.find_element_by_link_text ( "add new" ).click ()
        self.fill_contact_form ( contact )
        # submit group creation
        wd.find_element_by_xpath ( "(//input[@name='submit'])[2]" ).click ()
        self.retern_to_home_page ( )
        self.contact_cache = None

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name ( "selected[]" ).click ()
        self.contact_cache = None

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_name ( "selected[]" )[index].click ()
        self.contact_cache = None

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_home_page ()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath ( "//input[@value='Delete']" ).click ()
        wd.switch_to_alert ().accept ()
        self.retern_to_home_page ( )
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index ( 0 )

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page ()
        self.select_contact_by_index ( index )
        wd.find_elements_by_xpath ( "//img[@alt='Edit']" )[index].click ()
        self.fill_contact_form ( new_contact_data )
        wd.find_element_by_xpath ( "(//input[@name='update'])" ).click ()
        self.retern_to_home_page ()
        self.contact_cache = None

    def retern_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text ( "home page" ).click ()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name ( "selected[]" ))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page ()
            self.contact_cache = []
            for element in wd.find_elements_by_name ( 'entry' ):
                cells = element.find_elements_by_tag_name ( "td" )
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = element.find_element_by_name ( "selected[]" ).get_attribute ( "value" )
                        self.contact_cache.append ( Contact ( firstname=firstname, lastname=lastname, id=id,
                                            all_phones_from_home_page = all_phones,address=address, email=all_emails ) )
        return list ( self.contact_cache )


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page ()
        self.select_contact_by_index ( index )
        wd.find_elements_by_xpath ( "//img[@alt='Edit']" )[index].click ()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page ()
        self.select_contact_by_index ( index )
        wd.find_elements_by_xpath ( "//img[@alt='Details']" )[index].click ()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index ( index )
        firstname = wd.find_element_by_name ( "firstname" ).get_attribute ( "value" )
        lastname = wd.find_element_by_name ( "lastname" ).get_attribute ( "value" )
        id = wd.find_element_by_name ( "id" ).get_attribute ( "value" )
        homephone = wd.find_element_by_name ( "home" ).get_attribute ( "value" )
        mobilephone = wd.find_element_by_name ( "mobile" ).get_attribute ( "value" )
        workphone = wd.find_element_by_name ( "work" ).get_attribute ( "value" )
        secondaryphone = wd.find_element_by_name ( "phone2" ).get_attribute ( "value" )
        return Contact ( firstname=firstname, lastname=lastname, id=id,homephone =homephone,mobilephone=mobilephone,
                         workphone=workphone,secondaryphone=secondaryphone)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        workphone = re.search ( "W: (.*)", text ).group ( 1 )
        mobilephone = re.search ( "M: (.*)", text ).group ( 1 )
        secondaryphone = re.search ( "P: (.*)", text ).group ( 1 )
        return Contact (homephone=homephone, mobilephone=mobilephone,
                         workphone=workphone, secondaryphone=secondaryphone)


