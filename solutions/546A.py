n = int(input())
chapters = []

for i in range(n):
    chapter = list(map(int, input().split()))
    chapters.append(chapter)
    
k = int(input())

def read(chapter):
    if k > chapter[1]:
        return 0
    return 1

print(sum(map(read, chapters)))