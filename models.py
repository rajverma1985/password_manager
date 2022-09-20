
class Passman:
    """A sample Employee class"""

    def __init__(self, username, email, website, password):
        self.username = username
        self.email = email
        self.website = website
        self.password = password

    def __repr__(self):
        return "Passman('{}', '{}', {}, {})".format(self.username, self.email, self.website, self.password)



