"""make_questions.py - Generate questions for Alexa trivia game"""
import csv
import numpy as np
import pandas as pd

SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme.
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix

"""
{
    "Is this a question?": [
        "Horse",
        "Fox",
        "Beaver",
        "Bear",
        "Racoon",
        "Groundhog"
    ]
},
"""

if __name__ == '__main__':
    # import sys
    # orig_stdout = sys.stdout
    # q = open('questions.json', 'a')
    # sys.stdout = q
    df = pd.read_csv('stations.csv', names=['num', 'names'])
    nums = df.num
    stations = df.names
    quesions = {}
    with open('questions.json', 'w') as f:
        writer = csv.writer(f)
        f.write('"{ QUESTIONS_EN_US" : [')
        for n, s in zip(nums, stations):
            others = list(stations)
            others.remove(s)
            wrongs = list(np.random.choice(others, size=3, replace=False))
            options = [s] + wrongs
            f.write('{')
            f.write('"What is the {} station?": '.format(ordinal(n + 1)))
            # print(options)

            f.write(str(options))
            f.write('}, ')
        f.write(']}')


        # for i, station in enumerate(choices):
            # print('{', file=q)
            # print('"What is the', ordinal(i + 1), 'station?": ', file=q)

            # less = list(choices)
            # less.remove(station)
            # others = list(np.random.choice(less, size=3, replace=False))
            # print(station)
            # print(others)
            # fours = [station]
            # fours = fours + others
            # fours = [f.replace('\n','') for f in fours]
            # print(fours)
            # print('},')

    # sys.stdout = orig_stdout
    # q.close()
