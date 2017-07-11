FROM python:2.7
ADD ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
ADD . .
EXPOSE 8050
CMD ["python", "gdoc_slider.py"]
