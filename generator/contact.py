from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "_" + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_month():
    month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    return random.choice(month)

def random_day():
    return str(random.randint(1,31))

def random_year():
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range (random.randrange(4))])


testdata = [Contact(firstname=random_string("firstname", 10),
                    middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10),
                    title=random_string("title", 10),
                    company=random_string("company", 10),
                    address=random_string("address", 10),
                    phonehome=random_string("phonehome", 10),
                    phonemobile=random_string("phonemobile", 10),
                    phonework=random_string("phonework", 10),
                    phonefax=random_string("phonefax", 10),
                    email=random_string("email", 10),
                    email2=random_string("email2", 10),
                    email3=random_string("email3", 10),
                    homepage=random_string("homepage", 10),
                    bday=random_day(), bmonth=random_month(), byear=random_year(),
                    aday=random_day(), amonth=random_month(), ayear=random_year())
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    json.dump(testdata, f, default=lambda x: x.__dict__, indent=2)
