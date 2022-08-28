import datetime as dt
import random
import pandas
import smtplib

MY_MAIL = "demo.234@gmail.com"
PASSWORD = "Password"

now = dt.datetime.now()
TODAY_DAY = now.today().day
TODAY_MONTH = now.today().month
today_tuple = (TODAY_DAY, TODAY_MONTH)


birthday_data = pandas.read_csv("./birthdays.csv")

for (index, row) in birthday_data.iterrows():
    if row.month == now.month and row.day == now.day:
        filepath = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(filepath) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=row["email"], msg=f"Subject:Happy BirthDay!!\n\n{content}")
