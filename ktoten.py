#腾讯
def trans_map(cint):
    if cint < 0:
        print("不合法")
        return
    elif cint < 10:
        return cint
    elif cint >= 10:
        return chr(cint - 10 + 65)

def anyToTen(m, origin):
    # 任意进制的数转换为10机制
    return int(str(origin), base=m)

def tenToAny(n, origin):
    # 10进制转换为任意进制的数
    list = []
    while True:
        # 取商
        s = origin // n
        # 取余数
        tmp = origin % n
        list.append(trans_map(tmp))
        if s == 0:
            break
        origin = s
    list.reverse()
    list = [str(each) for each in list]
    return ''.join(list)

def compute(in_list):
    if not in_list:
        return
    # 要计算的实例个数
    compute_num = int(in_list[0])
    result = []
    for i in range(compute_num):
        hex = int(in_list[2 * i + 1])
        operand = in_list[2 * i + 2]
        operand1, operand2, cp_type = operand.split()[0], operand.split()[1], operand.split()[2]
        operand1 = anyToTen(hex, operand1)
        operand2 = anyToTen(hex, operand2)
        res = 0
        if cp_type == "+":
            res = operand1 + operand2
        elif cp_type == "-":
            res = operand1 - operand2
        elif cp_type == "*":
            res = operand1 * operand2
        result.append(tenToAny(hex, res))
    return result

in_list = ["3", "10", "114514 1919810 +", "2", "100 11 *", "36", "TXDY DJQ -"]
compute(in_list)
