#!/bin/python3

import os


# Complete the birthday function below.
def birthday(s, d, m):
    cnt = 0
    q = s[:m - 1]
    for i in s[m - 1:]:
        q.append(i)
        if sum(q) == d:
            cnt += 1
        q.pop(0)
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
