from contact import Contact


class Contacts:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        new_contact = Contact()
        self.contacts.append(new_contact.contact_)

    def delete_contact(self, contact_name):
        initial_length = len(self.contacts)
        for contact in self.contacts:
            if contact['name'] == contact_name:
                self.contacts.remove(contact)
                break
        if len(self.contacts)<initial_length:
            pass
        else:
            print(contact_name, 'does not exist')

    def search_contact(self, contact_name):
        contact_found = False
        for contact in self.contacts:
            if contact['name']==contact_name:
                print(contact)
                contact_found = True
                break
        if not contact_found:
            print(contact_name, 'not found')

    def get_contacts(self):
        return self.contacts
