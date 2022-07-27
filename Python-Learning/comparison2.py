grade1=float(input('Please Enter 1.Number: '))
grade2=float(input('Please Enter 2.Number: '))
grade3=float(input('Please Enter 3.Number: '))

meanGrade=((grade1+grade2)*0.6 + (grade3*0.4))


if meanGrade >= 50:
    print('Valid and mean of grade: ',meanGrade)
else:
    print('not valid')






