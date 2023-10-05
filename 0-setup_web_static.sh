#!/usr/bin/env bash
#sets up my web servers for the deployment
# Install Nginx if it's not already installed
if ! command -v nginx &> /dev/null
then 
    sudo apt update
    sudo apt-get -y install nginx
fi
#create files
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/ 
sudo touch data/web_static/releases/test/index.html

#create test HTML file
echo "<html><body><h1>AirBnB clone</h1></body>" > data/web_static/releases/test/index.html 
#create sympolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#restart nginx 
sudo service nginx restart
exit 0

        