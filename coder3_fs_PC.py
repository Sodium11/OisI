mode = ""
instructions=['+','-','*','/']
variables=['a','b','c','d']
value_map={}
for v in variables:
    value_map[v]=0
figures=['0','1','2','3','4','5','6','7','8','9']

def output_chr(char):
    print(char)
def output_str(string):
    print(string)

def chr_input():
    print("Char:")
    return input()[0]

def num_input():
    print("Num:")
    return int(input())

def label_dict(opes):
    p=0
    result={}
    for ope in opes:
        if ope[0]==':':
            label=ope[1]
            result[label]=p
        p+=1
    return result

def decode_ope(ope,l_dict):#return -1 if not jump;return p if jump
    global value_map
    if 'J' in ope:
        pass
    else:
        fields=ope.split('=')
        latter_fields=
        first=fields[0]
        third=0
        try:
            third=int(fields[1])
        except ValueError:
            if fields[1]=='I':
                third=num_input()
            else:
                third=value_map[fields[1]]
                
        if first=='O':
            output_str(str(third))
        else:
            value_map[first]=third
    return -1

def run_program(program_str):
    global value_map
    output_str(program_str)
    opes=program_str.rstrip(';').split(';')
    l_dict=label_dict(opes)
    p=0
    while p<len(opes):
        ope=opes[p]
        result=decode_ope(ope,l_dict)
        if result==-1:
            p+=1
        else:
            p=result
program="O=I;"
run_program(program)
