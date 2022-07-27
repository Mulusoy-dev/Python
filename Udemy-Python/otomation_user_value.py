#Kullanıcının girdiği değere göre verileri sınıflandıran uygulama

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}


#TODO-2: Write your code below to add the grades to student_grades.👇


#print(len(student_scores.keys()))
#print(student_scores.keys())
#print(student_scores.values())





#for key in student_scores.keys():
#    for value in student_scores.values():
#        if value>=91 and value<=100:
#            student_grades.update({key:"Outstanding"})
#            break    
#        elif value>=81 and value<=90:
#            student_grades.update({key:"Exceeds Expectations"})
#            break    
#        elif value>=71 and value<=80:
#            student_grades.update({key:"Acceptable"})
#            break
#        else:
#            student_grades.update({key:"Fail"})
#            break
     
    
for key, value in student_scores.items():
    #print(key,value)
    if value>90:
        student_grades.update({key:"Outstanding"})
            
    elif value>80:
        student_grades.update({key:"Exceeds Expectations"})
        
    elif value>70:
        student_grades.update({key:"Acceptable"})
    
    else:
        student_grades.update({key:"Fail"})
        




print(student_grades)


    

# 🚨 Don't change the code below 👇
#print(student_grades)