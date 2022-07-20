#! /bin/bash

## create images using Dockerfile in govt structure and nginx

podman build -t quay.io/wainaina3/govt /govt_structure/.

podman build -t quay.io/wainaina3/nginxgovt /nginx/.
# <<< creating containers in a pod podman >>>
##create a pod and expose on port 8080
podman pod create -n govtstructurenginx -p 8080:8080
##create a govt_structure container using govt latest image and attach it to the pod
podman run -d --name govtstructure --pod govtstructurenginx govt:latest

##create nginx container using nginx image and attach to the pod.
podman run -d --name nginx --pod govtstructurenginx nginxgovt:latest
