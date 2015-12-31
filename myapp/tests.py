import unittest
from test.support import EnvironmentVarGuard
from environ import settings

"""
Unit tests
"""


class TestSettings(unittest.TestCase):

    def test_my_custom_param(self):
        self.assertEqual('Hello World!', settings('MY_CUSTOM_PARAM'))

if __name__ == '__main__':
    env = EnvironmentVarGuard()
    env.set('SETTINGS_MODULE', 'myapp.settings.unittest')
    with env:
        unittest.main()
