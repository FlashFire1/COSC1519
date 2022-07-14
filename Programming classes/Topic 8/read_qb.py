infile = open("qbdata.txt","r")
outfile = open("qbnames.txt","w")

for line in infile:
    #use this to debug
    print("current line is:", line, end="")
    items = line.split()
    #in case we do not have the right format in the source file
    if len(items) >= 2:
        data_line = items[1] + ',' + items[0] + '\n'	# add '\n' to make a line
    else:
        data_line = "error reading the source file" +  '\n'
    # use this to debug
    print("new data line is:", data_line, end="")
    outfile.write(data_line) 			# write a string to outfile
    line = infile.readline()

#DO NOT FORGET TO CLOSE YOUR FILES
infile.close()
outfile.close()
