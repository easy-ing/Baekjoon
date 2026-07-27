def solution(wallpaper):
    rows = []
    cols = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                rows.append(i)
                cols.append(j)

    lux = min(rows)
    luy = min(cols)
    rdx = max(rows) + 1
    rdy = max(cols) + 1

    return [lux, luy, rdx, rdy]