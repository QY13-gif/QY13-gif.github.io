weight_kg=input("the weight(kg) is:")
strength=input("the strength is:")
weight=int(weight_kg)
def calcualte_paracetamol_dose(weight, strength):
   
    if not 10 <= weight <= 100:
        return "Error, the weight must be between 10 to 100"
    if strength not in ["120", "250"]:
        return "Error, the strength must be '120' or '250'"
    dose_mg=weight*15
    strength_num=float(strength)
    volume_ml=(dose_mg/strength_num)*5
    return round(volume_ml,2)
print(calcualte_paracetamol_dose(weight, strength))
#Example
print(calcualte_paracetamol_dose(30,"120"))
#It will print "18.75"
