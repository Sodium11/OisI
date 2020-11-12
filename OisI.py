from microbit import *
display.show("S")
mode = ""
instructions=['+','-','*','/']
value_map={}
value_map['A']=0
value_map['B']=0
value_map['C']=0
value_map['D']=0
figures=['0','1','2','3','4','5','6','7','8','9']
label_p=[0 for i in range(100)]

def output_chr(char):
    display.show(char)
def output_str(string):
    display.scroll(string)

def chr_input(li):
    sel_p=0
    while True:
        output_chr(li[sel_p])
        if button_a.was_pressed():
            sel_p+=1
            if sel_p>=len(li):
                sel_p=0
        elif button_b.was_pressed():
            return li[sel_p]

def num_input(mode="int"):
    number_str=""
    sel_p=0
    options=figures+['.']
    while True:
        output_chr(options[sel_p])
        if button_a.was_pressed():
            sel_p+=1
            if sel_p>=len(options):
                sel_p=0
        elif button_b.was_pressed():
            if options[sel_p]=='.':
                if mode=="int":
                    return int(number_str)
                else:
                    return number_str
            number_str+=options[sel_p]
#display.scroll("A:NEW B:OPEN")

def program_input():
    result=""
    while True:
        first=chr_input(variables+['L','O','R'])
        if first=='R':
            result=result.rstrip(';')
            return result
        result+=first
        if first=='L':
            label=num_input("str")
            result+=label+';'
            continue
        second=chr_input(['=','<','>'])
        result+=second
        third=chr_input(variables+['C','I'])
        if third=='C':
            third=str(num_input())
        result+=third
        fourth=chr_input([';']+instructions+['J'])
        result+=fourth
        if fourth=='J':
            label=chr_input(labels)
            result+=label+';'
            continue
        elif fourth in [';']:
            continue
        fifth=chr_input(variables+['C','I'])
        if fifth=='C':
            fifth=str(num_input())
        result+=fifth+';'

def label_register(program):
    global label_p
    opes=program.split(';'):
    for p in range(len(opes)):
        ope=opes[p]
        if ope[0]==':':
            p_num=int(ope[1:])
            label_p[p_num]=p

def run_program(program_str):
    output_str(program_str)
    opes=program_str.split(';')
    l_dict=label_dict(opes)
    p=-1
    while p<len(opes):
        p+=1
        ope=opes[p]
        first=ope[0]
        if first=='L':
            continue
        second=ope[1]
        third=ope[2]
        if third=='I':
            third=num_input()
        else:
            third=value_map[third]
        if second=='<':
            if value_map[first]<third:
                p=l_dict[ope[4]]
                continue
        elif second=='>':
            if value_map[first]>third:
                p=l_dict[ope[4]]
                continue
        if len(ope)==3:
            value_map[first]=value_map[third]
            if first=='O':
                output_str(str(value_map[first]))
            continue
        fourth=ope[3]
        fifth=ope[4]
        if fourth=='+':
            value_map[first]=third+value_map[fifth]
        elif fourth=='-':
            value_map[first]=third-value_map[fifth]
        elif fourth=='*':
            value_map[first]=third*value_map[fifth]
        elif fourth=='/':
            value_map[first]=third//value_map[fifth]
        elif fourth=='J':
            if value_map[first]==third:
                p=l_dict[ope[4]]
                continue
#main menu START
#A:make a new program
#B:open the saved program
while True:
    if (button_a.was_pressed()):
        mode = "NEW"
        break
    if (button_b.was_pressed()):
        mode = "OPEN"
        break
output_str(mode)
#main menu END
if mode=="NEW":
    program_str=program_input()
    output_str(program_str)
    output_str("SAVE")
    file_name=chr_input(figures)+".mbc"
    file=open(file_name,"w")
    file.write(program_str)
    file.close()
    output_str("SAVED")
elif mode=="OPEN":
    file_name=chr_input(figures)+".mbc"
    file=open(file_name,"r")
    program=file.read()
    file.close()
    run_program(program)
