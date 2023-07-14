from datetime import datetime

def extract_list(list_string):
    return list_string.strip("[]").replace("'", "").split(", ")

def formatDate(dBYdate):
    return datetime.strftime(datetime.strptime(dBYdate, "%d. %B %Y"), "%Y-%m-%d")
