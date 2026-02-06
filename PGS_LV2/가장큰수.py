def solution(numbers):
    str_numbers = [str(n) for n in numbers]
    str_numbers.sort(key=lambda x : x*3, reverse = 1)
    answer = ''.join(str_numbers)
    
    if str_numbers[0] == '0':
        return '0'
    
    return answer