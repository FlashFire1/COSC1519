'''
Created on 20 Sept 2021

@author: Eamon
'''
infile = open("quiz_scores.txt","r")
outfile = open("avg_scores.txt","w+")
for line in infile:
    each_num = []
    values = line.split(',')
    for ind_score in range(1, len(values)):
        each_num.append(int(values[ind_score]))
    avg_score = round(sum(each_num) / len(each_num), 2)
    if (avg_score % 1) == 0:
        avg_score = int(avg_score)
    ind_line = values[0] + ',' + str(avg_score) + '\n'
    outfile.write(ind_line)
outfile.close()