def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for h in range(3, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            if (h - 2) * (w - 2) == yellow:
                return [w, h]