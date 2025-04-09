name=input("name:")
age=input("age:")
last_admission=input("last aadmission is:")
medical_history=input("medical history is:")
class Patient():
   
    def __init__(self, name, age, last_admission, medical_history):
        
        self.name = name
        self.age = age
        self.last_admission = last_admission
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"patient: {self.name}, age: {self.age}, last_admission: {self.last_admission}, medical_history: {self.medical_history}")
 #Example
patient0=Patient(name="Li",age=18,last_admission="6 months ago",medical_history="headache")
patient0.print_details()
        
 
       
        
