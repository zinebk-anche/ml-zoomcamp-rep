# Customer Churn Prediction Service

This project trains and serves a customer churn prediction model. It uses a
scikit-learn logistic regression model with a `DictVectorizer`, exposes the
model through a Flask API, and packages the service with Docker and Gunicorn.

## Project Structure

```text
.
├── data-week-3.csv        # Training data
├── train.py               # Data preparation, validation, training, model export
├── model_C=1.0.bin        # Saved vectorizer and trained model
├── predict.py             # Flask prediction API
├── predict_test.py        # Example client request
├── customer.js            # Example customer payload
├── Pipfile                # Python dependencies
├── Pipfile.lock           # Locked dependency versions
└── Dockerfile             # Container build definition
```

## Architecture

```text
CSV data -> train.py -> model_C=1.0.bin -> predict.py -> Flask/Gunicorn API
```

The training script creates a serialized artifact containing both the feature
vectorizer and the trained model. The prediction service loads this artifact at
startup and uses it to score customer JSON payloads.

## Requirements

- Python 3.8
- Pipenv
- Docker, optional for containerized deployment

## Install Dependencies

```bash
pipenv install
```

Activate the environment:

```bash
pipenv shell
```

## Train the Model

Run:

```bash
python train.py
```

This reads `data-week-3.csv`, performs validation, trains the final model, and
writes the artifact to:

```text
model_C=1.0.bin
```

## Run the API Locally

Start the Flask app:

```bash
python predict.py
```

The service runs on:

```text
http://localhost:9696
```

The prediction endpoint is:

```text
POST /predict
```

Example response:

```json
{
  "churn_probability": 0.628,
  "churn": true
}
```

## Test the API

In another terminal, run:

```bash
python predict_test.py
```

This sends a sample customer payload to the running API and prints the
prediction response.

## Run with Docker

Build the image:

```bash
docker build -t churn-prediction .
```

Run the container:

```bash
docker run -it --rm -p 9696:9696 churn-prediction
```

Then test it with:

```bash
python predict_test.py
```

## Notes

- The Docker image copies only `predict.py` and `model_C=1.0.bin`, so the
  container is focused on serving predictions rather than retraining.
- The model artifact is loaded with `pickle`, so it should only come from a
  trusted source.
- The API currently assumes the input JSON contains all required customer
  fields.
