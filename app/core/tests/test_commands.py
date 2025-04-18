"""
Test custom django management commands.
"""

from psycopg2 import OperationalError as Psycopg2Error

from unittest.mock import patch


from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test commands """

    def test_wait_for_db(self, patched_check):
        """Test waiting for database if database is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_watit_for_db_delay(self, patched_sleep, patched_check):
        """ Test is database is getting readdy"""

        patched_check.side_effect = [Psycopg2Error] * 2 +  [OperationalError] * 3 +[True]

        call_command('wait_for_db')

        self.assertEquals(patched_check.call_count, 6)

        patched_check.assert_called_with(databases=['default'])