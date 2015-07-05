#!/bin/bash

if [ $UID != "0" ] #&& exit || echo "Please use sudo !" 
  then
    echo "Please use sudo !"
fi

function fixcode (){
echo "Installing environment !"
yum -y install readline* zlib zlib-devel openssl openssl-devel gcc libxslt-devel libxml2-devel >/dev/null 2>&1  
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
ln -s /usr/local/python34/bin/python3 /usr/bin/python3 >/dev/null 2>&1
}

function installsetuptools (){
mkdir -p /opt/download
cd /opt/download
[ -e setuptools-18.0.1.tar.gz   ] && rm -rf  setuptools-18.0.1.tar.gz ||wget https://pypi.python.org/packages/source/s/setuptools/setuptools-18.0.1.tar.gz >/dev/null 2>&1
echo "Downloading setuptools !"
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-18.0.1.tar.gz >/dev/null 2>&1
tar -zxf setuptools-18.0.1.tar.gz
cd setuptools-18.0.1
echo "Installing setuptools-18.0.1"
python3 setup.py install >/dev/null 2>&1
}

function installpip (){
mkdir -p /opt/download
cd /opt/download
[ -e pip-7.0.3.tar.gz   ] && rm -rf  pip-7.0.3.tar.gz ||wget https://pypi.python.org/packages/source/p/pip/pip-7.0.3.tar.gz  >/dev/null 2>&1
echo "Downloading pip-7.0.3 !"
wget https://pypi.python.org/packages/source/p/pip/pip-7.0.3.tar.gz  >/dev/null 2>&1
tar -zxf pip-7.0.3.tar.gz
cd pip-7.0.3
echo "Installing pip-7.0.3"
python3 setup.py install >/dev/null 2>&1
ln -s /usr/local/python34/bin/pip3 /usr/bin/pip3 >/dev/null 2>&1
}



function py3ok (){
version=`/usr/bin/python3 --version  2>/dev/null|awk '{print $2}'`
if [ $version = "3.4.3" ]
  then
    echo "python3 is successful install !"
  else
    echo "Something wrong is happen, check it out !"
fi
}

function pip3ok (){
/usr/bin/pip3 -V >/dev/null 2>&1
if [ $? -eq "0" ]
  then
    echo "pip3 is successful install !"
  else
    echo "Something wrong is happen, check it out !"
fi
}


fixcode
installpython
installsetuptools
installpip
py3ok
pip3ok

