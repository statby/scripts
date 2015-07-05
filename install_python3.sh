#!/bin/bash

if [ $UID != "0" ] #&& exit || echo "Please use sudo !" 
  then
    echo "Please use sudo !"
fi

function fixcode (){
echo "Installing environment !"
yum -y install readline* zlib zlib-devel openssl openssl-devel  >/dev/null 2>&1

}

function installpython (){
mkdir -p /opt/download
cd /opt/download
[ -e Python-3.4.3.tgz  ] && rm -rf  Python-3.4.3.tgz||wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz >/dev/null 2>&1
echo "Downloading python3 !"
wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz >/dev/null 2>&1
tar -zxf Python-3.4.3.tgz
cd Python-3.4.3
echo "Compiling python3"
./configure --prefix=/usr/local/python34  >/dev/null 2>&1 ;make >/dev/null  2>&1 &&make install  >/dev/null 2>&1
ln -s /usr/local/python34/bin/python3 /usr/bin/python3
}

fixcode
installpython

version=`/usr/bin/python3 --version  2>/dev/null|awk '{print $2}'`
if [ $version = "3.4.3" ]
  then
    echo "python3 is successful install !"
  else
    echo "Something wrong is happen, check it out !"
fi
