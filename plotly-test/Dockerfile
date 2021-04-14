FROM nginx:1.19.6 as target
COPY nginx.conf /etc/nginx/nginx.conf
COPY src /usr/share/nginx/html
ENV USER=65534
RUN chown -R $USER:$USER /usr/share/nginx/html && chmod -R 755 /usr/share/nginx/html && \
        chown -R $USER:$USER /var/cache/nginx && \
        chown -R $USER:$USER /var/log/nginx && \
        chown -R $USER:$USER /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R $USER:$USER /var/run/nginx.pid

