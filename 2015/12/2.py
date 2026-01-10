"""
Given a JSON document, find sum of all the numbers that occur except in objects that contain "red"
"""

# -------
# imports
# -------

from json import load

# -------------------
# find obj sum no red
# -------------------

def find_obj_sum_no_red(obj):
    """
    Given a dict, list, string, or int, return the sum of all int-type vars contained
    """
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return 0
    if isinstance(obj, list):
        return sum(map(find_obj_sum_no_red, obj))
    if isinstance(obj, dict):
        return 0 if 'red' in obj.values() else sum(map(find_obj_sum_no_red, obj.values()))
    return 0

# -------------
# find json sum
# -------------

def find_json_sum(filepath):
    """
    Given a JSON file, return the sum of all numbers in the file
    """
    with open(filepath, encoding='utf-8') as file:
        obj = load(file)
        return find_obj_sum_no_red(obj)

# ----
# main
# ----

if __name__ == "__main__":
    print(find_json_sum('input'))
