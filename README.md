# Django 1
test django app with docker and docker compose

### run stack
```Bash
# build docker images
docker-compose build
# up services
docker-compose up -d
```

### Services
- **web-service** depends of:
    - **database**
    - ws-**migrations** depends of:
        - **database**
    - ws-**create-superuser**  depends of:
        - **database**
        - ws-**migrations**
