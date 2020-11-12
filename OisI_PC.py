#from microbit import *
#display.show("S")
mode = ""
instructions=['+','-','*','/']
variables=['a','b','c','d']
value_map={}
for i in variables:
    value_map[i]=0
figures=['0','1','2','3','4','5','6','7','8','9']
label_p=[0 for i in range(128)]
queue=[]

def output_chr(char):
    print("Output:"+char)
def output_str(string):
    print("Output:"+string)
def chr_input(li):
    print(li)
    print("char:")
    return input()

def num_input(mode="int"):
    print("num:")
    if mode=="int":
        return int(input())
    else:
        return input()

def label_register(program):
    global label_p
    opes=program.split(';')
    for p in range(len(opes)):
        ope=opes[p]
        if ope[0]=='L':
            p_num=int(ope[1:])
            label_p[p_num]=p

def read_v(v):
    if v in variables:
        return value_map[v]
    elif v=='I':
        return num_input()
    elif v=='Q':
        global queue
#       print(queue)
        if len(queue)>0:
            n= queue.pop(0)
#           print(queue)
            return n
        else:
            return 0
    else:
        return int(v)

def write_v(v,n):
    global value_map
    if v in variables:
        value_map[v]=n
    elif v=='O':
        output_str(str(n))
    elif v=='Q':
        global queue
        queue.append(n)
        #print(queue,n)

def read_const(ope,start_p):
    n=0
    p=start_p
    while ope[p] in figures:
        n*=10
        n+=int(ope[p])
        p+=1
        if p>=len(ope):
            break
    return n

def run_program(program_str):
    output_str(program_str)
    label_register(program_str)
    #print(label_p)
    opes=program_str.split(';')
    p=-1
    while p<len(opes)-1:
        p+=1
        ope=opes[p]
        #print(ope)
        first=ope[0]
        if first=='L':
            continue
        second=ope[1]
        third=ope[2]
        if third=='Q':
            if len(queue)==0:
                third=0
            else:
                third=queue[0]
        elif ope[2] in figures:
            third=read_const(ope,2)
        else:
            third=read_v(ope[2])
        #print(first,second,third)
        if second=='<':
            if read_v(first)<third:
                label_num=int(ope.split('J')[1])
                p=label_p[label_num]
                continue
        elif second=='>':
            if read_v(first)>third:
                label_num=int(ope.split('J')[1])
                p=label_p[label_num]
                continue
#        print(len(ope))
        if len(ope)<=4:
            write_v(first,read_v(ope[2:]))
            continue
        fourth=ope[3]
        fifth=read_v(ope[4])
        #print(fourth,fifth)
        if fourth=='+':
            write_v(first,third+fifth)
        elif fourth=='-':
            write_v(first,third-fifth)
        elif fourth=='*':
            write_v(first,third*fifth)
        elif fourth=='/':
            write_v(first,third//fifth)
        else:
            write_v(first,third)

print(read_const("jioj120njn",4))
file=open("test.oisi","r")
program=file.read().rstrip('\n')
file.close()
run_program(program)
