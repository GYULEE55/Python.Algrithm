from collections import Counter
def solution(participant, completion):
    counter = Counter(participant)  # {'mislav': 2, 'stanko': 1, 'ana': 1}
    
    for name in completion:
        counter[name] -= 1          # 완주한 사람 하나씩 빼기
    
    for name, count in counter.items():
        if count > 0:              
            return name
