def get_max_nested(data):
    """
    Recursively finds the maximum numerical value in a deeply nested structure 
    containing dictionaries, lists, integers, and floats.
    """
    max_val = float('-inf')

    if isinstance(data, dict):
        for value in data.values():
            max_val = max(max_val, get_max_nested(value))
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            max_val = max(max_val, get_max_nested(item))
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        max_val = data

    return max_val


# --- Example Usage ---
nested_dict = {
    "a": 10,
    "b": {
        "c": 45,
        "d": [12, 99, {"e": 200}],
        "f": -50
    },
    "g": {"h": 88},
    "is_active": True  # Booleans are excluded automatically
}

highest_number = get_max_nested(nested_dict)
print(f"Highest number: {highest_number}")  # Output: 200