FROM python:3

LABEL MAINTAINER SSDR "lib-ssdr@umd.edu"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY whpool-connect.py /app/whpool-connect.py

ENTRYPOINT [ "python" ]

CMD [ "whpool-connect.py" ]