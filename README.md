# BMI-Calculator
With this code , you can calc your Body mass index then show the information about  your bmi and the last insert info into data base
| method name | Function | argument(s) |
| ----------  | -------- | ----------- | 
| __init__    | initial Func | name , last name ,  weight , heigth |
| calc_bmi | Calc and return your bmi with bmi Formula (kg/m**2) | self |
| Status_bmi | A state of your health according to the obtained body mass index | self | 
| insert_database | insert your name , lastname , weight , height , bmi , and bmi analysis | self |
| Show_date_base | display the data base  |self , last_name = None |
| Delete_DataBase | if lastname = None --> Delete all item else : delete orresponding row | self , last_name |
| quit_script | go out from script | self |
| run_required_methods | run the calc_bmi , __init__ , Status_bmi , insert_database | self | 

You Should install 'tabulate' package with this command:
` pip install tabulate `

Used packages : 
sqlite3 - 
os - 
tabulate 
