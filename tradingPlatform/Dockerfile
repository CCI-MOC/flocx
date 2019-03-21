FROM python:3-alpine

MAINTAINER Sahil Tikale

COPY tradingPlatform /tradingPlatform/tradingPlatform
COPY setup.py /tradingPlatform

WORKDIR /tradingPlatform

#RUN pip install -r requirements.txt

RUN pip install -e .
WORKDIR /tradingPlatform/tradingPlatform

CMD ["python", "rest.py"]