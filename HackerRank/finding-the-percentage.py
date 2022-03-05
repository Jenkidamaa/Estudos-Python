## https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    media = 0
    media_1 = 0
    for i in range(3):
      media = student_marks[query_name][i]
      media_1 += media
    print("%.2f" %(media_1/3))
