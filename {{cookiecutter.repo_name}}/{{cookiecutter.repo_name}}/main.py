"""Myapp

Usage:
    main.py

Options:
    -h --help  aide
"""

from log import logger
from docopt import docopt
from environ import set_settings_module, settings


def main():
    logger.info("Start {{cookiecutter.project_name}}")
    docopt(__doc__)
    set_settings_module()
    logger.info("MY_CUSTOM_PARAM: %s" % settings('MY_CUSTOM_PARAM'))

if __name__ == "__main__":
    main()
