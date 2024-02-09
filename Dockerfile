FROM continuumio/miniconda3:latest

WORKDIR /app

COPY conda.yaml /app

RUN conda update -n base -c defaults conda
RUN conda env create -n venv -f conda.yaml

SHELL ["conda", "run", "-n", "venv", "/bin/bash", "-c"]

RUN echo "source activate venv" > ~/.bashrc

COPY . /app

CMD ["conda", "run", "-n", "venv", "python", "producer.py"]