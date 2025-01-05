
# Use Python 3.13 as the base image
FROM python:3.13.1-slim

# Copy all files from "Docker Course" to /app directory
COPY . /app

# set the current working directory to /app (the one we created above)
WORKDIR /app

# Execute this command -> runs the app.py
CMD [ "python","app.py" ] 