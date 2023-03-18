FROM python:3.9-slim-buster
WORKDIR /usersopenapi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "-m", "api.spec.v1.openapi_server"]
