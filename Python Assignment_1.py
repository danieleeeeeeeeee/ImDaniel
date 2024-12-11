#Q_1

def is_eligible_for_award(grade: float, req_grade: float) -> bool:
    if grade >= req_grade:
        return True
    else:
        return False


#Q_2
def is_yes(msg: str) -> bool:
    msg = msg.lower()
    
    if len(msg) >= 2 and msg[1] == 'y' and msg[2] in 'aeiou':
        return True
    else:
        return False


# Q_3
def contains_x(msg: str) -> bool:
    if 'x' in msg.lower():
        return True
    else:
        return False
