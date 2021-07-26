FROM python:3.7.6

RUN echo "fems00"

WORKDIR /home/

RUN git clone https://github.com/jwtech05/fems_data.git

WORKDIR /home/fems01

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 3000

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]