import unittest

from unittest.mock import patch
from src.sql.sql_client import DatabaseManager

class DatabaseManagerTests(unittest.TestCase):

    @patch('src.sql.sql_client.psycopg2.connect')
    def test_execute_query(self, mock_connect):
        # Créer une instance de DatabaseManager
        db_manager = DatabaseManager("tests/conf/config.ini")

        # Mock de l'objet de connexion et de son curseur
        mock_connection = mock_connect.return_value
        mock_cursor = mock_connection.cursor.return_value

        # Exécuter une requête SQL
        sql_query = "SELECT * FROM example_table;"
        db_manager.execute_query(sql_query)

        # Vérifier que les méthodes appropriées ont été appelées
        mock_connect.assert_called_once()
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(sql_query)
        mock_cursor.fetchall.assert_called_once()
        
if __name__ == "__main__":
    unittest.main()