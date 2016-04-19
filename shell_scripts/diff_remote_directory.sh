#!/bin/env bash
# coding=utf-8
# Date        : 2016-04-18 18:10:20
# Author      : Statby
# Description : 

LOCAL_DIR=""
REMOTE_DIR=""
SSH_USER=""
REMOTE_IP=
RESULT_DIR=""
RESULT_FINAL=$RESULT_DIR/final.txt
[ -x $RESULT_DIR  ] || mkdir -p ${RESULT_DIR}


function diff_dir(){
    ssh ${SSH_USER}@${REMOTE_IP} "find ${REMOTE_DIR}  -type f  -exec md5sum {} \;"|awk  '{print $1  " " $2 }'|sort  > ${RESULT_DIR}/remote_result.txt
    find ${LOCAL_DIR}  -type f  -exec md5sum {} \;|awk  '{print $1  " " $2 }'|sort > ${RESULT_DIR}/local_result.txt
    diff ${RESULT_DIR}/remote_result.txt ${RESULT_DIR}/local_result.txt 2>&1 > /dev/null
}



function show_remote(){
printf "\n"
echo ---------------------------------REMOTE--------------------------------  |tee -a ${RESULT_FINAL}
diff ${RESULT_DIR}/remote_result.txt ${RESULT_DIR}/local_result.txt|grep "<"  |tee -a  ${RESULT_FINAL}
echo ---------------------------------REMOTE--------------------------------  |tee  -a ${RESULT_FINAL}
printf "\n"|tee  -a ${RESULT_FINAL}
}

function show_local(){
echo ---------------------------------LOCAL---------------------------------  |tee -a ${RESULT_FINAL}
diff ${RESULT_DIR}/remote_result.txt ${RESULT_DIR}/local_result.txt|grep ">"  |tee -a  ${RESULT_FINAL}
echo ---------------------------------LOCAL--------------------------------   |tee -a  ${RESULT_FINAL}
printf "\n"|tee  -a ${RESULT_FINAL}
}

function show_default(){
printf "\n"
echo ---------------------------------DEFAULT-------------------------------- |tee  ${RESULT_FINAL}
diff ${RESULT_DIR}/remote_result.txt ${RESULT_DIR}/local_result.txt           |tee -a  ${RESULT_FINAL}
echo ---------------------------------DEFAULT-------------------------------- |tee -a  ${RESULT_FINAL}
printf "\n"|tee  -a ${RESULT_DIR}/final.txt
}


diff_dir
if [ $? -eq "0" ] ;then
    echo "No different!"
    exit 0
else
    case $1 in
        r)
            show_remote;;
        l)
            show_local;;
        *)
            show_default
            show_remote
            show_local
            ;;
    esac
fi

#python sendmail.py email diff_static ${RESULT_FINAL}
