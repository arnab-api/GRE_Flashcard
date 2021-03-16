import json
import numpy as np
from collections import deque
import random
from PyDictionary import PyDictionary


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print(f"{bcolors.HEADER}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.OKBLUE}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.ENDC}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.HEADER}{bcolors.BOLD}Warning: No active frommets remain. Continue?{bcolors.ENDC}{bcolors.ENDC}")
# print(f"{bcolors.UNDERLINE}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

def save_logs(log, que, new_word):
    print(f"{bcolors.OKBLUE}SAVING LOG ..... {bcolors.ENDC}")
    while(len(que) != 0):
        nxt = que.pop()
        word = nxt[1]
        if(word in new_word):
            log[word] = random.randint(999, 9999)

    with open("logger.json", "w") as f:
        json.dump(log, f)

    print(f"{bcolors.OKBLUE}SAVED SUCCESSFULLY{bcolors.ENDC}")



with open("word_list.json") as lst:
    wrr = json.load(lst)
    print(wrr)

with open("logger.json") as f:
    log = json.load(f)
    print(log, type(log))

wrr = wrr[0:-1]
random.shuffle(wrr)
print(wrr)

new_word = []
for word in wrr:
    if word not in log:
        log[word] = random.randint(999, 9999)
        new_word.append(word)
    elif(log[word] >= 999):
        log[word] = random.randint(999, 9999)
        new_word.append(word)

que = deque()
for word in wrr:
    que.append((log[word], word))

que = deque(sorted(que))
dictionary = PyDictionary()
while(len(que) != 0):
    nxt = que.popleft()
    word = nxt[1]
    if(log[word] >= 999):
        log[word] = 1
    else:
        log[word] += 1

    print(f"{bcolors.WARNING}{bcolors.BOLD}{word}{bcolors.ENDC}{bcolors.ENDC}", end = "")
    fb = input()
    meaning = dictionary.meaning(word)
    print(f"{bcolors.OKGREEN}{nxt}: , {meaning}{bcolors.ENDC}")
    # syn = dictionary.synonym(nxt)
    # print(syn)
    # ant = dictionary.synonym(nxt)
    # print(ant)
    print(f"{bcolors.HEADER}===> did you get it right??  -{bcolors.ENDC}", end = "")
    fb = input()
    if(fb == "y"):
        continue
    elif(fb == "end"):
        break
    que.append(nxt)

save_logs(log, que, new_word)