import pandas as pd
import os

def DataStore(name, number, email, occupation):
    if os.path.isfile("user_data.xlsx"):
        df = pd.read_excel("user_data.xlsx")
        df.loc[len(df)] = [name, number, email, occupation]
        df.to_excel("user_data.xlsx", index = False)
    else:
        df = pd.DataFrame([[name, number, email, occupation]], columns=["Name", "Mobile Number", "Email Address", "Occupation"])
        df.to_excel("user_data.xlsx", index = False)