FROM python:3.9-slim

# set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the necessary files to install dependencies
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry with the settings most suitable for the build environment
RUN poetry config virtualenvs.create false

# Install only the package dependencies using Poetry
RUN poetry install --no-dev

# Copy the current directory contents into the container at /app
COPY . /app

# make port 8000 available to the world outside this container
EXPOSE 8000

# run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
