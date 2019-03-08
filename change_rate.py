import decimal

f2 = open('output_shrunk.log','a')
with open('/home/kartik/candump_files/test_dump.log') as file:
    for line in file:
        get_line = str(line[1:17])
        get_line = decimal.Decimal(get_line)
        get_line = get_line/3
        if (len(str(get_line))!=17):
            get_line = format(get_line, '.7f')
        # print(get_line[0])

        line_list = list(line)
        for i in range(len(get_line)):
            line_list[i+1] = get_line[i]

        line = "".join(line_list)
        f2.write(line)

f2.close()
print("Writing complete")
