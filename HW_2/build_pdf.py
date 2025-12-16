from latex_generator import generate_table, generate_pic, generate_document

data = [
    ["A", "B", "C", "D"],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

table = generate_table(data)
pic = generate_pic("sad.jpg")

latex = generate_document(table, pic)

with open("result.tex", "w", encoding="utf-8") as f:
    f.write(latex)
