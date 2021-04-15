#!/usr/bin/env bash
# Prepare for web static

sudo apt-get -y install nginx
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

printf "<html>
	    <head>
	    </head>
	    <body>
	    Holberton School
	    </body>
	</html>" > sudo tee /data/web_static/releases/test/index.html

FILE=/data/web_static/current

if [ -f "$FILE" ]
then
    sudo rm /data/web_static/current
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

sudo chgrp -R ubuntu /data/
sudo chown -R ubuntu /data/
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;
	location /hbnb_static/ {
		alias /data/web_static/current/;
		autoindex off;
	}
}" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
