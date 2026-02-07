def validate_response(data):
    if isinstance(data, dict) and "error" in data:
        return False, data["error"]

    if not isinstance(data, list):
        return False, "Invalid response format"

    if len(data) == 0:
        return False, "Empty response"

    return True, "OK"
