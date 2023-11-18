import csv, sqlite3

def RefreshFoodTypeTable():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS FoodType')
    
    cur.execute('CREATE TABLE IF NOT EXISTS FoodType (Type TEXT NOT NULL, Unit TEXT NOT NULL, PRIMARY KEY("Type"));')
    
    with open("src/FoodTypes.csv", 'r') as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            try:
                cur.execute('INSERT INTO FoodType VALUES (?, ?)', (row[0], row[1]))
            except:
                pass

    con.commit()
    con.close()

def GetAllTypesWithUnit():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM FoodType')
    result = cur.fetchall()

    con.close()
    return result

print(GetAllTypesWithUnit())

    