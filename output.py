import re

from roll import droll


def res_out(in_vk, mark):
    exp = droll(in_vk, mark)

    if mark == 0:
        output = str(in_vk) + " " + str(exp[0])
        output = re.sub('[(''),]', '', output)
        return output

    else:
        output = str(in_vk) + " " + str(exp[0]) + " = " + str(exp[1])
        output = re.sub('[(''),]', '', output)
        return output
