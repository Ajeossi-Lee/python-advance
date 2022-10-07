import os
import sys
import datetime


def auth(func):
    """ Permission validation decorator """
    endline = datetime.datetime(2022, 9, 20)

    def wrapper(*args, **kwargs):
        if datetime.datetime.now().__gt__(endline):
            raise ExpireError('sorry, Program is due, goodbye')
        return None
    return wrapper


class ExpireError(Exception):
    pass


class MyTools:

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])

    @auth
    def run(self):
        pass

    def main_help_text(self, commands_only=False):
        pass

    def fetch_command(self, subcommand):
        pass

    @property
    def fields(self):
        """
        Return a list of string names corresponding to each of the Fields
        available in this Layer.
        """
        pass

if __name__ == '__main__':
    obj = MyTools()
    obj.run()
