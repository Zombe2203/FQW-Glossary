FROM node:18 AS react-build
WORKDIR /app/frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.10-slim AS fastapi-build
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./

RUN apt-get update && \
    apt-get install -y nginx

COPY --from=react-build /app/frontend/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8500
EXPOSE 80

CMD sh -c "python /app/initDatabase.py && uvicorn main:app --host 0.0.0.0 --port 8500 & nginx -g 'daemon off;'"