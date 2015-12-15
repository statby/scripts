#!/bin/bash

os=`cat /etc/system-release|cut -d" " -f1`
release=`awk '{print $(NF-1)}' /etc/system-release|cut -d'.' -f1`


if [ $os != "CentOS" ] ; then
    echo "Please use Centos !"
    exit 1

else
    if [ ${release} = "7" ] ; then 
        echo "Your system release is ${os} ${release} !"
        #DO SOME THING
    
    elif [ ${release} = "6" ] ; then
        echo "Your system release is ${os} ${release} !"
        #DO SOME THING 
    else
        echo "Please use Centos 6 or 7 !"
    fi
fi


