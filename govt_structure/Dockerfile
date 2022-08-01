# Dockerfile for govt_structure container image
# Enable access to red hat container register
FROM ubi8/python-38
LABEL description="This is govt structure application container image"

#user user 0 to create directories and a new user
USER 0

#working dir
ENV APP_DIR /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#Copy files from working directory to container file system
COPY . ${APP_DIR}

#switch to working directory
WORKDIR ${APP_DIR}

#configure image with the app user and correct permissions
#create directory where the application will stay
#Finally install pipenv and python dependecies to run the app
RUN groupadd -r appuser -f -g 1002 && \
    adduser -u 1002 -r -g appuser -m -s /sbin/nologin -c "App user" appuser && \
    chown -R appuser:appuser ${APP_DIR} && \
    chmod -R 755 ${APP_DIR} && \
    pip3 install pipenv && \
    pipenv install --system --deploy

#User who will be running the application; Best practice to use a different user other than root
USER appuser

EXPOSE 8000
#Entrypoint specifies default command to execute when the image runs
ENTRYPOINT [ "/app/appentry.sh" ]
