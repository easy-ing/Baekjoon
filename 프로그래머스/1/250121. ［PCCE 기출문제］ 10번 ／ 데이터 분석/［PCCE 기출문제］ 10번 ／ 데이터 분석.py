def solution(data, ext, val_ext, sort_by):
    index = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    filtered_data = [
        row for row in data
        if row[index[ext]] < val_ext
    ]

    filtered_data.sort(key=lambda row: row[index[sort_by]])

    return filtered_data