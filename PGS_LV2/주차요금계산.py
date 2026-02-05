import math

def solution(fees, records):
    std_min, std_fee, unit_min, unit_fee  = fees
    
    parking_time = {}
    
    in_time = {}

    for record in records:
        time, car_num, io = record.split()
        h, m = map(int,time.split(":"))
        minutes = h * 60 + m
        
        if io == "IN":
            in_time[car_num] = minutes
        else:
            duration = minutes - in_time.pop(car_num)
            parking_time[car_num] = parking_time.get(car_num,0) + duration
    
    end_of_day = 23 * 60 + 59
    for car_num, start_time in in_time.items():
        duration = end_of_day - start_time
        parking_time[car_num] = parking_time.get(car_num,0) + duration
    
    answer = []
    for car_num in sorted(parking_time.keys()):
        total_min = parking_time[car_num]

        if total_min > std_min:
            f = math.ceil((total_min - std_min) / unit_min) * unit_fee + std_fee
            answer.append(f)
        else:
            answer.append(std_fee)

    return answer