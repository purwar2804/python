#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    p1=p2=p3=0
    for i in range(1,len(patient_medical_speciality_list),2):
        if(patient_medical_speciality_list[i]=="P"):
            p1=p1+1
        elif(patient_medical_speciality_list[i]=="O"):
            p2=p2+1
        elif(patient_medical_speciality_list[i]=="E"):
            p3=p3+1
    if(max(p1,p2,p3)==p1):
        speciality="Pediatrics"
    elif(max(p1,p2,p3)==p2):
        speciality="Orthopedics"
    elif(max(p1,p2,p3)==3):
        speciality="ENT"

    return speciality


patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
