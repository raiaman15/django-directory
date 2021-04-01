FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/ssl-production/nginx/nginx.conf /etc/nginx/conf.d
COPY ./compose/ssl-production/nginx/domain_ssl_cert.pem /etc/ssl/domain_ssl_cert.pem
COPY ./compose/ssl-production/nginx/domain_ssl_private_key.key /etc/ssl/domain_ssl_private_key.key
