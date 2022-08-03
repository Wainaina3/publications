# singlepageflask
This is single page flask application which have just one endpoint "/jokeme". The end point returns
a random dad joke each time its called. 

It's using gunicorn as wsgi server and can be started by running the appentry.sh script locally.
As a container, use the Dockerfile to build image. Dockerfile will pull the application files from this git branch.

Remember to expose the container by mapping host with container port 8000.
If you are using podman, you can test it locally by below command;

$ git clone -b singleflask --single-branch https://github.com/Wainaina3/publications.git
$ cd singlepageflask
$ podman build -t singlepage .
$ podman run -d -p 8000:8000 --name singlepage singlepage

Test the endpoint;

$ curl http://localhost:8000/jokeme
