import os

# Decorators.py is a module where all utility decorators is to be listed.

# "log_write" is a decorator used for logging that writes all the entries in logger
# into a log file at the current working directory.


def log_write(f):
    def wrap(*args):
        with open(os.getcwd() + os.sep + "log.log", "a") as logFile:
            logFile.write(args[1])
        pass

    return wrap
