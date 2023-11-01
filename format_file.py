import math
import csv
def roundup(x):
    return int(math.ceil(x / 100.0)) * 100
def list_text(l):
    s=''
    if len(l) == 1:
        return str(l[0])
    else:
        for i in l:
            s=s+','+str(i)
    return s[1::]
def header(f,page,c_name,c_no,reg):    
    f.writelines([('SECONDARY SCHOOL CERTIFICATE EXAMINATION 2023').center(143,' ')])
    f.write('\n')
    f.writelines(['**CBSE-66/ CENTRE MEMO**'.center(143,' ')])
    f.write('\n')
    f.write(('| Region : '+reg).ljust(34,' ')+('CENTRE-  '+c_no+' :: '+c_name).ljust(122-(len('| Region : '+reg)+len('PAGE : '+str(page))),' ')+'PAGE : '+str(page))
    f.write('\n')
    f.write('|'+'-'*141+'|')
    f.write('\n')
    f.write('|DATE OF'.ljust(12,' ')+'SUBJECT DESCRIPTION'.ljust(26,' ')+'ROLL NOS REGISTERED'.ljust(22,' ')+'|ROLL NOS OF CANDIDATES'.ljust(37,' ')+'|ROLL NOS OF UNFAIR'.ljust(20,' ')+'|TOTAL NO OF ANSWER BOOKS'.ljust(25,' ')+'|')
    f.write('\n')
    f.write('|EXAM.'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|ABSENT, IF ANY'.ljust(37,' ')+'|MEANS CASES,IF ANY'.ljust(20,' ')+'|SENT TO REGIONAL OFFICE '.ljust(25,' ')+'|')
    f.write('\n')
    f.write('|'+'-'*141+'|')
    #f.write('\n')
    #f.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
    f.flush()
def footer(f,fname,sname,ftsname,stsname):
    f.write('\n')
    f.write('| **Certified that the No. of Answer Books indicated in Col-6 have been checked and packed for dispatch'.ljust(142,' ')+'|')
    f.write('\n')
    f.write('| Withnes of two asstt. Supdt.(one should be from the school other than exam centre'.ljust(142,' ')+'|')
    f.write('\n')
    f.write('| 1 Signature  :..................................................  2. Signature  :..................................................'.ljust(142,' ')+'|')
    f.write('\n')
    f.write(('|   Name       :'+fname.upper().ljust(50,'.')+'     Name       :'+sname.upper().ljust(50,'.')).ljust(142,' ')+'|')
    f.write('\n')
    f.write('|   Designation:TEACHER...........................................     Designation:TEACHER...........................................'.ljust(142,' ')+'|')
    f.write('\n')
    f.write(('|   Address    :'+ftsname.upper().ljust(50,'.')+'     Address    :'+stsname.upper().ljust(50,'.')).ljust(142,' ')+'|')
    f.write('\n')
    f.write('|'+' '*141+'|')
    f.write('\n')
    f.write('| NOTE :-ONE COPY TO BE PLACED IN THE ANSWER BOOK BAG'.ljust(142,' ')+'|')
    f.write('\n')
    f.write('|        ONE  TO BE DELIVERED AT THE RECEIVING CENTER AND'.ljust(142,' ')+'|')
    f.write('\n')
    f.write('|        ONE  TO BE RETAINED BY THE CENTRE FOR RECORD'.ljust(142,' ')+'|')
    f.write('\n')
    f.write('|'+'SIGNATURE OF THE CENTRE SUPDT.'.rjust(141,' ')+'|')
    f.write('\n')
    f.write('|'+'RUBBER STAMP AND DATE '.rjust(141,' ')+'|')
    f.write('\n')
    f.write('|'+'-'*141+'|')
    f.write('\f')
    f.flush()
def middle(file,total_stu,absent_stu,present_stu):
    #file.write('\n')
    #file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,'-')+'|'.ljust(20,'-')+'|'.ljust(25,'-')+'|')
    file.write('\n')
    file.write('|'+'** SUBJECT-TOTAL **'.center(55,' ')+str(len(total_stu)).rjust(4,' ')+('|'+str(len(absent_stu))).ljust(37,' ')+'|'.ljust(20,' ')+('|'+str(len(present_stu))).ljust(25,' ')+'|')
    file.write('\n')
    file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,'-')+'|'.ljust(20,'-')+'|'.ljust(25,'-')+'|')
    file.write('\n')
    file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
    file.write('\n')
    file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
    file.write('\n')
    file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
    file.write('\n')
    file.write('|'.ljust(60,'-')+'|'.ljust(37,'-')+'|'.ljust(20,'-')+'|'.ljust(25,'-')+'|')
def series(file,absent_stu):
    #rt=csv.reader(file)
    #next(rt)
    first_record=file[0]
    f=file[0]
    break_point=roundup(int(f))
    x=[]
    c_roll=0
    l=[f]
    ser=[]
    abs_lst=[]
    for i in file[1:]:    
        if (int(i)-int(f))==1 and int(i)<=break_point :
            l.append(i)
            f=i
        else:
            '''for j in absent_stu:
                if int(j) >= int(l[0]) and int(j)<=int(l[-1]):
                    x.append(str(j))'''
        
            ser.append([l[0],l[-1]])
            l.clear()
            break_point=roundup(int(i)+1)
            l.append(i)
            f=i
    
   
    else:
        ser.append([l[0],l[-1]])
        '''for j in absent_stu:
            if int(j) >= int(l[0]) and int(j)<=int(l[-1]):
                x.append(str(j))'''
            #print(x)
    
   
    return ser
