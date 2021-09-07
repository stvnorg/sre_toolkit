FROM python:3.8-alpine3.13

WORKDIR /app
COPY requirements.txt .

COPY *.py /app/
COPY libs/*.py /app/libs/
COPY routers/*.py /app/routers/

RUN apk add build-base
RUN pip install -r requirements.txt

EXPOSE 8000

ENV APP_NAME "CHANGE_ME"
ENV DEPLOY_ENG "CHANGE_ME"
ENV AUTHOR "CHANGE_ME"

CMD ["uvicorn", "--host", "0.0.0.0", "main:app", "--reload"]

