from flask import Flask, render_template, request, redirect, url_for,send_file
import pandas as pd
import csv
import io
from io import TextIOWrapper
import format_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    date=request.form.get("date")
    ftname=request.form.get("first_teacher").capitalize()
    stname=request.form.get("second_teacher").capitalize()
    ftsname=request.form.get("school1").capitalize()
    stsname=request.form.get("school2").capitalize()
    centre_name=request.form.get("center_name").upper()
    centre_no=request.form.get("center_no")
    reg=request.form.get("region").upper()
    #return f'{ftname}{stname}{ftsname}{stsname}{centre_name}{centre_no}{reg}'
    if 'file' not in request.files:
        # Handle case where no file is selected
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        # Handle case where no filename is provided
        return redirect(url_for('index'))

    if file:
        df=pd.read_csv(file)
        #txt_file=open('form66.txt','w')
        txt_file = io.StringIO()
        
        sub_list=df.subCode.unique()
        page_no=1
        def l_len(reg_stu,ab_stu):
            if ab_stu.count('---')==0:
                return len(reg_stu)-len(ab_stu)
            else:
                return len(reg_stu)-len(ab_stu)+1
        for sub in sub_list:
            total_stu=list(df[df['subCode']==sub]['roll'])
            stu=df[df['subCode']==sub]
            #print(stu)
            present_stu=list(stu[stu['absent']!='ABS']['roll'])
            absent_stu=list(stu[stu['absent']=='ABS']['roll'])
            
            w=format_file.series(list(stu['roll']),absent_stu)
            #print(w)
            for line in range(0,len(w),20):
                format_file.header(txt_file,page_no,centre_name,centre_no,reg)
                for i in range(line,line+20):
                    if i<len(w):
                        mask=(stu['roll']>=int(w[i][0]))&(stu['roll']<=int(w[i][-1]) )
                        x=stu.loc[mask]
                        reg_stu=list(x['roll'])
                        ab_stu=list(x[x['absent']=='ABS']['roll'])
                        if len(ab_stu)== 0:
                            ab_stu.append('---')
                        #print(type(w[i][0]),i,",".join([str(item) for item in ab_stu]))
                        if len(ab_stu)<=4:
                            txt_file.write('\n')
                            txt_file.write(('|'+date).ljust(12,' ')+str(sub).ljust(26,' ')+str(w[i][0])+'-'+str(w[i][-1]).ljust(9,' ')+str(len(reg_stu)).rjust(4,' ')+"|"+",".join([str(item) for item in ab_stu]).ljust(36,' ')+'|'.ljust(20,' ')+('|'+str(l_len(reg_stu,ab_stu))).ljust(25,' ')+'|')
                            txt_file.write('\n')
                            txt_file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
                        else:
                            #print(ab_stu)
                            for r in range(0,len(ab_stu),4):
                                if r==0:
                                    #print(r)
                                    txt_file.write('\n')
                                    txt_file.write(('|'+date).ljust(12,' ')+str(sub).ljust(26,' ')+str(w[i][0])+'-'+str(w[i][-1]).ljust(9,' ')+str(len(reg_stu)).rjust(4,' ')+"|"+",".join([str(item) for item in ab_stu[r:r+4]]).ljust(36,' ')+'|'.ljust(20,' ')+('|'+str(l_len(reg_stu,ab_stu))).ljust(25,' ')+'|')
                                    #file.write('\n')
                                    #file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
                                else:
                                    #print(r)
                                    txt_file.write('\n')
                                    txt_file.write('|'.ljust(12,' ')+''.ljust(26,' ')+"".rjust(22,' ')+"|"+",".join([str(item) for item in ab_stu[r:r+4]]).ljust(36,' ')+'|'.ljust(20,' ')+('|'+"").ljust(25,' ')+'|')
                                    txt_file.write('\n')
                                    txt_file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
                    
                
                    else:
                        txt_file.write('\n')
                        txt_file.write('|'.ljust(12,' ')+''.ljust(26,' ')+''.ljust(22,' ')+'|'.ljust(37,' ')+'|'.ljust(20,' ')+'|'.ljust(25,' ')+'|')
                #format_file.middle(file,total_stu,absent_stu,present_stu)
                txt_file.write('\n')
                txt_file.write('|'+'-'*141+'|')
                if len(w)-line<=20:
                    format_file.middle(txt_file,total_stu,absent_stu,present_stu)
                format_file.footer(txt_file,ftname,stname,ftsname,stsname)
                txt_file.write('\n\n')
                page_no+=1
        
        txt_file.seek(0)
        iobyte=io.BytesIO()
        iobyte.write(txt_file.read().encode('utf-8'))
        iobyte.seek(0)
        iobyte.flush()
        
    return send_file(iobyte,as_attachment=True,download_name="form66.txt")

if __name__ == '__main__':
    app.run()
