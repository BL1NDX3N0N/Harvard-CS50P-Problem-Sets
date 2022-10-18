operand1, operator, operand2 = input('Expression: ').strip().split(' ')

match operator:
    case '+':
        print(float(operand1) + float(operand2))
    case '-':
        print(float(operand1) - float(operand2))
    case '*':
        print(float(operand1) * float(operand2))
    case '/':
        print(float(operand1) / float(operand2))