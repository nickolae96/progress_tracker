FROM  python:3.11.3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /progress_tracker

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn progress_tracker.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000