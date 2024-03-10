FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy project
COPY . /app/

# Command to run the application
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]