import pandas as pd 

class Gnb():


    def __init__(self, age, income, student, cred_rating):
        
        self.age = age
        self.income = income
        self.student = student
        self.cred_rating = cred_rating

    def gnb_algo(self):
        self.data = pd.read_csv('computer_dataset.csv')
        
        self.obs = self.data.values
        self.total_obs = len(self.data.values)

        self.class_label = []

        self.age_yes = []
        self.age_no = []

        self.income_yes = []
        self.income_no = []

        self.student_yes = []
        self.student_no = []

        self.cred_rating_yes = []
        self.cred_rating_no = []

        for ob in self.obs:
            if ob[-1] == "yes":
                self.class_label.append(ob[-1])

            if ob[0] == self.age and ob[-1] == "yes":
                self.age_yes.append(ob[0])
            if ob[0] == self.age and ob[-1] == "no":
                self.age_no.append(ob[0])

            if ob[1] == self.income and ob[-1] == "yes":
                self.income_yes.append(ob[1])
            if ob[1] == self.income and ob[-1] == "no":
                self.income_no.append(ob[1])

            if ob[2] == self.student and ob[-1] == "yes":
                self.student_yes.append(ob[2])
            if ob[2] == self.student and ob[-1] == "no":
                self.student_no.append(ob[2])

            if ob[3] == self.cred_rating and ob[-1] == "yes":
                self.cred_rating_yes.append(ob[3])
            if ob[3] == self.cred_rating and ob[-1] == "no":
                self.cred_rating_no.append(ob[3])


        self.total_yes = len(self.class_label)
        self.total_no = self.total_obs - self.total_yes

        #P(Ci)
        self.pc_yes = self.total_yes/self.total_obs
        self.pc_no = self.total_no/self.total_obs

        self.len_age_yes = len(self.age_yes)/self.total_yes
        self.len_age_no = len(self.age_no)/self.total_no

        self.len_income_yes = len(self.income_yes)/self.total_yes
        self.len_income_no = len(self.income_no)/self.total_no

        self.len_student_yes = len(self.student_yes)/self.total_yes
        self.len_student_no = len(self.student_no)/self.total_no

        self.len_cred_rating_yes = len(self.cred_rating_yes)/self.total_yes
        self.len_cred_rating_no = len(self.cred_rating_no)/self.total_no

        #P(X|Ci)
        self.pxci_yes = self.len_age_yes * self.len_income_yes * self.len_student_yes * self.len_cred_rating_yes
        self.pxci_no = self.len_age_no * self.len_income_no * self.len_student_no * self.len_cred_rating_no

        #P(X|Ci)*P(Ci)
        self.p_yes = self.pxci_yes * self.pc_yes
        self.p_no = self.pxci_no * self.pc_no

        print("Yes: ",str(self.p_yes) + "\nNo: ",str(self.p_no))

        if self.p_yes > self.p_no:
            print("Prediction: Buys")
        elif self.p_yes < self.p_no:
            print("Prediction: Does not Buy")
        else:
            print("Something went terribly wrong :(\n")
