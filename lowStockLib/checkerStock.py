import mysql.connector

class StockChecker:
    def __init__(self, db_name, host, user, password, table_name, threshold, user_id):
        self.db_name = db_name
        self.host = host
        self.user = user
        self.password = password
        self.table_name = table_name
        self.threshold = threshold
        self.user_id = user_id

    def connect_to_database(self):
        """Establishes a connection to the database."""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            return connection
        except mysql.connector.Error as err:
            raise Exception(f"Database connection failed: {err}")

    def execute_query(self, query, params):
        """Executes a custom query with parameters."""
        connection = self.connect_to_database()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
        finally:
            connection.close()
        return results
