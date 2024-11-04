#!/bin/bash


pkg update && pkg upgrade -y


pkg install -y wget build-essential libffi libffi-dev openssl openssl-dev zlib zlib-dev


wget https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tgz
tar -xf Python-3.11.6.tgz
cd Python-3.11.6


./configure --prefix=$PREFIX --enable-optimizations
make
make install


python3 --version
