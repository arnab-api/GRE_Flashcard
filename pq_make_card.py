import json
import numpy as np
from collections import deque
import random
from PyDictionary import PyDictionary
from queue import PriorityQueue
from termcolor import cprint

def save_logs(log, que, new_word):
    cprint("SAVING LOG ..... ", color="blue", attrs=["bold"])
    while(not que.empty()):
        nxt = que.get()
        word = nxt[1]
        if(word in new_word or nxt[0] <= -999):
            log[word] = random.randint(999, 9999)

    with open("barron_logger.json", "w") as f:
        json.dump(log, f)

    cprint("SAVED SUCCESSFULLY", color="green", attrs=["bold"])
 

with open("barron333_missed.json") as lst:
    wrr = json.load(lst)
    print(wrr)

with open("barron_logger.json") as f:
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


que = PriorityQueue()
for word in wrr:
    que.put((-log[word], word))

dictionary = PyDictionary()


try_count = {}
while(not que.empty()):
    nxt = que.get()
    word = nxt[1]
    if(word not in try_count):
        try_count[word] = 1
    else:
        try_count[word] += 1

    cprint(word, color="yellow", attrs=["bold","underline"] , end = "  ")

    fb = input()
    meaning = dictionary.meaning(word)

    cprint(meaning, color="green")
    
    # syn = dictionary.synonym(nxt)
    # print(syn)
    # ant = dictionary.synonym(nxt)
    # print(ant)
    cprint("===> did you get it right??  -", color="cyan" , end = "  ")
    
    fb = input()
    if(fb == "y"):
        log[word] = try_count[word]
        cprint("OK", color="green", attrs=["bold"])
        continue
    elif(fb ==  "end"):
        break

    nxt = (-random.randint(999, 9999), nxt[1])
    que.put(nxt)
    cprint("try to get it right next time" , color = "magenta")

save_logs(log, que, new_word)