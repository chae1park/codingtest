# 동빈북 p.359 정렬 문제 23 국영수
# https://www.acmicpc.net/problem/10825


N = 12
score_list = []
score_list.append(list('Junkyu 50 60 100'.split()))
score_list.append(list('Sangkeun 80 60 50'.split()))
score_list.append(list('Sunyoung 80 70 100'.split()))
score_list.append(list('Soong 50 60 90'.split()))
score_list.append(list('Haebin 50 60 100'.split()))
score_list.append(list('Kangsoo 60 80 100'.split()))
score_list.append(list('Donghyuk 80 60 100'.split()))
score_list.append(list('Sei 70 70 70'.split()))
score_list.append(list('Wonseob 70 70 90'.split()))
score_list.append(list('Sanghyun 70 70 80'.split()))
score_list.append(list('nsj 80 80 80'.split()))
score_list.append(list('Taewhan 50 60 90'.split()))
# print(score_list)

# 숫자를 int형으로 바꿈
score_list = [[score[0], int(score[1]), int(score[2]), int(score[3]) ] for score in score_list]
sorted_score_list = sorted(score_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))
answers = [score[0] for score in sorted_score_list]
for answer in answers:
    print(answer)

