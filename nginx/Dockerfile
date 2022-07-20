FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf /etc/nginx/nginx.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

#add the govt server configs
COPY govtnginx.conf /etc/nginx/conf.d/

