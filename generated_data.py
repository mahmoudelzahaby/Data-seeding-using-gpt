import mysql.connector
from faker import Faker
import random

mydb = mysql.connector.connect(
  host="svc-24b7b016-b727-41b2-b209-cd3ac3cc68f3-dml.aws-virginia-5.svc.singlestore.com",
  user="admin",
  password="P@ssw0rd",
  database="stup"
)

mycursor = mydb.cursor()

fake = Faker()

sql_create_employes2 = """CREATE TABLE employes2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(255),
    date_of_birth VARCHAR(255),
    gender VARCHAR(255)
)""" 

sql_create_customeres2 = """CREATE TABLE customeres2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(255),
    date_of_birth VARCHAR(255),
    gender VARCHAR(255),
    membership_status VARCHAR(255)
)""" 

mycursor.execute(sql_create_employes2)
mycursor.execute(sql_create_customeres2)

# generate 1000 data items
for i in range(1000):
    # generate employee data
    name = fake.name()
    age = random.randint(18, 60)
    email = fake.email()
    address = fake.address()
    phone = fake.phone_number()
    date_of_birth = fake.date()
    gender = random.choice(["Male", "Female", "Other"])

    sql_employes2 = "INSERT INTO employes2 (name, age, email, address, phone, date_of_birth, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val_employes2 = (name, age, email, address, phone, date_of_birth, gender)
    mycursor.execute(sql_employes2, val_employes2)

    # generate customer data
    name = fake.name()
    email = fake.email()
    address = fake.address()
    phone = fake.phone_number()
    date_of_birth = fake.date()
    gender = random.choice(["Male", "Female", "Other"])
    membership_status = random.choice(["Active", "Inactive"])

    sql_customeres2 = "INSERT INTO customeres2 (name, email, address, phone, date_of_birth, gender, membership_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val_customeres2 = (name, email, address, phone, date_of_birth, gender, membership_status)
    mycursor.execute(sql_customeres2, val_customeres2)

mydb.commit()