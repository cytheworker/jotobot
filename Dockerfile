FROM python:3.11-slim-bookworm
WORKDIR /jotobot

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY jotobot jotobot
CMD ["poetry", "run", "python3", "-m", "jotobot"]