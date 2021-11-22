# Binary Operator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290

global_dict = {}
next_flag = 1

def update_dict(dict: dict, key: str, value: int):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value

# Make i#j as symbol like $xxx, xxx is serial number increasing by next_flag
def update_global_dict(exp: str):
    if exp not in global_dict:
        global next_flag
        global_dict[exp] = '${:03d}'.format(next_flag)
        next_flag += 1
    return global_dict[exp]

# Split the variable into constant and variable part
# e.g. 2+3$001$002 -> {"const": 2, "$001$002": 3}
def num_to_dict(num: str):
    result_dict = {}
    num = num.split('+')
    for var in num:
        flag = 0
        const = True
        for c in var:
            if not c.isdigit():
                const = False
                var_num = int(var[0:flag]) if flag != 0 else 1
                var_var = var[flag:]
                update_dict(result_dict, var_var, var_num)
                break
            else:
                flag += 1
        if const:
            result_dict["const"] = int(var)
    return result_dict

def process(exp: str):
    stack_num = []
    stack_exp = []
    temp_num = ""
    for c in exp:
        # print("current", c)
        if c == '(':
            if temp_num:
                stack_num.append(temp_num)
                temp_num = ""
        elif c == ')':
            if temp_num:
                stack_num.append(temp_num)
                temp_num = ""
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            op = stack_exp.pop()

            if num1.isdigit() and num2.isdigit():
                if op == '+':
                    stack_num.append(str(int(num1) + int(num2)))
                elif op == '*':
                    stack_num.append(str(int(num1) * int(num2)))
                else:
                    stack_num.append(update_global_dict(num1 + op + num2))
                    # print(global_dict, stack_num)
            else:
                temp_dict1 = num_to_dict(num1)
                temp_dict2 = num_to_dict(num2)
                # print(temp_dict1, temp_dict2)

                if op == '+':
                    result_dict = {}
                    for key, value in temp_dict1.items():
                        update_dict(result_dict, key, value)
                    for key, value in temp_dict2.items():
                        update_dict(result_dict, key, value)
                    # print("+", result_dict)
                    result_str = []
                    for var, num in sorted(list(result_dict.items())):
                        if var == "const":
                            if num != 0:
                                result_str.insert(0, str(num))
                        elif num == 1:
                            result_str.append(var)
                        else:
                            result_str.append(str(num) + var)
                    result_str = '+'.join(result_str)
                    stack_num.append(result_str)
                elif op == '*':
                    result_dict = {}
                    for key1, value1 in temp_dict1.items():
                        for key2, value2 in temp_dict2.items():
                            if value1 == 0 or value2 == 0:
                                continue
                            elif key1 == "const" and key2 == "const":
                                result_dict["const"] = value1 * value2
                            elif key1 == "const":
                                update_dict(result_dict, key2, value1 * value2)
                            elif key2 == "const":
                                update_dict(result_dict, key1, value1 * value2)
                            else:
                                # Combine variable part and sort it, e.g. $001$002 * $001$003 -> $001$001$002$003
                                new_key = '$' + '$'.join(sorted(key1.split('$')[1:] + key2.split('$')[1:]))
                                update_dict(result_dict, new_key, value1 * value2)
                    # print("*", result_dict)
                    if not result_dict:
                        result_str = "0"
                    else:
                        result_str = []
                        for var, num in sorted(list(result_dict.items())):
                            if var == "const":
                                result_str.insert(0, str(num))
                            elif num == 1:
                                result_str.append(var)
                            else:
                                result_str.append(str(num) + var)
                        result_str = '+'.join(result_str)
                    stack_num.append(result_str)
                else:
                    stack_num.append(update_global_dict(num1 + op + num2))
        elif c == '+' or c == '*' or c == '#':
            if temp_num:
                stack_num.append(temp_num)
                temp_num = ""
            stack_exp.append(c)
        else:
            temp_num += c

    if temp_num:
        return temp_num
    else:
        return stack_num[-1]

T = int(input())
for t in range(T):
    N = int(input())

    output_dict = {}
    output_index = []
    next_index = 1
    for i in range(0, N):
        input_str = input()
        # Make output_str the most simplified var order
        output_str = process(input_str)
        # print(input_str, " -> ", output_str)
        if output_str not in output_dict:
            output_dict[output_str] = next_index
            next_index += 1
        output_index.append(str(output_dict[output_str]))

    # print("\n", global_dict)
    print(f"Case #{t + 1}: {' '.join(output_index)} ")
