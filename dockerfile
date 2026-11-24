FROM python:3.14

WORKDIR /app
COPY student.py .
CMD ["python","student.py"]