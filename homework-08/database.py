import os

DB_FILE = 'data.txt'

def init_db():
    if not os.path.isfile(DB_FILE):
        with open(DB_FILE, "w", encoding="UTF-8") as file:
            file.write('')

def get_all():
    with open(DB_FILE, "r", encoding="UTF-8") as file:
        return file.readlines()

def write_one_row(row):
    if row[-1] != "\n":
        row += "\n"
    with open(DB_FILE, "a", encoding="UTF-8") as file:
        file.write(row)

def overwrite_all_data(data):
    with open(DB_FILE, "w", encoding="UTF-8") as file:
        for row in data:
            if row[-1] != "\n":
                row += "\n"
            file.write(row)

def search_data(char):
    lst = get_all()
    found_rows = []
    for row in lst:
        if char in row:
            found_rows.append(row)
    if len(found_rows) > 0:
        return found_rows
    return False

def get_row_by_id(row_id, lst):
    for row in lst:
        if row_id == int(row[0]):
            return row
    return False

def get_new_id():
    lst = get_all()
    if lst:
        row = lst[-1]
        new_id = int(row.split(';')[0])
    else:
        new_id = 0
    return new_id + 1

def delete_row(row):
    lst = get_all()
    lst.remove(row)
    overwrite_all_data(lst)

def edit_row(row_id, num):
    lst = get_all()
    row = get_row_by_id(row_id, lst)
    key = lst.index(row)
    # if num == 1:

# def sort_by(row):
#     return row.split(';')[1]