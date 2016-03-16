#!/bin/bash

sudo yum install wget -y
sudo yum install epel-release -y

sudo yum install nodejs -y 

# install  Node.js Package Manager
sudo yum install npm -y

# install Node.js module Request

sudo npm install request

#forward requests from 80 to default Node.js port

sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3000
