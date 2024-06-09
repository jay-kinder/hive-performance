FROM python:3.9
WORKDIR /app
RUN apt update && apt install netcat-traditional
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
