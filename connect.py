import pyodbc


class Sql():
    print("\33[1m\33[34m\t\t\t\t\t********  will come quiz game **********\33[0m\n\n ")

    def data_int(self):

        user = int(input("\33[1m\33[31m\t\tChoose Your Interests Quiz\33[0m\t\t\t"
                         "\33[1m\33[32m\t\t1,History for Israel\33[0m\t"
                         "\33[1m\33[33m\t\t2,Sport Questions\33[0m"))
        if user == 1:

            join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                                  "Server};SERVER=LAPTOP-0DLOL877;"
                                  "DATABASE=TIRVIA;"
                                  "Trusted_connection=yes")
            X = 'SELECT Question, choose1, choose2, choose3, choose4, Answer FROM dbo.Generals'
            cursor = join.cursor()
            cursor.execute(X)
            score = 0
            for i in cursor:
                print(i[0])

                print("1", i[1], "\n", "2", i[2], "\n", "3", i[3], "\n", "4", i[4])
                answer = input("Enter your answer")
                if answer == i[5]:
                    score += 1
                    input("correct  answer")
                else:
                    input("Incorrect  answer")
            print("your final score is", score, "/8")
        elif user == 2:

            join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                                  "Server};SERVER=LAPTOP-0DLOL877;"
                                  "DATABASE=TIRVIA;"
                                  "Trusted_connection=yes")
            X = 'SELECT Question, option1, option2, Answer FROM dbo.Sports'
            cursor = join.cursor()
            cursor.execute(X)
            score = 0
            for i in cursor:
                print(i[0])

                print("1", i[1], "\n", "2", i[2])
                Answer = input("Enter your answer")
                if Answer == i[3]:
                    score += 1
                    input("correct  answer")
                else:
                    input("Incorrect  answer")
            print("your final score is", score, "/8")







