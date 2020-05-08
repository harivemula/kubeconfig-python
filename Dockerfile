FROM python:2
RUN pip install pycurl
ADD sample.py /
CMD [ "python", "./sample.py" ]

