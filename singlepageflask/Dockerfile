#FROM python:3.11.0b4-alpine3.16
FROM ubi8/python-38

#working dir
ENV APP_DIR /app

#Copy files from working directory to container file system
COPY . ${APP_DIR}

ADD 
#switch to working directory
WORKDIR ${APP_DIR}

#RUN ls -l appentry.sh
#RUN pwd
#RUN ./appentry.sh

#user user 0 to change directories permissions and adding new user
USER 0

#Finally install pipenv and python dependecies to run the app
RUN groupadd -r appuser -f -g 1002 && \
    adduser -u 1002 -r -g appuser -m -s /sbin/nologin -c "App user" appuser && \
    chown -R appuser:appuser ${APP_DIR} && \
    chmod -R 755 ${APP_DIR} && \
    pip3 install pipenv && \
    pipenv install --system --deploy

#set created user to be used in the container
USER appuser

#expose container port 8000
EXPOSE 8000

#Run script to start gunicorn wsgi server
ENTRYPOINT ["/app/appentry.sh"]
