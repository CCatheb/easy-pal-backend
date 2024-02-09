import unittest

from unittest import mock
from unittest.mock import patch
from sql.sql_client import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        #self.database_manager = DatabaseManager(config_file="tests/conf/config.ini")
        pass

    def test_execute_good_query(self):
        """Test docstring
        """
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()