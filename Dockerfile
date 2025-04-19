FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .
COPY boot.sh /boot.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy the entire app
COPY . .

RUN chmod +x /boot.sh

# Set environment variables, if needed
ENV ENV=production

# Command to run your app (modify as per your app structure)
CMD ["/boot.sh"]

