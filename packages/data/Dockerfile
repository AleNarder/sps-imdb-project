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
COPY process.py app/process.py
COPY data_process_scripts/p_name_basics.py app/p_name_basics.py
COPY data_process_scripts/p_title_basics.py app/p_title_basics.py
COPY data_process_scripts/p_title_ratings.py app/p_title_ratings.py
COPY data_process_scripts/p_title_crew.py app/p_title_crew.py
COPY data_process_scripts/p_title_episode.py app/p_title_episode.py
COPY data_process_scripts/p_title_principals.py app/p_title_principals.py


WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "./setup.sh" ]

CMD [ "python", "python3" ]