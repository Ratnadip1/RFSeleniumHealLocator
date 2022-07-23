import os


def log_write(f):
    def wrap(*args):
        with open(os.getcwd() + os.sep + "log.log", "a") as logFile:
            logFile.write(args[1])
        pass

    return wrap
