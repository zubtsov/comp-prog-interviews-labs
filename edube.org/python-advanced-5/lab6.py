# https://edube.org/learn/pcpp1-5/lab-csv-lab-2

from csv import DictWriter

with open('exam_results.csv', 'w', newline='') as f:
    fieldnames = ['Exam Name', 'Number of Candidates',
                  'Number of Passed Exams', 'Number of Failed Exams',
                  'Best Score', 'Worst Score']

    w = DictWriter(f, fieldnames=fieldnames)

    w.writeheader()
    w.writerow(rowdict=dict(zip(fieldnames, ['Maths', 8, 4, 6, 90, 33])))
    w.writerow(rowdict=dict(zip(fieldnames, ['Physics', 3, 0, 3, 66, 50])))
    w.writerow(rowdict=dict(zip(fieldnames, ['Biology', 5, 2, 3, 88, 23])))
