import sqlite3
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def connect(self):
        self.__conn = sqlite3.connect('test.db')
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS TEXTOS
            (ID INTEGER PRIMARY KEY,
            TEXTO           TEXT    NOT NULL);''')
    print ("Tabla TEXTOS creada exitosamente");

    def insert(self, text):
        self.__conn.execute("INSERT INTO TEXTOS (TEXTO) VALUES (\""+text+"\")")
        self.__conn.commit()
        
    def query_all(self):
        cursor = self.__conn.execute("SELECT * FROM TEXTOS")
        for row in cursor:
            print ("ID = ", row[0])
            print ("TEXTO = ", row[1],"\n")



bd1 = Database()
bd2 = Database()

if id(bd1) == id(bd2):
    print("IGUALES.")
else:
    print("DISTINTOS.")
bd1.connect()
bd1.insert("holaa")
bd1.query_all()