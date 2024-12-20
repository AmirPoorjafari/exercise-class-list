class Student:
   
   
   
    def __init__(self, first_name, last_name, age, gender, national_number, student_number,GPA ):
        
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 
 
        self.gender = gender
        self.national_number = national_number
        self.student_number =  student_number
        self.GPA = GPA
    
    

    def get_firsr_name(self):
        return ("The first name: "+ self.first_name)
    

    def get_last_name(self):
        return ("The last name: "+self.last_name) 
    

    def get_age(self):
        return ("The "+self.first_name + 's age is ' + str(self.age))
    
 
    def get_gender(self):
        return ("The "+self.first_name + 's gender is ' + str(self.gender))
    
  
    def get_national_number(self):
        return ("The "+self.first_name + 's national number is ' + str(self.national_number))
  
    
   
    def get_GPA(self):
        return ("The "+self.first_name + 's GPA is ' + str(self.GPA))
    

student_1 = Student('amir', 'poorjafari', 18 , 'Men' , 99211140162022 , 2124003452 , 16.00)
student_2 = Student('mohammad', 'hasani', 25 , 'Men' , 99212240062012 , 2024133458 ,18.00)
student_3 = Student('narges', 'alavi', 30 , 'Women' , 92141140133002 ,'0025086123' , 19.5)
student_4 = Student('ali', 'fatami', 20 , 'Men' , '02121040809016' , '0023143567' , 14.00)
student_5 = Student('maryam', 'Karimi', 19 , 'women' , '02221040507011' , 2104583052 , 17.90)
student_6 = Student('reza', 'tehrani', 27 , 'Men' , 9341040102022 , 3412410345 , 13.06)
student_7 = Student('pooria', 'vali', 29 , 'Men' , '02121150608011' , '0026024567' , 19.00)


print(student_2.get_gender())
print(student_2.get_national_number())
print(student_2.get_age())
print(student_2.get_firsr_name())
print(student_2.get_last_name())
