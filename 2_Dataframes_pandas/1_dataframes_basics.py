import numpy as np
import pandas as pd

# creating dataframe using lists
student_list_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

student_list_dataframe = pd.DataFrame(student_list_data , columns=["iq" , "marks" , "package"])
print(student_list_dataframe)

# creating dataframe using dictionary

student_dict_data = {
    "iq" : [100 , 90 , 120 ,80],
    "marks" : [80 , 70 , 100 , 50],
    "package" : [10 , 7 , 14 ,2]
}

student_dict_dataframe = pd.DataFrame(student_dict_data)
print(student_dict_dataframe)