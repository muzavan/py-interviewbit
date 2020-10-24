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

def getExtByLanguage(lang):
    if lang.startswith('C '):
        return 'c'
    if lang.startswith('C++'):
        return 'cpp'
    if lang.startswith('Python'):
        return 'py'
    # don't forget to put this before Java
    if lang.startswith('Javascript'):
        return 'js'
    if lang.startswith('Java'):
        return 'java'
    if lang.startswith('Ruby'):
        return 'rb'
    if lang.startswith('Objective-C'):
        return 'm'
    if lang.startswith('C#'):
        return 'cs'
    if lang.startswith('GO'):
        return 'go'
    if lang.startswith('Scala'):
        return 'scala'
    if lang.startswith('Swift'):
        return 'swift'
    if lang.startswith('PHP'):
        return 'php'
    
    print(f"unknown language! {lang}")
    return 'txt'

for t in topics:
    if t == 'time-complexity':
        # skip it, since it does not have code, only multiple choices
        continue

    print(f"topic {t} ...")
    # 2. get problems for all topics
    problems = ib.get_problems(t)

    # For storing purpose, dict[problem_name] -> [{code, language}]
    dct = {}


    for p in problems:
        if p['solved']:
            print(f"checking {t}/{p['name']} ...")

            #3. get code that already solved the problem
            solution = ib.get_solved_code(p['name'])

            if not solution['code']:
                # None means unsolved (or, for some reason it has different page structure)
                print(f"{t}/{p['name']} unsolved")
                continue 

            problem_name = p['name'].replace("-", "_")
            dct[problem_name] = solution
    
    # store in this repo as well
    parent_dir = '.'
    new_dir_path = t.replace("-", "_")
    new_dir_path = os.path.join(parent_dir, new_dir_path)

    os.mkdir(new_dir_path)

    for problem, solution in dct.items():
        code = solution['code']
        ext = getExtByLanguage(solution['language'])
        flname = f"{problem}.{ext}"
        flpath = os.path.join(new_dir_path, flname)

        with open(flpath, "w") as f:
            f.write(code)

    print(f"{t} done!")
    print()
    print()

print("all done!")





