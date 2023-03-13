import random
from hermetrics.levenshtein import Levenshtein
lev = Levenshtein()


def pwd_str(pwd, char_dict, g):
    i = 0
    str_pass = ""
    while len(pwd[i: i+g]) == g:
        char = pwd[i: i+g]
        try: 
            char_cho = random.choice(char_dict[char])
            jump = len(char)
        except: 
            char_cho = char
            jump = len(char_cho)
        
        str_pass = str_pass + char_cho
        i+=jump
    
    str_pass = str_pass + pwd[i: i+g]
    str_pass = str_pass.replace(" ", "")
    return str_pass



def gen_password(pwd, char_dict, g, lim = 3):
    if g <= lim:
        new_pass = gen_password(
            pwd_str(pwd, char_dict, g + 1),
            char_dict,
            g + 1
        )
        return new_pass
    else:
        return pwd


def middle(n):
    return n[-1]

def sort(list_of_tuples):
    return sorted(list_of_tuples, key = middle)



def get_pass_groups(results, pwd):
    results = list(dict.fromkeys(results))

    suggestions = []

    for sug_pass in results:
        data_point = (sug_pass, lev.similarity(pwd, sug_pass))

        suggestions.append(data_point)

    suggestions = sort(suggestions)[:3]

    return suggestions


