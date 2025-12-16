def generate_table(data):
    count_rows = len(data)
    count_columns = len(data[0])
    latex_str = f"\\begin{{tabular}}{{|{'c|' * count_columns}}} \\hline\n"
    for i in range(count_rows):
        for j in range(count_columns):
            if j == 0:
                latex_str += f"{data[i][j]} "
            else:
                latex_str += f"& {data[i][j]} "
        latex_str += f"\\\\ \\hline\n"
    latex_str += f"\\end{{tabular}}\n"
    return latex_str
