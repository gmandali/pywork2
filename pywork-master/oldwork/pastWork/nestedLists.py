# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
students = []
gradeSet = set()
for rep in range(int(input())):
    student = [input(), float(input())]
    students.append(student)
    gradeSet.add(student[1])

runnerUpGrade = sorted(gradeSet)[1]
runnerUpNames = sorted([student[0] for student in students if student[1] == runnerUpGrade])
print("\n".join(runnerUpNames))
