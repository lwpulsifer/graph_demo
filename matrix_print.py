def print_matrix(matrix, row_spacing=0, col_spacing=6, blank_character="-"):
    if not matrix: return
    num_cols = len(matrix[0])
    header_row = " "  * col_spacing + " " + " ".join([f"{i:>{col_spacing}}" for i in range(num_cols)])
    print(header_row)
    print(blank_character * len(header_row))
    for i, row in enumerate(matrix):
        for _ in range(row_spacing):
            print()
        print(f"{i:{col_spacing - 1}}|", " ".join([f"{(val if val else '-'):>{col_spacing}}" for val in row]))

if __name__ == "__main__":
    print_matrix([])