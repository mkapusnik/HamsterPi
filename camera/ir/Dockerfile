FROM arm32v6/python:3.10-alpine
WORKDIR /app
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ir.py .
CMD ["python", "./ir.py"]