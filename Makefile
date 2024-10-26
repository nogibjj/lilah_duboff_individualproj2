install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py 
	
test:
	python -m pytest -vv test_main.py

check:
	python main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "Makefile git push"; \
	git push; \

deploy:
	#deploy goes here

extract: 
	python main.py extract

transform:
	python main.py transform

query: 
	python main.py query