FROM python:3
ADD entrypoint_script.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./entrypoint_script.py"]
