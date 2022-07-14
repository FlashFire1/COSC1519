'''
Created on 30 Sept 2021

@author: Eamon
'''
#q1
#infile = open("mystery_chapter.txt","r")
#for line in infile:
#    print(line)

#q2
infile = open("grades.csv","r")
lines = infile.readlines()[1:]
first_assign = []
second_assign = []
third_assign = []
for line in lines:
    words = line.strip().split(',')
    avg_grade = round((int(words[2]) + int(words[3]) + int(words[4])) / 3)
    first_assign.append(int(words[2]))
    second_assign.append(int(words[3]))
    third_assign.append(int(words[4]))
    print(words[0],words[1],"grades are",words[2],"for A1,",words[3],"for A2,",words[4], "for A3, their average is", avg_grade)
avg_first = str(round(sum(first_assign) / len(first_assign), 1))
avg_second = str(round(sum(second_assign) / len(second_assign), 1))
avg_third = str(round(sum(third_assign) / len(third_assign), 1))
avg_global = str(round((float(avg_first) + float(avg_second) + float(avg_third)) / 3, 1))
print("\nA1 average is " + avg_first + "\nA2 average is " + avg_second + "\nA3 average is " + avg_third + "\nGlobal average is " + avg_global)