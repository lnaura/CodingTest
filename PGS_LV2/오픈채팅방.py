def solution(record):
    nicknames = {}
    logs = []
    for r in record:
        parts = r.split()
        command = parts[0]
        uid = parts[1]
        
        if command in ["Enter", "Change"]:
            nicknames[uid] = parts[2]
        
        if command in ["Enter", "Leave"]:
            logs.append((uid,command))
    
    answer = []
    for uid, command in logs:
        if command == "Enter":
            answer.append(f"{nicknames[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{nicknames[uid]}님이 나갔습니다.")

    return answer