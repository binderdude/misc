def main():
    while 1:
        N = input("Please input 4 number separately by space: ").split(' ')
        if len(N) == 4:
            break

    for i in range(4):
        N[i] = int(N[i])
    temp = [0,0,0,0]
    operator_list = ['+','-','*','/']
    operator = []
    number = []
    correct = []

    #Permutation of number
    for i in range(4):
        for j in range(4):
            if j == i:
                continue
            for k in range(4):
                if k == j or k == i:
                    continue
                for l in range(4):
                    if l == k or l == j or l == i:
                        continue
                    temp1 = N[i]
                    temp2 = N[j]
                    temp3 = N[k]
                    temp4 = N[l]
                    temp = [temp1, temp2, temp3, temp4]
                    number.append(temp)

    #permutation of operator
    for i in range(4):
        for j in range(4):
            for k in range(4):
                temp1 = operator_list[i]
                temp2 = operator_list[j]
                temp3 = operator_list[k]
                oper_temp = [temp1, temp2, temp3]
                operator.append(oper_temp)

    #working with bracket (5 conditions)
    for number_row in number:
        for oper_row in operator:
            result = 0

            # (a b) (c d)
            result = calc(calc(number_row[0], number_row[1], oper_row[0]), calc(number_row[2], number_row[3], oper_row[2]), oper_row[1])
            if abs(result - 24) < 0.001:
                correct.append("({0} {1} {2}) {3} ({4} {5} {6})".format(number_row[0], oper_row[0], number_row[1], oper_row[1], number_row[2], oper_row[2], number_row[3]))

            # ((a b) c) d
            result = calc(number_row[0], number_row[1], oper_row[0])
            result = calc(result, number_row[2], oper_row[1])
            result = calc(result, number_row[3], oper_row[2])
            if abs(result - 24) < 0.001:
                correct.append("(({0} {1} {2}) {3} {4}) {5} {6}".format(number_row[0], oper_row[0], number_row[1], oper_row[1], number_row[2], oper_row[2], number_row[3]))

            # (a (b c)) d
            result = calc(number_row[1], number_row[2], oper_row[1])
            result = calc(number_row[0], result, oper_row[0])
            result = calc(result, number_row[3], oper_row[2])
            if abs(result - 24) < 0.001:
                correct.append("({0} {1} ({2} {3} {4})) {5} {6}".format(number_row[0], oper_row[0], number_row[1], oper_row[1], number_row[2], oper_row[2], number_row[3]))

            # a ((b c) d)
            result = calc(number_row[1], number_row[2], oper_row[1])
            result = calc(result, number_row[3], oper_row[2])
            result = calc(number_row[0], result,  oper_row[0])
            if abs(result - 24) < 0.001:
                correct.append("{0} {1} (({2} {3} {4}) {5} {6})".format(number_row[0], oper_row[0], number_row[1], oper_row[1], number_row[2], oper_row[2], number_row[3]))                # a (b (c d))
            result = calc(number_row[2], number_row[3], oper_row[2])
            result = calc(number_row[1], result, oper_row[1])
            result = calc(number_row[0], result, oper_row[0])
            if abs(result - 24) < 0.001:
                correct.append("{0} {1} ({2} {3} ({4} {5} {6}))".format(number_row[0], oper_row[0], number_row[1], oper_row[1], number_row[2], oper_row[2], number_row[3]))
    correct = list(dict.fromkeys(correct))
    for row in correct:
        print(row)

def calc(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    else:
        if b == 0:
            return 999999
        return a / b


main()
