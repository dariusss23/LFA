def TM(tape_string):
    s=list(tape_string)
    top=0
    state='q0'

    while state!='qaccept':
        symbol=s[top]

        if state=='q0':
            if symbol=='1':
                top+=1
            elif symbol=='+':
                s[top]='1'
                state='q1'
                top+=1

        elif state=='q1':
            if symbol=='1':
                top+=1
            elif symbol == '$':
                state = 'q2'
                top -= 1

        elif state=='q2':
            if symbol=='1':
                s[top]='$'
                state='qaccept'
                top-=1

    return s.count('1')

input_string="1111+111$"
rezultat=TM(input_string)

print("Rezultatul final:", rezultat)
