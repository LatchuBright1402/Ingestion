FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install sudo
RUN apt-get install -y python3.9
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install -y python3-pip
RUN apt-get install -y curl
RUN apt-get update
WORKDIR /ingestion
COPY ./ingestion.py .
COPY ./schemas.py .
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt
COPY . .
EXPOSE 5984
#CMD ["uvicorn", "ingestion:app", "--reload"]
CMD ["uvicorn", "ingestion.ingestion:app", "--host", "127.0.0.1", "--port", "8000" , "--reload"]



