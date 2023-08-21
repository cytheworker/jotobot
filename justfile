build:
    docker build -t jotobot:latest .
run:
    docker run --env-file .env jotobot:latest