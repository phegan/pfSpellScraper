import MySQLdb

class ConnectionManager(object):
    def get_connection(self):
        connection = MySQLdb.connect(host="127.0.0.1",
                               user="pfSpell",
                               passwd="scrapethatspell",
                               db="pfSpells")

        connection.autocommit(True)
        return connection