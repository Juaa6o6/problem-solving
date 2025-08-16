N, K = map(int, input().split())

student = {}

for i in range(N):
    S, Y = input().split()
    if S == '0':
        S = '남'
        Y = Y+S
    else:
        S = '여'
        Y = Y+S

    student[Y] = student.get(Y, 0) + 1

Sum = 0
for i in range(1, 7):
    m_st = student.get(str(i)+'남', 0)
    w_st = student.get(str(i)+'여', 0)

    # 학년, 성별 별로 K 로 나눠서 나머지가 0이면 몫 = 방 개수, 0이 아니면 몫 + 1
    if m_st % K == 0:
        Sum += m_st//K
    else:
        Sum += m_st//K + 1

    if w_st % K == 0:
        Sum += w_st//K
    else:
        Sum += w_st//K + 1

print(Sum)