import random
import re


def droll(vkinput):

    d_res = 0
    total = [vkinput, ]
    i = 0
    if '+' in vkinput:
        p = re.compile('\d+d\d+[+]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = vkinput.replace('+', 'd')
            form = form.split('d')
            form = list((map(int, form)))
            while i < form[0]:
                i = i + 1
                d_throw = random.randint(1, form[1])
                d_res = d_res + d_throw
                total.append(d_throw)

            temp = str(total)
            temp2 = str(d_res + form[2])
            res = " roll " + str(temp) + " + " + str(form[2]) + " = " + str(temp2)

            res = re.sub('[(),]', '', res)

            return res


        else:

            return "Error. Formula 5d20/1d6+12/etc"

    elif '-' in vkinput:
        p = re.compile('\d+d\d+[-]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = vkinput.replace('-', 'd')
            form = form.split('d')
            form = list((map(int, form)))
            while i < form[0]:
                i = i + 1
                d_throw = random.randint(1, form[1])
                d_res = d_res + d_throw
                total.append(d_throw)

            temp = str(total)
            temp2 = str(d_res - form[2])
            res = " roll " + str(temp) + " - " + str(form[2]) + " = " + str(temp2)

            res = re.sub('[(),]', '', res)

            return res


        else:

            return "Error. Formula 5d20/1d6-5/etc "
    else:
       p = re.compile('\d+d\d+\Z')
       m = p.match(vkinput)

       if m:
         form = vkinput.split("d")
         form = list((map(int, form)))
         while i < form[0]:
             i = i + 1
             d_throw = random.randint(1, form[1])
             d_res = d_res + d_throw
             total.append(d_throw)

             temp = str(total)
             temp2 = str(d_res)

             res = " roll " + str(temp) + " = " + str(temp2)

             res = re.sub('[(),]', '', res)

             return res
       else:

           return "Error. Formula 5d20/1d6/etc"

    return "Что то совсем кривое. Формула 1d20+-Число"