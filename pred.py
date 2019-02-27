from gnb import Gnb

age = input("\nAge \"<=30, 31-40 or >40\": ")
income = input("Income \"high, medium or low\": ")
student = input("Student \"yes or no\": ")
cred_rating = input("Credit_rating \"fair or excellent\": ")

obj = Gnb().gnb_algo(age, income, student, cred_rating)