def is_valid_int(value):
    try:
        int(value)
        return True
    except:
        return False

def is_valid_float(value):
    try:
        float(value)
        return True
    except:
        return False

def is_valid_date(value):
    from datetime import datetime
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except:
        return False
