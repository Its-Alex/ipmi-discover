#!/bin/bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -t|--time)
    TIME="$2"
    shift # past argument
    shift # past value
    ;;
    --kea-log-path)
    LOG_PATH="$2"
    shift # past argument
    shift # past value
    ;;
    --kea-args)
    KEA_ARGS="$2"
    shift # past argument
    shift # past value
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

if [ -z $TIME ]; then
    TIME="60"
fi
if [ -z $LOG_PATH ]; then
    LOG_PATH="/var/log/kea-debug.log"
fi
if [ -z $KEA_ARGS ]; then
    KEA_ARGS="-c /kea-config.json"
fi

# Start kea-dhcp4
nohup /usr/sbin/kea-dhcp4 $KEA_ARGS &>/dev/null &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start kea: $status"
  exit $status
fi

# Start the second process
ipmi-finder -t $TIME --kea-log-path $LOG_PATH
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start ipmi-finder: $status"
  exit $status
fi
