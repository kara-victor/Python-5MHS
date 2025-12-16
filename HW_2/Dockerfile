FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-fonts-recommended && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir \
    -i https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple \
    latex-generator-karavictor==0.1.1

COPY build_pdf.py .
COPY sad.jpg .

CMD ["python", "build_pdf.py"]