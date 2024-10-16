FROM python:3
# WORKDIR to folder w środku kontenera,
#w którym odbywa się praca podczas budowy kontenera
# !!!! KOMENTARZE NAD SPRAWĄ, KTÓREJ DOTYCZĄ!!!!
WORKDIR /usr/src/app
#kropka w docker oznacza TUTAJ TO ZRÓB!!!
COPY PapierKamienNozyce.py .
CMD [ "python", "./PapierKamienNozyce.py" ]
