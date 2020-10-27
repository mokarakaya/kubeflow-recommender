FROM python:3
ADD my_script.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./entrypoint_script.py"]
