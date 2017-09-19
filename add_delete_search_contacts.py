from contacts import Contacts
add_delete_search_contact_ = True
phone_book = Contacts()


while add_delete_search_contact_:
    check = input('Add/Delete/Search/Quit a contact? a/d/s/q  ')
    if check == 'a':
        contact = phone_book.add_contact()
        add_delete_search_contact_ = True
    elif check == 'd':
        contact = input('Name of contact to delete: ')
        phone_book.delete_contact(contact)
        add_delete_search_contact_ = True
    elif check == 's':
        contact = input('Name of contact to search: ')
        phone_book.search_contact(contact)
        add_delete_search_contact_ = True
    elif check == 'q':
        break

# for contact in phone_book.get_contacts():
#     print(contact)
