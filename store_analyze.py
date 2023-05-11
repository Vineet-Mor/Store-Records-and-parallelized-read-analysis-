import os
import multiprocessing
import sys
import time
def create_dirs():
    for curr_dir in ['Fixed', 'Delimited', 'Offset']:
        if(not os.path.isdir(curr_dir)):
            os.mkdir(curr_dir)


### This is main cell
def read_in_tuples(file_location):
    curr_f = open(file_location)
    highest = open(file_location)
    high = 0
    value = highest.readline()
    while (len(value) > 0):
        high += 1
        value = highest.readline()
    line = curr_f.readline()
    delimitedcount = 0
    dpage = 1
    delimited = open("Delimited/page_1.txt", "w")
    fixedcount = 0
    fpage = 1
    fixed = open("Fixed/page_1.txt", "w")
    offsetcount = 0
    opage = 1
    offset = open("Offset/page_1.txt", "w")
    curr_tuple = line.strip().split(',')
    size = len(curr_tuple) - 1
    offstr = ""
    offstr = offstr + str(size)
    offstr = offstr + ",2\n"
    offset.write(offstr)
    offstr = ""
    arr = []
    pl = -1
    k = 0
    total = 20
    fixedstr = ""
    for i in curr_tuple:
        if (not i == "INSERT"):
            offstr = offstr + i
            arr.append(pl + 1)
            pl = pl + len(i)

            totalpresent = len(i)
            fixedstr = fixedstr + i
            for j in range(total - totalpresent):
                fixedstr = fixedstr + 'x'
    ostr = ""
    for i in arr:
        if ((i + (size * 2)) < 10):
            ostr = ostr + str((i + (size * 2))) + 'x'
        else:
            ostr = ostr + str((i + (size * 2)))
    ostr = ostr + offstr
    offset.write(ostr)
    fixed.write(fixedstr)
    fixed.write("\n")
    offset.write("\n")
    fixedcount = fixedcount + 1
    offsetcount = offsetcount + 1
    string = ""
    for i in line:
        if (i == ',' and k > 0):
            string = string + '$'
        elif (not i == ',' and k > 0):
            string = string + i
        if (i == ','):
            k = k + 1
    fixedstr = ""
    ostr = ""
    offstr = ""
    delimitedcount = delimitedcount + 1
    delimited.write(string)
    while (len(line) > 0):
        if ((delimitedcount % 500) == 0.0 and delimitedcount > 400 and delimitedcount < high):
            # print(delimitedcount,len(line))
            dpage = dpage + 1
            delimited.close()
            dstr = "Delimited/page_"
            dstr = dstr + str(dpage)
            dstr = dstr + ".txt"
            delimited = open(dstr, "w")
        if ((fixedcount % 500) == 0.0 and fixedcount > 400 and fixedcount < high):
            # print(delimitedcount,len(line))
            # print(fixedcount)
            fpage = fpage + 1
            fixed.close()
            fstr = "Fixed/page_"
            fstr = fstr + str(fpage)
            fstr = fstr + ".txt"
            fixed = open(fstr, "w")
        if ((offsetcount % 500) == 0.0 and offsetcount > 400 and offsetcount < high):
            # print(delimitedcount,len(line))

            opage = opage + 1
            offset.close()
            ostr = "Offset/page_"
            ostr = ostr + str(opage)
            ostr = ostr + ".txt"
            offset = open(ostr, "w")
            offstr = ""
            offstr = offstr + str(size)
            offstr = offstr + ",2\n"
            offset.write(offstr)
        line = curr_f.readline()
        curr_tuple = line.strip().split(',')  # current tuple as a list
        k = 0
        fixedstr = ""
        string = ""

        for i in line:
            if (i == ',' and k > 0):
                string = string + '$'
            elif (k > 0):
                string = string + i
            if (i == ','):
                k = k + 1
        delimitedcount = delimitedcount + 1
        size = len(curr_tuple) - 1
        offstr = ""
        arr = []
        pl = -1
        for i in curr_tuple:
            if (not i == "INSERT"):
                offstr = offstr + i
                arr.append(pl + 1)
                pl = pl + len(i)
                totalpresent = len(i)
                fixedstr = fixedstr + i
                for j in range(total - totalpresent):
                    fixedstr = fixedstr + 'x'
        fixedcount = fixedcount + 1
        offsetcount = offsetcount + 1
        ostr = ""
        for i in arr:
            if ((i + (size * 2)) < 10):
                ostr = ostr + str((i + (size * 2))) + 'x'
            else:
                ostr = ostr + str((i + (size * 2)))
        ostr = ostr + offstr
        if (len(ostr) > 2):
            offset.write(ostr)
            offset.write("\n")
            fixed.write(fixedstr)
            fixed.write("\n")
            delimited.write(string)
    # print(delimitedcount,fixedcount,offsetcount)
    delimited.close()
    fixed.close()
    offset.close()
    print("Stored")


def Offset(index):
    # iterate over files in
    # that directory
    file = []
    for filename in os.scandir('Offset'):
        if filename.is_file():
            file.append(filename.path)
    mean = []
    # print(len(file))
    for path in file:
        offset = open(path)

        line = offset.readline()
        curr_tuple = line.strip().split(",")
        # print(curr_tuple)
        if (len(curr_tuple) > 0):
            offsetvalue = int(curr_tuple[0]) * int(curr_tuple[1])
            total = 0
            meantotal = 0
            while (len(line) > 0):
                line = offset.readline()
                if (not line == "" and not line == " "):
                    arr = []
                    offstr = ""
                    for i in range(offsetvalue):
                        if (not line == "" and not line == " "):
                            offstr = offstr + line[i]
                            if not i % 2 == 0:
                                arr.append(int(offstr))
                                offstr = ""
                    # for i in range(len(line)):
                    if (index < int(curr_tuple[0]) - 1):
                        value = ""
                        for i in range(arr[index], arr[index + 1]):
                            value = value + line[i]
                        meantotal = meantotal + int(value)

                        total = total + 1
                        # print(value,total)
                        # print(arr)
                    else:
                        value = ""
                        for i in range(arr[index], len(line)):
                            value = value + line[i]
                        meantotal = meantotal + int(value)
                        # print(value)
                        total = total + 1

            mean.append(meantotal / total)
            # print(meantotal/total,path)
    # print(len(mean))
    return mean


def Delimited(index):
    file = []
    for filename in os.scandir('Delimited'):
        if filename.is_file():
            file.append(filename.path)
    mean = []
    # print(len(file))
    for path in file:
        delimited = open(path)
        line = delimited.readline()
        curr_tuple = line.strip().split('$')
        meantotal = 0
        total = 0
        for i in range(len(curr_tuple)):
            if (i == index and not curr_tuple[i] == ""):
                meantotal = meantotal + int(curr_tuple[i])
                total = total + 1
                # print(curr_tuple[i])
        while (len(line) > 0):
            line = delimited.readline()
            curr_tuple = line.strip().split("$")
            for i in range(len(curr_tuple)):
                if (i == index and not curr_tuple[i] == ""):
                    meantotal = meantotal + int(curr_tuple[i])
                    total = total + 1
                    # print(curr_tuple[i])
        if(not total==0):
            mean.append(meantotal/total)
        # print(meantotal/total,path)
    #print(len(mean))
    return mean



def Fixed(index):
    file=[]
    for filename in os.scandir('Fixed'):
        if filename.is_file():
            file.append(filename.path)
    mean=[]
    #print(len(file))
    for path in file:
        fixed=open(path)
        line=fixed.readline()
        curr_tuple = line.strip().split('x')
        meantotal=0
        total=0
        a=0
        for i in range(len(curr_tuple)-a):
            if(curr_tuple[i-a]==""):
                del curr_tuple[i-a]
                a=a+1
        for i in range(len(curr_tuple)):
            if(i==index and not curr_tuple[i]==""):
                meantotal=meantotal+int(curr_tuple[i])
                total=total+1
        #print(curr_tuple)

        while(len(line)>0):
            #print(len(line),"-------")
            line=fixed.readline()
            curr_tuple=line.strip().split('x')
            #print(line)
            a=0
            for i in range(len(curr_tuple)-a):
                if(curr_tuple[i-a]==""):
                    del curr_tuple[i-a]
                    a=a+1
            #print(curr_tuple)
            for i in range(len(curr_tuple)):
                if(i==index and not curr_tuple[i]==""):
                    meantotal=meantotal+int(curr_tuple[i])
                    total=total+1
                    #print(curr_tuple[i])
        #print(meantotal/total)
        if(not total==0):
            mean.append(meantotal/total)
    #print(len(mean))
    return mean


if __name__ == '__main__':
    command =sys.argv[1]  # This will be store or analyze
    if (command == 'store'):
        create_dirs()
        input_file_path = sys.argv[2]
        read_in_tuples(input_file_path)

    elif (command == 'analyze'):
        target_dir = sys.argv[2]
        target_attribute = int(sys.argv[3])
        num_threads = int(sys.argv[4])

        if target_dir=="Delimited":
            target_dir=Delimited
        elif target_dir=="Fixed":
            target_dir=Fixed
        else:
            target_dir=Offset

        t1=time.time()
        pool = multiprocessing.Pool(num_threads)
        result = pool.map(target_dir, (target_attribute,))
        pool.close()
        pool.join()
        totalmean=0
        for i in result[0]:
            totalmean=totalmean+i
        print(target_attribute," average: ",totalmean/len(result[0]))
        t2=time.time()
        #print(t2-t1,"................."num_threads)
