import sys

for _ in range(int(input())):
    ox = sys.stdin.readline().rstrip()
    score = 0
    sum_sore = 0
    for i in ox:
        if i == 'X':
            sum_sore = 0
            continue
        sum_sore += 1
        score += sum_sore

    sys.stdout.write(f'{score}\n')