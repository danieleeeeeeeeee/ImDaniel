Q_4

def is_eligible_for_award_v2(gpa: float, major: str, req_gpa: float, req_major: str) -> bool:
    if gpa >= req_gpa and major == req_major:
        return True
    else:
        return False

Q_6

def check_names(lst: List [str]) -> bool:
    if "Alice" in lst or "Daniel" in lst or "Anthony" in lst or "Minsoo" in lst:
        return True
    else:
        return False

q_5
def get_row(board: List[List[str]], row_num: int) -> List[str]:
    return board[row_num]

