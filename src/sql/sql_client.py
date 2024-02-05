from psycopg2 import pool
import configparser

import psycopg2

from pal_utils.logger_factory import CustomLogger


class DatabaseManager:
    """ This class is a dabase manager, used to connect and execute queries on the database specified in the config file."""

    def __init__(self, config_file: str = "conf/config.ini", max_connections: int = 5) -> None:

        self.__logger = CustomLogger.get_logger("DBMAN")
        
        # Get the config informations from the config.ini file
        try:
            self.__conf = configparser.ConfigParser()
            self.__conf.read(config_file)
            self.__logger.debug(f"Configuration sections from '{config_file}': {self.__conf.sections()}")
        except Exception as err:
            self.__logger.error(f"Could not read config file '{config_file}': {err}")

        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, max_connections,
            user = self.__conf.get('sql', 'user'),
            host = self.__conf.get('sql', 'host'),
            port = self.__conf.get('sql', 'port'),
            database = self.__conf.get('sql', 'database')
        )

    def execute_query(self, sql_query: str) :

        connection = self.connection_pool.getconn()
        cursor = connection.cursor()

        try:
            self.__logger.debug(f"SQL Query is: {sql_query}")
            cursor.execute(sql_query)
            result = cursor.fetchall()
            connection.commit()
            self.__logger.info("SQL Query executed")
        except Exception as err:
            self.__logger.warning(f"Tried to execute SQL query '{sql_query}' but it failed: {err}")
            connection.rollback()
        finally:
            cursor.close()
            self.connection_pool.putconn(connection)
        return result