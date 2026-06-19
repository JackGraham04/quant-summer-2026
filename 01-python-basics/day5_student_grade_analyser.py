import csv 

def average_grade(*args):
    return sum(args)/len(args)

results = []

with open('01-python-basics/students.csv', 'r') as grade_file:
    reader = csv.DictReader(grade_file)

    for line in reader:
        average = round(average_grade(int(line['Maths']), int(line['English']), 
                                      int(line['Science'])), 1)
        
        name = line['Name']

        if average >= 70:
            grade = 'First'
        elif average >= 60:
            grade = '2:1'
        elif average >= 50:
            grade = '2:2'
        else:
            grade = 'Fail'
        
        print(f'{name}: {average} - {grade}')

        results.append({'Name': name,'Average': average,'Grade': grade})
    
with open('01-python-basics/student_results.csv', 'w', newline='') as results_file:
    fieldnames = ['Name', 'Average', 'Grade']
        
    writer = csv.DictWriter(results_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)







