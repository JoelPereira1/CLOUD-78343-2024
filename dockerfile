# FROM python:3.12
# # Or any preferred Python version.
# ADD main.py .
# RUN pip install requests beautifulsoup4 python-dotenv
# CMD ["python3", “./main.py”]
# # Or enter the name of your unique directory and parameter set.


FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/app/modules/databases:/app/modules/cosmosdb:/app/flaskshop:/app/models:/app/models/challenge:/app/models/community:/app/models/customer:/app/models/order:/app/models/product:/app/models/post:/app/packages"

WORKDIR /app/flaskshop
ENV FLASK_APP=/app/flaskshop/app.py
ENV FLASK_ENV=development
EXPOSE 5000

# CMD ["python", "/app/shop/app.py"]
CMD python -m flask run --host=0.0.0.0 --debug

# CMD [ "python", "-m flask run --debug" ]