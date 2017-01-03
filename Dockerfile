FROM python:3.5
MAINTAINER Johannes Gontrum <gontrum@me.com>

# Install the needed packages
RUN apt-get update
RUN apt-get install -y supervisor nginx

# Copy and set up the app
RUN mkdir /app
RUN pip install virtualenv
COPY . /app
RUN cd /app && make

# Configure nginx
RUN mv /app/config/nginx.conf /etc/nginx/sites-available/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf 

# Configure supervisor
RUN mv /app/config/supervisor.conf /etc/supervisor/conf.d/

EXPOSE 10010
CMD ["supervisord", "-n"]
