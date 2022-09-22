
class Passman:
    """ Password manager class for managing & saving password"""

    def __init__(self, email, website, password):
        self.email = email
        self.website = website
        self.password = password

    def __repr__(self):
        return "Passman('{}', '{}', {}, {})".format(self.email, self.website, self.password)



