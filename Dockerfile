FROM python:3.6
ADD . /myretail-api
WORKDIR /myretail-api
RUN pip install -r requirements.txt && pip install /myretail-api/
