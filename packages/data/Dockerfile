FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt install -y python3.9 python3-pip wget

RUN mkdir /app

COPY --chmod=x setup.sh app/setup.sh
COPY requirements.txt app/requirements.txt

COPY scripts/ app/scripts

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "./setup.sh" ]

CMD [ "python", "python3" ]