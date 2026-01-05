FROM python:3.9-slim

WORKDIR /app

# Force install libraries directly (Bypasses the Pipenv hang)
RUN pip install --no-cache-dir \
    pandas \
    scikit-learn \
    xgboost \
    flask \
    gunicorn \
    pydantic

# Copy your Professional folders
COPY ["src", "./src"]
COPY ["models", "./models"]

# Expose port
EXPOSE 9696

# Point to the new location of the app
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "src.predict:app"]