"""CUGB Mirror Bot CLI

Usage:
  mirror_bot add <mirrorconfig>
  mirror_bot delete <mirrorname>
  mirror_bot list
  mirror_bot start <mirrorname>
  mirror_bot status <mirrorname>
  mirror_bot stop <mirrorname>

Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""

from docopt import docopt
import mirror_bot
import mirror_bot.utils as utils
import mirror_bot.config_parse as config_parse


def add(mirrorconfig):
    configdata = utils.read("_config.yml")
    configdata['mirror'].append(config_parse.parse(mirrorconfig))
    utils.write("_config.yml", configdata)


def delete(mirrorname):
    configdata = utils.read("_config.yml")
    configdata['mirror'].remove(config_parse.parse(mirrorname))
    utils.write("_config.yml", configdata)


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
