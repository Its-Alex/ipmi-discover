# IPMI-Discover

This project aim to discover mac address of all IPMI asking IP address

## Requirements

* [docker](https://www.docker.com/)
* [pipenv](https://github.com/pypa/pipenv)

```
$ pipenv install
$ pipenv shell
```

## How to

By default this tool wait 60 seconds for kea to alloc ip then parse it's log

To use this image you must provide a kea configuration in the container at
`/kea-config.json` and log to **stdout**

You can change options from command:
* **-t** or **--time** to change time to wait for kea alloc. By default `60`
* **--kea-start** command to launch kea. By default `/usr/sbin/kea-dhcp4 -c /kea-config.json`

docker-compose example:

```
version: '3'
services:
  ipmi-discover:
    image: itsalex/ipmi-discover
    restart: unless-stopped
    command: -t 160
    volumes:
      - ./kea-config.json:/kea-config.json
```

## Hack

Build

```
$ docker build -t <tag> .
```

Launch image

```
$ docker-compose up -d
```

Enter inside container

```
$ docker-compose exec ipmi-discover bash
```
## License
[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License)
