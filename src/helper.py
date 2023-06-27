def extract_list(list_string):
    return list_string.strip("[]").replace("'", "").split(", ")
