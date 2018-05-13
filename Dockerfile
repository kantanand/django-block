FROM python:3
LABEL name="django-block"
LABEL version="1"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD [ "python run app.py 8000" ]
EXPOSE 8000