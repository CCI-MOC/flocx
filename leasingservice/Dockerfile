FROM python:3-alpine

MAINTAINER Sahil Tikale

COPY leasingService /leasingService/leasingService
COPY setup.py /leasingService

WORKDIR /leasingService

#RUN pip install -r requirements.txt

RUN pip install -e .
WORKDIR /leasingService/leasingService

CMD ["python", "rest.py"]
