#!/bin/bash

case $1 in 
home)
  cp -r /etc/sysconfig/network-scripts/ifcfg-eth0.home /etc/sysconfig/network-scripts/ifcfg-eth0;
  service network restart;
;;
company)
  cp -r /etc/sysconfig/network-scripts/ifcfg-eth0.company /etc/sysconfig/network-scripts/ifcfg-eth0;
  service network restart;
;;
*)
  echo "Please input home or company"
;;
esac
