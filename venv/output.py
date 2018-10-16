import re

from roll import droll


def res_out(in_vk, mark):

    if mark == 0:
        exp = droll(in_vk, mark)
        output = str(in_vk) + " " + str(exp[0])
        output = re.sub('[('',]', '', output)
        return output

    elif mark == 2:
        exp = droll((in_vk + str(6)), mark)
        suc_cnt = exp[0].count('6')
        output = str(in_vk) + " | " + str(suc_cnt) + " Успехов"
        output = re.sub('[('',]', '', output)
        return output

    else:
        exp = droll(in_vk, mark)
        output = str(in_vk) + " " + str(exp[0]) + " = " + str(exp[1])
        output = re.sub('[(''),]', '', output)
        return output

if __name__ == '__main__':
    res_out()