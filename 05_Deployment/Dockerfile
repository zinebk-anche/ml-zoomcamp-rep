# Full code for building our docker image
# Specify base docker image
FROM python:3.8.11-slim

# Install Pipenv inside the image.
# Pipenv reads the Pipfile and Pipfile.lock files and installs the exact Python libraries needed by this project.
RUN pip install pipenv 

# Set /app as the working directory inside the container.
# The following line create a directory called /app if it doesn't exist and cd to it
# All following commands such as COPY, RUN, and CMD will run from this folder.
WORKDIR /app
# Copy only the dependency files first , "./" means copy to current directory .
COPY ["Pipfile", "Pipfile.lock", "./"]

#Because pipenv install will create a virtual environment in docker which we don't need
RUN pipenv install --system --deploy

COPY ["predict.py", "model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]