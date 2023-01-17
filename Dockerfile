FROM python:3.11-alpine3.16

COPY req.txt /temp/req.txt 
COPY PhoneShop /PhoneShop
WORKDIR /PhoneShop
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/req.txt

RUN adduser --disabled-password linux-user

USER linux-user