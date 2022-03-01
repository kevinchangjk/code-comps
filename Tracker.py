# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:36:33 2021

@author: Kevin Chang

Project: Codeforces Problem Tracker

"""

from collections import Counter

all_solved = []

class solved:
    
    def __init__(self, nrid, tags, difficulty):
        self.nrid = nrid
        self.tags = tags
        self.difficulty = difficulty
        all_solved.append(self)
        
def tag_counter(problemset):
    all_tags = []
    for problem in problemset:
        all_tags.extend(problem.tags)
    return Counter(all_tags)

def difficulty_counter(problemset):
    all_difficulty = [problem.difficulty for problem in problemset]
    print(f"Average Difficulty: {sum(all_difficulty)/len(all_difficulty)}")
    return Counter(all_difficulty)

def print_count(caption, count):
    print(caption)
    print("\n")
    for item in count:
        print(f"{item}: {count[item]}")
    print("\n")
    return 0
    
_1551A = solved("1551A", ["greedy", "math"], 800)
_1551B = solved("1551B", ["greedy", "strings"], 800)
_1541A = solved("1541A", ["constructive algorithms", "greedy", "implementation"], 800)
_1554A = solved("1554A", ["greedy"], 800)
_1557A = solved("1557A", ["brute force", "math", "sortings"], 800)


print_count("Tags of Solved Problems", tag_counter(all_solved))
print_count("Number of Solved Problems", difficulty_counter(all_solved))
        