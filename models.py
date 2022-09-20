
class Passman:
    """ Password manager class for managing & saving password"""

    def __init__(self, username, email, website, password):
        self.username = username
        self.email = email
        self.website = website
        self.password = password

    def __repr__(self):
        return "Passman('{}', '{}', {}, {})".format(self.username, self.email, self.website, self.password)



