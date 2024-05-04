#!/usr/bin/env bash
# Sets up nginx for web_static codebase deployment

sudo apt-get update && sudo apt-get -y  upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

conf_path="/etc/nginx/sites-available/default"
dir="location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
if ! grep -q "location /hbnb_static/" $conf_path
then
    sudo sed -i "s/^\tserver_name _;/\tserver_name _;\n\t$dir/" $conf_path
fi
sudo service nginx restart
