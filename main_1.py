from latex_table import generate_table


data = [
    ["A", "B", "C", "D"],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def get_latex_file(latex):
    latex = f"\\documentclass{{article}} \n\\begin{{document}}\n" + latex + f"\\end{{document}}"
    with open("table.tex", "w") as f:
        f.write(latex)


if __name__ == '__main__':
    latex_str = generate_table(data)
    get_latex_file(latex_str)
