import datetime as dt
import random
import pandas as pd
import smtplib

username="sun.pythonil@gmail.com"
password="pczsddmnrbnumcvp"
today=dt.datetime.now()
month=today.month
day=today.day
birth_df=pd.read_csv("birthdays.csv")
birth_list=birth_df.to_dict(orient="records")
letters=["letter_1.txt","letter_2.txt","letter_3.txt"]

for i in birth_list:
    if i["day"] == day and i["month"]==month:
        file=random.choice(letters)
        with open(file) as file:
            file_data=file.read()
            message=file_data.replace("[NAME]",i["name"])
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(username,password)
                connection.sendmail(from_addr=username,to_addrs=i["email"],msg=f"Subject: Happy Birthday {i["name"]}\n\n{message}")








