setup:
	pipenv install --dev

# We add '-W ignore' here to hide the warnings
test:
	pipenv run python -W ignore -m pytest tests/

run:
	pipenv run python -m src.predict

docker-build:
	docker build -t agri-nova .

docker-run:
	docker run -it -p 9696:9696 agri-nova
