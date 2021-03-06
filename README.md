[![Build Status](https://travis-ci.org/Its-Alex/ipmi-discover.svg?branch=master)](https://travis-ci.org/Its-Alex/ipmi-discover)
[![Docker Automated build](https://img.shields.io/docker/automated/itsalex/ipmi-discover.svg)](https://hub.docker.com/r/itsalex/ipmi-discover/)
[![Docker Build Status](https://img.shields.io/docker/build/itsalex/ipmi-discover.svg)](https://hub.docker.com/r/itsalex/ipmi-discover/)

# IPMI-Discover

This project aim to discover mac address of all IPMI asking IP address

## Requirements

* [docker](https://www.docker.com/)

## Development

Launch image

```
$ docker-compose up -d
```

Enter inside container

```
$ docker-compose exec ipmi-discover bash
```

This folder is synced with `/code/` in container so all python deps are inside
container

## How to

By default this tool wait 60 seconds for kea to alloc ip then parse it's log

To use this image you must provide a kea configuration in the container at
`/kea-config.json` and log to a **file**

You can change options from command execute `/launch-services.sh`:
* **-t** or **--time** to change time to wait for kea alloc by default `60`
* **--kea-log-output** to change where is store log by default `/var/log/kea-debug.log`
* **--kea-start** command to launch kea by default `/usr/sbin/kea-dhcp4 -c /kea-config.json`

docker-compose example:

```
version: '3'
services:
  ipmi-discover:
    image: itsalex/ipmi-discover
    restart: unless-stopped
    network_mode: host
    command: /launch-services.sh -t 60
    volumes:
      - ./kea-config.json:/kea-config.json
```

output:

```json5
[{
	"vendor": {
		"description": "PcsCompu",
		"name": "PcsCompu"
	},
	"ip": "192.168.0.12",
	"mac": "08:00:27:8a:17:9b",
	"ipmi": false
}, {
	"vendor": {
		"description": "PcsCompu",
		"name": "PcsCompu"
	},
	"ip": "192.168.0.12",
	"mac": "08:00:27:8a:17:9b",
	"ipmi": false
}]
```

## License
[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License)
