import random
import smtplib
from datetime import datetime as dt
import pandas

today = (dt.now().month, dt.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}
######------------------Check birthdays--------------------------######
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_string = letter.read()
        letter_string = letter_string.replace("[NAME]", birthday_person["name"])
        print(letter_string)

######------------------Send email--------------------------######
    my_email = "ruhlmirkojoel@gmail.com"
    password = "kxitbenunmwuivcb"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mirkoruhl@yahoo.com",
            msg=f"Subject:Birthday\n\n{letter_string}"
        )
