#Convert log file to text or csv file

with open('/home/naveed/Dropbox/Pallet_Jack/1_25_forward.log') as file: #path of the file to be read
    lines = file.read().splitlines() #split the file into lines
    #lines = [lines[x:x+3] for x in range(0, len(lines), 3)]
    print "length:", len(lines)
    i=0
    while(1):
        dat = lines[i].split(' ') #split at space
        #189 is the chosen identifier
        if dat[2][0] == '7':
            if dat[2][1] == 'F':
                if dat[2][2] == '4':
                    #print dat[2]

                    #writing into text file
                    file = open('1_25_7F4_forward.csv', 'a+') #name of the file to be written
                    file.write(str(float(dat[0][1:18])-1547668991.0000 ))
                    #print str(float(dat[0][1:18])-1547668991.0000)
                    file.write(',')
                    for j in range(8): #iterate over 8 bytes and write one byte at a time with delimiter
                        file.write(str(int(dat[2][4+2*j:4+2*(j+1)],16))) #convert hex data to decimal and write
                        #file.write(dat[2][4+2*j:4+2*(j+1)]) #write as hex data
                        file.write(',')
                    file.write('\n')
                    file.close()

        i = i+1
        if i == len(lines):
            break
