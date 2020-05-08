FROM python:3
RUN pip install pycurl
ADD sample.py /
CMD [ "python", "./sample.py" ]

