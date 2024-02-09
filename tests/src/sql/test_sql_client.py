import unittest

from unittest import mock, patch
from sql.sql_client import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.database_manager = DatabaseManager(config_file="tests/conf/config.ini")

    def test_execute_good_query(self):

        input_query = "SELECT @@VERSION"
        expected_response = "Toto"

        result = self.database_manager.execute_query(input_query)

        self.assertEqual(expected_response, result)

if __name__ == "__main__":
    unittest.main()