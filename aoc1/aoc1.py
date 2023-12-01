import re

global_ans=0

def find_first_and_last(s): 
    integers = re.findall(r'\d+', s)
    ans = int(integers[0][0] + integers[-1][-1])
    return ans

def replace_words(s): 
    replacements = {'one': 'o1e', 'two': 't2o', 'three': 'th3ee', 'four': 'fo4r', 'five': 'fi5e', 'six': 's6x', 'seven': 'se7en', 'eight': 'ei8ht', 'nine': 'ni9e'}
    for word, replacement in replacements.items():
        s = re.sub(r'\b' + word + r'\b', replacement, s)
    return s

with open('test', 'r') as file: 
    for s in file: 
        s = replace_words(s)
        global_ans += find_first_and_last(s)

print(global_ans)
