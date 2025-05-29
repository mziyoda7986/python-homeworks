import csv

with open("grades.csv", 'rt') as file:
    reader = csv.DictReader(file, delimiter=',')
    rows = list(reader)
print(rows)

sum = {}
num = {}
for i in rows:
    subject = i.get('Subject')
    grade = int(i.get('Grade'))
    if subject in sum.keys():
        sum_grade = sum.get(subject) + grade
        sum.update({subject: sum_grade})
    else:
        sum.update({subject : grade})
    if subject in num.keys():
        sum_num = num.get(subject) + 1
        num.update({subject: sum_num})
    else:
        num.update({subject : 1})


avg = []
Subject = list(sum.keys())
Grade = list(sum.values())
Num = list(num.values())
for i in range (len(Subject)):
    d = {}
    d.update({"Subject" : Subject[i]})
    d.update({"Average Grade" : round(Grade[i]/Num[i], 1)})
    avg.append(d)

with open ("average_grades.csv", 'w', newline='') as file:
    fieldnames = ['Subject', 'Average Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(avg)