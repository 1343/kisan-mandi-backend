
def is_correct_type(check_type, data):
    """This method is to check the type of input data"""
    if check_type == 'list':
        if not isinstance(data, list):
            return True
    elif check_type == 'str':
        if not isinstance(data, str):
            return True
    elif check_type == 'int':
        if not isinstance(data, int):
            return True
    return False


def validate(data, conditions):
    """This method checks whether provided fields match given condition"""
    error = {}
    for field, condition in conditions.items():
        line_errors = ""
        for checker in condition.split("|"):
            if checker == "NNULL":
                if field not in data or data[field] == "":
                    line_errors = "Null Value"
                    break
            elif "TYPE" in checker:
                check_type = checker[4:]
                if is_correct_type(check_type, data[field]):
                    line_errors = "Invalid Type"
                    break
            elif "IN" in checker:
                check_type = checker[2:]
                user_type = ["farmer", "merchant"]
                if check_type == "status":
                    if data[field] not in user_type:
                        line_errors = "Invalid Input"
                        break
        if line_errors:
            error[field] = line_errors
    return error
