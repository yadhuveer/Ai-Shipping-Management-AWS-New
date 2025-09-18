# Step 1: Base image
FROM python:3.11-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Install system dependencies (if needed for numpy, pandas, sklearn, etc.)
RUN apt-get update && apt-get install -y build-essential

# Step 4: Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project files
COPY . .

# Step 6: Expose FastAPI port
EXPOSE 9000

# Step 7: Start FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
