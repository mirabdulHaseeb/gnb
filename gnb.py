import pandas as pd 

data = pd.read_csv('computer_dataset.csv')

#print(data.head())
obs = data.values
total_obs = len(data.values)


age = input("\nAge \"<=30, 31-40 or >40\": ")
income = input("Income \"high, medium or low\": ")
student = input("Student \"yes or no\": ")
cred_rating = input("Credit_rating \"fair or excellent\": ")

class_label = []

age_yes = []
age_no = []

income_yes = []
income_no = []

student_yes = []
student_no = []

cred_rating_yes = []
cred_rating_no = []

for ob in obs:
    if ob[-1] == "yes":
        class_label.append(ob[-1])

    if ob[0] == age and ob[-1] == "yes":
        age_yes.append(ob[0])
    if ob[0] == age and ob[-1] == "no":
        age_no.append(ob[0])

    if ob[1] == income and ob[-1] == "yes":
        income_yes.append(ob[1])
    if ob[1] == income and ob[-1] == "no":
        income_no.append(ob[1])

    if ob[2] == student and ob[-1] == "yes":
        student_yes.append(ob[2])
    if ob[2] == student and ob[-1] == "no":
        student_no.append(ob[2])

    if ob[3] == cred_rating and ob[-1] == "yes":
        cred_rating_yes.append(ob[3])
    if ob[3] == cred_rating and ob[-1] == "no":
        cred_rating_no.append(ob[3])


total_yes = len(class_label)
total_no = total_obs - total_yes

#P(Ci)
pc_yes = total_yes/total_obs
pc_no = total_no/total_obs

len_age_yes = len(age_yes)/total_yes
len_age_no = len(age_no)/total_no

len_income_yes = len(income_yes)/total_yes
len_income_no = len(income_no)/total_no

len_student_yes = len(student_yes)/total_yes
len_student_no = len(student_no)/total_no

len_cred_rating_yes = len(cred_rating_yes)/total_yes
len_cred_rating_no = len(cred_rating_no)/total_no

#P(X|Ci)
pxci_yes = len_age_yes * len_income_yes * len_student_yes * len_cred_rating_yes
pxci_no = len_age_no * len_income_no * len_student_no * len_cred_rating_no

#P(X|Ci)*P(Ci)
p_yes = pxci_yes * pc_yes
p_no = pxci_no * pc_no

print("Yes: ",str(p_yes) + "\nNo: ",str(p_no))

if p_yes > p_no:
    print("Prediction: Buys")
elif p_yes < p_no:
    print("Prediction: Won't Buy")
else:
    print("Something went terribly wrong :(\n")
        