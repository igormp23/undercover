from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection
    
    def create_round(self, id_game, num_mr_white, num_civilian, num_undercover):
        # cursor = self.connection.cursor(dictionary=True)
        # sql = "INSERT INTO circulation VALUES(default, %s, %s, 'BORROW')"
        # cursor.execute( sql, (id_user, id_book))
        # self.connection.commit()

    def update_round(self, id_book):
        # cursor = self.connection.cursor(dictionary=True)
        # sql = "SELECT status FROM circulation WHERE id_book = {}".format(id_book)
        # cursor.execute(sql)
        # result = cursor.fetchone()
        # cursor.close()
        # return result

    def delete_round(self, id):
        # cursor = self.connection.cursor(dictionary=True)
        # sql = "SELECT * FROM circulation WHERE id = {}".format(id)
        # cursor.execute(sql)
        # result = cursor.fetchone()
        # cursor.close()
        # return result

    def create_round_detail(self, id, status):
        # cursor = self.connection.cursor(dictionary=True)
        # sql = "UPDATE circulation SET status = %s WHERE id = %s"
        # cursor.execute(sql, (status, id))
        # cursor.close()
        # self.connection.commit()

    def mrwhite_guess(self, id, word1):
        # cursor = self.connection.cursor(dictionary=True)
        # sql = "UPDATE circulation SET status = %s WHERE id = %s"
        # cursor.execute(sql, (status, id))
        # cursor.close()
        # self.connection.commit()


    def close_connection(self):
        self.connection.close()

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="DB_POOL",
                pool_size=10,
                pool_reset_session=True,
                host='localhost',
                database='soa_ceria',
                user='root',
                password=''
            )  
            print ("Success Connecting to MySQL")
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")