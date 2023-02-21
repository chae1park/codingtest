# 프로그래머스 코딩테스트 연습 > 2023 KAKO BLIND RECRUITMENT > 이모티콘 할인행사
# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product
def solution(users, emoticons):
    answer = []
    # 유저 최대 100명
    # 이모티콘 최대 7개
    # 비율 4개
    # 16,384 조합 * 100명 = 163,840
    # => 연산횟수가 충분히 적으므로 완전 탐색이 가능하겠다!고 판단 후 문제를 해결하였다.
    

    ##### 해당 문제에서는 부동소수점 관련 연산으로 아래와 같이 두가지 에러를 해결하였다.
    # 1. 아래 24번째 줄 off_prices 변수에서 int() 씌어주는 것을 뺐더니 에러가 해결되었다.
    # -> (100이상의 수 * 소수점 한자리수) 연산은 int()를 굳이 씌워줄 필요가 없이 연산이 잘되나보다.
    #    근데 이걸 int() 씌워줬다고 왜 오류가 생기는지까지는 아직 잘 모르겠다.
    # 2. user_buy_idx 변수에서 유저허용 할인율 vs. 이모티콘 할인율을 비교하는 연산에서 
    #    나누기 연산을 최대한 뒤로 빼는 방식으로 순서만 바꿨더니 한개의 에러를 해결할 수 있었다.
    ##### 소수점을 다룰 때 항상 부동소수점에 유의하도록 하자 !
     
    num_emo = len(emoticons)
    sale_ratio = [0.6, 0.7, 0.8, 0.9] # 40%, 30%, 20%, 10%
    ratio_emoticon = list(product(sale_ratio,repeat=num_emo))
    len_perm_emo = len(ratio_emoticon)
    max_plus_user = 0
    max_total_price = 0
    for ratio_emo in ratio_emoticon:
        off_prices = [(emoticons[i]*ratio_emo[i]) for i in range(num_emo)]
        # off_prices = [int(emoticons[i]*ratio_emo[i]) for i in range(num_emo)] # 이렇게 쓰면 13,15,18 case error
        
        plus_user = 0
        emo_total_price = 0
        for user_ratio, user_limit in users:
            user_buy_emo = 0
            # 할인율 비교해서 총 몇개 이모티콘 사는지 구하고
            user_buy_idx = [ idx for idx in range(num_emo) if  ( ratio_emo[idx] <= (100-user_ratio)/100 ) ]
            
            # 부동소수점 때문에 최대한 나누기 100같은 것을 뒤에 해줄 수록 좋다고 함. 위의 코드 대신 밑의 것을 사용하면 case 15 실패.
            # user_buy_idx = [ idx for idx in range(num_emo) if (user_ratio/100) <= (1 - ratio_emo[idx])]
            
            if user_buy_idx:
                user_buy_total = sum([off_prices[idx] for idx in user_buy_idx])
                # 그렇게 다 샀을때 금액을 넘으면 플러스 고객
                if user_buy_total >= user_limit:
                    plus_user += 1
                # 금액 안넘으면 해당 금액    
                else:
                    emo_total_price += user_buy_total
            else:
                # 아무것도 안사면 이 유저는 넘어감
                continue
    
        # 이모티콘 플러스 가입 유저가 많은 것을 선택
        if max_plus_user < plus_user:
            max_plus_user = plus_user
            max_total_price = emo_total_price
        # 이모티콘 플러스 가입 유저 수가 같다면 이모티콘 판매액이 큰 것을 선택
        elif max_plus_user == plus_user:
            if max_total_price < emo_total_price:
                max_plus_user = plus_user
                max_total_price = emo_total_price
        # 위 두 경우 이외는 그대로
        
    answer.append(max_plus_user)
    answer.append(max_total_price)
    return answer