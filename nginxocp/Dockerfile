FROM registry.access.redhat.com/ubi9/nginx-120
#Set labels used in OpenShift to describe the image
LABEL io.k8s.description="This is a Nginx image configured to act as reverse proxy for govtapplication" \
     io.k8s.display-name="Nginx Govt reverse proxy image" \
     io.openshift.expose-services="8181:http" \
     io.openshift.tags="nginx,proxy,govt"

# Add application sources
ADD nginx.conf "${NGINX_CONF_PATH}"
ADD nginx-default-cfg/*.conf "${NGINX_DEFAULT_CONF_PATH}"
ADD nginx-cfg/*.conf "${NGINX_CONFIGURATION_PATH}"
#Unnecessary html files. Can be ommited
ADD *.html ./
#Nginx reverse proxy will listen on port 8181
EXPOSE 8181
# Run script uses standard ways to run the application
CMD nginx -g "daemon off;"