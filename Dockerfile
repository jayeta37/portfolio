FROM python:3.12

WORKDIR /portfolio

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app" ]