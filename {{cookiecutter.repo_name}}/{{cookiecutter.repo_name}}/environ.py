import os
import importlib

"""
set the settings module
"""


def settings(setting):
    """
    get settings
    """
    mod = importlib.import_module(os.environ.get("SETTINGS_MODULE"))
    return getattr(mod, setting.upper())


def set_settings_module():
    if not os.environ.get("SETTINGS_MODULE"):
        os.environ.setdefault("SETTINGS_MODULE",
                              "{{cookiecutter.repo_name}}.settings.{{ '{{' }} goal {{ '}}' }}")
