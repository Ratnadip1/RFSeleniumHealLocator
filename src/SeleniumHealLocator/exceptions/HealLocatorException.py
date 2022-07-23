
class HealLocatorException(Exception):

    def __init__(self, message):
        super(HealLocatorException.__class__)
        self.message = message

    def __repr__(self):
        return 'HealLocatorException [message: {}]'.format(self.message)
