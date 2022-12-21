import pyodbc


class datas():

    def data_int(self):
        join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                              "Server};SERVER=LAPTOP-0DLOL877;"
                              "DATABASE=TIRVIA;"
                              "Trusted_connection=yes")
        cursor = join.cursor()

        id = int(input("\33[1m\33[34m\t\t Enter your id number\33[0m"))
        fname = input("\33[1m\33[34m\t\t Enter your firstname\33[0m ")
        score = input("\33[34m\t\tEnter your result\33[0m")
        cursor.execute("INSERT INTO Datas (id, fname, score ) VALUES (?, ?, ?)", (id, fname, score))
        join.commit()
