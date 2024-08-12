FROM python:3.11.0

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt
    
COPY . .

RUN groupadd -r appuser && useradd -r -g appuser appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "python /app/projet01/manage.py runserver 0.0.0.0:8000"]
