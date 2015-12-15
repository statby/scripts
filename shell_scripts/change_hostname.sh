#!/bin/bash

if [ ${UID} -ne 0 ];then
    echo "Please use root !"
    exit 1
fi

if [ $# -ne 1 ];then
  echo "Please input one HOSTNAME !"
  exit 2
fi


name=$1
sed -i "s/^HOSTNAME.*$/HOSTNAME=${name}/" /etc/sysconfig/network
echo $name > /proc/sys/kernel/hostname

source /etc/profile
PS1="[\u@$HOSTNAME \W]\$"

echo "If you want to take effect immediately, please excute with source but not bash !"
