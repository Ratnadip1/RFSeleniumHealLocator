from robot.output.logger import Logger
from ..utilities.Decorators import log_write


class HealLog(Logger):

    def __init__(self):
        super()

    @log_write
    def info(self, msg):
        super().info(msg)
        print(msg)

    @log_write
    def error(self, msg):
        super().error(msg)

    pass
