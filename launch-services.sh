#!/bin/bash

# Start the first process
nohup /usr/sbin/kea-dhcp4 -c /kea-config.json &>/dev/null &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start kea: $status"
  exit $status
fi

# Start the second process
ipmi_finder -t 10
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start ipmi-finder: $status"
  exit $status
fi
