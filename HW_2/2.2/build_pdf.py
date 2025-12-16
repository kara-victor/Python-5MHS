import subprocess
from latex_generator import generate_table, generate_pic, generate_document


def build_pdf(tex_filename: str):
    try:
        subprocess.run(
            ["pdflatex", tex_filename],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        print("Ошибка при генерации PDF")
        print(e.stderr.decode("utf-8"))
        raise


data = [
    ["A", "B", "C", "D"],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

table = generate_table(data)
pic = generate_pic("sad.jpg")
latex = generate_document(table, pic)

tex_file = "result.tex"

with open(tex_file, "w", encoding="utf-8") as f:
    f.write(latex)

build_pdf(tex_file)
