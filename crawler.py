from ibit import InterviewBit
import json
import os
from time import sleep

SLEEP_TIME = 1 # to make sure the request is not rate limited

conf = {}
with open('config.json', 'r') as f:
    conf = json.load(f)

ib = InterviewBit(conf.get('cookie', ''))

# crawl all my previous solved codes
# 1. get all topics
topics = ib.get_programming_topics()

for t in topics:
    if t == 'time-complexity':
        # skip it, since it does not have code, only multiple choices
        continue

    # 2. get problems for all topics
    problems = ib.get_problems(t)

    # For storing purpose, dict[problem_name] -> [solution]
    dct = {}

    for p in problems:
        print(f"checking {t}/{p} ...")
        #3. get code that already solved the problem
        code = ib.get_solved_code(p)

        if not code:
            # None means unsolved (or, for some reason it has different page structure)
            print(f"{t}/{p} unsolved")
            continue 

        problem_name = p.replace("-", "_")
        dct[problem_name] = code
    
    # store in this repo as well
    parent_dir = '.'
    new_dir_path = t.replace("-", "_")
    new_dir_path = os.path.join(parent_dir, new_dir_path)

    os.mkdir(new_dir_path)

    for problem, code in dct.items():
        flname = f"{problem}.py"
        flpath = os.path.join(new_dir_path, flname)

        with open(flpath, "w") as f:
            f.write(code)

    print(f"{t} done!")
    print()
    print()

print("all done!")





