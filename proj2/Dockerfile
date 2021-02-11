FROM python:3.6.8

MAINTAINER Your Name "nish"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt


ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]