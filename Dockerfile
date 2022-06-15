FROM python:3.9
WORKDIR /scraper
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .