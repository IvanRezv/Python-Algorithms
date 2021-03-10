startS = ["[","{","("]
endS = ["]","}",")"]

def balance(myStr):
    stack= []
    for i in myStr:
        if i in startS:
            stack.append(i)
        elif i in endS:
            position = endS.index(i)
            if ((len(stack)>0) and (startS[position] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Не правильно"
    if len(stack) == 0:
        return "Правильно"


print (balance("{[()](){}}"))