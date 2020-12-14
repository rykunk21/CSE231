"""
This program takes a text file, scores.txt in as input. Scores.txt is
separated into n lines (n can be any value) containing a comma separated
last and first name, followed by 4 exam scores separated by a random amount
of spaces. The program will read the file and return an organized table
displaying each students name, exam scores, and compute an average exam
score for each student. The program will then compute an average score by
all students on each exam and print that as well. It will also print the
student names in alphabetical order.
"""


with open('../Extras/scores.txt', 'r') as scores:
    student_exams = []
    lines = sorted([tuple(line.strip().split()) for line in
                    scores.readlines()])

    print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format('Name', 'Exam1',
                                                         'Exam2', 'Exam3',
                                                         'Exam4', 'Mean'))

    for line in lines:
        last, first, e1, e2, e3, e4 = line
        name = '{} {}'.format(last, first)
        exams = list(map(int, [e1, e2, e3, e4]))
        student_exams.append(exams)
        mean = sum(exams) / 4
        print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(name, exams[0],
                                                          exams[1],
                                                          exams[2],
                                                          exams[3], mean))

    t1, t2, t3, t4 = 0, 0, 0, 0
    length = len(student_exams)
    for _ in student_exams:
        e1, e2, e3, e4 = _
        t1 += e1
        t2 += e2
        t3 += e3
        t4 += e4
    print(
        "{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format('Exam Mean', (t1 / length),
                                                    (t2 / length),
                                                    (t3 / length),
                                                    (t4 / length)))
