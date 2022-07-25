FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf /etc/nginx/nginx.conf

# Replace with our own nginx.conf
#configs will include everything from /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf

#add the govt server configs
# the server block will be in this file
COPY govtnginx.conf /etc/nginx/conf.d/

