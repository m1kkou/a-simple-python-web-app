Dockerfile dev:

FROM python:3.9.6-alpine3.13 as dev

WORKDIR /work

Build and start our container:
docker build --target dev . -t python
docker run -it -v ${PWD}:/work python sh

huom! bind mount määritelty docker run skriptissä "-v" ${PWD} == nykyinen sijainti/kansio

Flask install from requirements.txt file:
pip install -r src/requirements.txt

huom! ajetaan kontainerin shellissä

Starting the minimal Flask app:
export FLASK_APP=src/app
flask run -h 0.0.0 -p 5000

huom! ajetaan kontainerin shellissä

Avataan portti kontista ulos:
exit
docker run -it -p 5000:5000 -v ${PWD}:/work python sh

#get our dependencies and start our application
pip install -r requirements.txt
export FLASK_APP=src/app
flask run -h 0.0.0 -p 5000
