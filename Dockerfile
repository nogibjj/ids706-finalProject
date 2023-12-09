# Stage 1: Build and install dependencies in a full Python image
FROM python:3.11 as builder

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install --user -r requirements.txt

# Stage 2: Copy the necessary files to a Distroless image
FROM gcr.io/distroless/python3

COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local

WORKDIR /app

EXPOSE 8080
CMD ["python", "app.py"]
