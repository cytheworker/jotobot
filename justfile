build:
    docker build -t cytheworker/jotobot:latest .
run:
    docker run --env-file .env cytheworker/jotobot:latest