import sqlite3

class SQLiteDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS crops (id INTEGER PRIMARY KEY, name TEXT, type TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fertilizers (id INTEGER PRIMARY KEY, name TEXT, recommended_for TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS farmers (id INTEGER PRIMARY KEY, name TEXT, farm_size REAL)''')
        self.connection.commit()

    def close(self):
        self.connection.close()


class MongoDBDatabase:
    def __init__(self, uri, db_name):
        from pymongo import MongoClient
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def create_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()


class PostgreSQLDatabase:
    def __init__(self, user, password, host, port, db_name):
        import psycopg2
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS crops (id SERIAL PRIMARY KEY, name VARCHAR(100), type VARCHAR(100))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fertilizers (id SERIAL PRIMARY KEY, name VARCHAR(100), recommended_for VARCHAR(100))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS farmers (id SERIAL PRIMARY KEY, name VARCHAR(100), farm_size REAL)''')
        self.connection.commit()

    def close(self):
        self.connection.close()