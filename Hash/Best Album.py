### Programmers 문제
### 해쉬 - 베스트앨범

# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 장르별 최대 2곡까지 수록


def solution(genres, plays):
    answer = []
    least_num_song = 2
    # 1. 총 횟수가 든 장르 딕셔너리 생성
    genre_total = {genre: 0 for genre in list(set(genres))}
    for i in range(len(genres)):
        genre_total[genres[i]] += plays[i]
        
    # 2. 1의 딕셔너리를 내림차순 정렬
    genre_total = sorted(genre_total.items(), key=lambda x: -x[1])

    # 3. 장르 별 재생횟수가 개별로 들어있는 딕셔너리 생성
    genre_dict = {genre: [] for genre in list(set(genres))}
    for i in range(len(genres)):
        genre_dict[genres[i]].append((i, plays[i]))
        
    # 4. 3의 딕셔너리를 장르별로 재생횟수가 높은 순서대로 정렬
    for genre, plays in genre_total:
        for (idx, plays) in sorted(genre_dict[genre], key=lambda x: -x[1])[:least_num_song]:
            answer.append(idx)
    '''
    런타임 에러나는 코드! 
    다른점: 1) 장르에서 정렬하고 슬라이싱 안함  2)2회를 for문 쓰는건 똑같지만 이렇게해서 "이중인덱싱"함 
    
    for genre, plays in genre_total:
        genre_best_list = sorted(genre_dict[genre], key=lambda x: -x[1])
        for i in range(least_num_song):
            answer.append(genre_best_list[i][0])
    '''    
    
    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    output = solution(genres, plays)
    print(output)
    # expected output: [4, 1, 3, 0]