FROM python:3.11

WORKDIR /app

# source code
COPY personal_finance ./personal_finance
COPY scripts ./scripts

# dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# database connection
COPY .pg_pass .pg_pass
RUN chmod 0600 .pg_pass

# network
EXPOSE 8000

# execution
ENTRYPOINT ["python", "scripts/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
