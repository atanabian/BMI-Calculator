import sqlite3
from os import remove , system
import tabulate

class BMI_Calc:

    def __init__(self, name, lname, weight, height):

        self.name = name
        self.lname = lname
        self.weight = weight
        self.height = height

    def calc_bmi(self):
        "Calc and return your bmi"
        # Convert height cm to m
        self.height_m = self.height / 100
        self.bmi = self.weight / (self.height_m ** 2)

        return round(self.bmi, 1)

    def Status_bmi(self):
        "analysis BMI"
        if self.bmi < 18.5:
            msg = 'You must have weight, so maybe you need to gain some weight.\nWe recommend that you seek help from your doctor or nutritionist.'
            self.database_msg = 'Underweight'
        elif self.bmi > 18.5 and self.bmi < 24.9:
            msg = 'A BMI between 18.5 and 24.9 indicates a somewhat normal BMI and tells you that you are at an appropriate weight for your height.\nBy maintaining a healthy weight, you prevent serious risks to your health.'
            self.database_msg = 'Normal'
        elif self.bmi > 25 and self.bmi < 29.9:
            msg = 'A BMI between 25 and 29.9 tells you that you are slightly overweight and need to lose some weight.\nYou can consult your doctor to lose weight.'
            self.database_msg = 'slightly overweight'
        elif self.bmi > 30:
            msg = "A BMI above 30 warns you that you are overweight. If you don't lose weight, your health will definitely be at risk. Be sure to talk to your doctor or nutritionist and start dieting."
            self.database_msg = 'overweight'
        return msg

    def insert_database(self):

        self.conn = sqlite3.connect("bmi.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bmi (
            name TEXT , 
            lname TEXT , 
            weight REAL , 
            height REAL ,
            BMI REAL , 
            status TEXT
        )""")

        self.cursor.execute(
            """
            INSERT INTO bmi VALUES (:name , :lname , :weight , :height , :BMI , :status)
            """, {'name': self.name, 'lname': self.lname, 'weight': self.weight,
                  'height': self.height, 'BMI': self.bmi, 'status': self.database_msg}
        )

        self.conn.commit()
        self.conn.close()

        print("Values inserted to data bace!")

    def Show_date_base(self, last_name=None):

        # if last namn has value
        self.conn = sqlite3.connect("bmi.db")
        self.cursor = self.conn.cursor()
        
        if last_name != None:

            self.cursor.execute(
                """SELECT * FROM bmi WHERE lname = :lname""", {'lname': last_name})
            return tabulate.tabulate(self.cursor.fetchall())

        elif last_name == None:
            self.cursor.execute("""SELECT * FROM bmi""")
            return tabulate.tabulate(self.cursor.fetchall())

    def Delete_DataBase(self , last_name = None) :
            "Delete Data Base if last name --> None : Delete all database else : delete the lastname's info from data bace"
            
            if last_name == None : 
                input("Enter any thing for delete all table(s) of datebace ...")
                self.conn.close()
                remove('bmi.db')
                print("Database Deleted!")
            
            else : 
                input(f"Enter any thing for delete info of {last_name} in database...")
                self.cursor.execute('DELETE FROM bmi WHERE lname = ?,' , (last_name,))
                self.conn.commit()
                print("Remove Successfully!")


    def quit_script(self) :
        "Press ctrl + z in terminal to go out of cmd"
        system('^Z')
  
    
    
def run_required_methods() :
        print("Welcome To BMI Calculator script enter the values to show bmi and analysis BMI and save info into datebace ")
        
        # Get name , last name ,  weight and height
        name = input("Enter your name:")
        lname = input(f"Dear {name} Enter your last name:")


        try:
            weight = float(input(f"Dear {name} Enter your weight (kg):"))
            height = float(input(f"Dear {name} Enter your height (cm):"))

        except ValueError as Error:
            print(Error)


        # made instance
        user1 = BMI_Calc(name, lname, weight, height)

        # call methods 
        print(f'Your Bmi :', user1.calc_bmi())
        print('\n', user1.Status_bmi(), end='\n')
        user1.insert_database()

# run_required_methods()
