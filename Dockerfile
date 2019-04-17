FROM python:3
RUN pip install numpy
RUN pip install quandl
RUN pip install python-dateutil
RUN pip install azure-eventhub
RUN mkdir /app
COPY gettsdata.py /app
COPY pushtsdata.py /app
WORKDIR /app
