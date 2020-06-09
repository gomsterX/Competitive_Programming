for i in range(int(input())):
    s = input()

    rpn_string = ""
    op_string = ""
    count = 0
    for i in s:
        if i == '(':
            True
        elif (i == ')'):
            rpn_string += op_string[-1:]
            op_string = op_string[:-1]
        elif(i == '*' or i == '/' or i == '-' or i == '+' or i == '^'):
            op_string += i
        else:
            rpn_string += i

    print(rpn_string)
