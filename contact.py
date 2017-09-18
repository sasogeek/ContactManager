class Contact:
    def __init__(self):
        self.contact_ = {}
        self.name = input('Name: ')
        self.phone_number = input('Phone Number: ')
        self.email = input('Email: ')
        self.website = input('Website: ')
        self.birthday = input('Birthday: ')
        self.linked_in = input('Linked In: ')
        # self.picture = input('Picture: ')
        self.contact_ = {'name': self.name,
                         'phone number': self.phone_number,
                         'email': self.email,
                         'website': self.website,
                         'birthday': self.birthday,
                         'linkedin': self.linked_in}
