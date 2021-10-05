## The solution is to simply generate a test.ppm file ->
# P3 3 2
# 255
# 255 0 0 255 255 255 0 0 255
# 255 255 0 255 255 255 0 0 0

if __name__ == "__main__":
    n_rows = int(input())
    n_cols = int(input())
    first_row = f"P3 {n_rows} {n_cols}"
    with open(file="test_mera.ppm", mode="a") as file:
        file.write(first_row)
        file.writelines("\r\n255\r\n")

    for _ in range(n_cols):
        temp = ""
        for _ in range(n_rows):
            r, g, b = int(input()), int(input()), int(input())
            temp += f"{r} {g} {b} "
        with open(file="test_mera.ppm", mode="a") as file:
            temp += "\r\n"
            file.writelines(temp)
