FROM python:3.11

WORKDIR /app
COPY personal_finance ./personal_finance
COPY scripts ./scripts
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "scripts/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
