
"""
HealLocatorException: A customized framework level Exception that is raised and handled based on
framework level logical errors.
"""


class HealLocatorException(Exception):

    # Customized constructor of HealLocator exception.
    def __init__(self, message):
        super(HealLocatorException.__class__)
        self.message = message

    # Representation of HealLocatorException instance on casting to string.
    def __repr__(self):
        return 'HealLocatorException [message: {}]'.format(self.message)
