FROM python:3.7.6

RUN echo "fems_data"

WORKDIR /home/

RUN git clone https://github.com/jwtech05/fems_data.git

WORKDIR /home/양진이

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]