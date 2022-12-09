def solution(array, commands):
    answer = []
    
    for command in commands:
        new_arr = sorted(array[(command[0]-1):(command[1])])
        ans = new_arr[command[2]-1]
        answer.append(ans)

    return answer