FROM continuumio/miniconda3:latest

WORKDIR /app

COPY conda.yaml /app

RUN conda update -n base -c defaults conda
RUN conda env create -n myenv -f conda.yaml

SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

RUN echo "source activate myenv" > ~/.bashrc

COPY . /app

CMD ["conda", "run", "-n", "myenv", "python", "producer.py"]