FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /ticket_app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY / .

RUN mkdir -p /vol/web/
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/database


# RUN adduser -D -G user
# RUN chown -R user  /vol
# RUN chmod -R 755 /vol/web
# USER user

# CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8080

# EXPOSE 8080