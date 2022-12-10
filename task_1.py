# Доделать:
# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2 + 2 => 4;
# 1 + 2 * 3 => 7;
# 1 - 2 * 3 => -5;

import re


actions = {
    "^": lambda x, y: str(float(x)**float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def my_eval(expresion: str) -> str:

    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(
            match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(
                match.group(0), action(*match.groups()))

    return expresion


exp = "1 + 2 * 3 != 7"
if "!"  in exp:
    t="!"+str(exp[exp.index("!")+1])
    s = exp.split(t)
    m=my_eval(s[0])
    m2=my_eval(s[1])
    print(float(m) != float(m2))
elif "=" not in exp:
    if ">" in exp:
        s = exp.split(">")
        m=my_eval(s[0])
        m2=my_eval(s[1])
        print(float(m) > float(m2))
    if "<" in exp:
        s = exp.split("<")
        m=my_eval(s[0])
        m2=my_eval(s[1])
        print(float(m) < float(m2))

else:
    t=exp[exp.index("=")]
    if exp[exp.index("=")+1]=="=":
        t="=="
        s = exp.split(t)
        m=my_eval(s[0])
        m2=my_eval(s[1])
        print(float(m) == float(m2))
    elif exp[exp.index("=")+1] == "<":
        t="=<"
        s = exp.split(t)
        m=float(my_eval(s[0]))
        m2=float(my_eval(s[1]))
        print(m <= m2)
    elif exp[exp.index("=")+1] == ">":
        t="=>"
        s = exp.split(t)
        m=float(my_eval(s[0]))
        m2=float(my_eval(s[1]))
        print(m >= m2)