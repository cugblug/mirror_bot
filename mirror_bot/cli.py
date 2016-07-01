"""CUGB Mirror Bot CLI

Usage:
  mirror_bot add <file>
  mirror_bot delete <name>
  mirror_bot list
  mirror_bot start <name>
  mirror_bot status <name>
  mirror_bot stop <name>

Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""

from docopt import docopt
import mirror_bot
import mirror_bot.utils as utils
import mirror_bot.config_parse as config_parse


def add(file):
    configdata = utils.read("_config.yml")
    configdata['mirror'].append(config_parse.parse(file))
    utils.write("_config.yml", configdata)


def delete():
    pass


def list():
    pass


def start(container_name):
    pass


def status(container_name):
    pass


def stop(container_name):
    pass


def main():
    # arguments = docopt(__doc__, version=mirror_bot.version)
    # utils.docker_version_check(mirror_bot.docker_version)
    # print(arguments)
    pass


if __name__ == '__main__':
    main()
