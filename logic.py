import re
from roll import droll

def clear(vk_text):
    clr = vk_text.split(']', 1)
    roll = str(clr[1])
    clr = roll.strip()
    return comm(clr)

def comm(vk_text):

    if ' ' in vk_text:
        tp = vk_text.split(' ', 1)
        result = droll(tp[0])
        cmt = tp[1]

        vk_res = str(result) + " [" + str(cmt) + "]"
        vk_res = re.sub('[(),]', '', vk_res)

        return vk_res
    else:
        vk_res = droll(vk_text)

        return vk_res