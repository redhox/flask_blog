import mysql.connector as mysqlpyth
from dotenv import load_dotenv
import os




bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    load_dotenv()
    bdd = mysqlpyth.connect(user = os.getenv('USER_BDD'),password = os.getenv('PASSWORD'),host =os.getenv('HOST'),port = os.getenv('PORT'),database = os.getenv('DATABASE'))
    cursor = bdd.cursor()
    return bdd, cursor

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()



    @classmethod
    def get_element(cls, login,passwd):
        cls.connexion()
        user = cls.collection.find_one({'name': login, 'password': passwd})
        cls.deconnexion()
        return user

    @classmethod
    def get_elements(cls):
        cls.connexion()
        tous = cls.collection.find()
        cls.deconnexion()
        return list(tous)

    @classmethod
    def set_element(cls, login, passwd):
        cls.connexion()
        cls.collection.insert_one({'name': login, 'password': passwd})
        cls.deconnexion()