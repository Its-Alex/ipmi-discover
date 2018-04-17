# IPMI-Discover

This project aim to discover mac address of all IPMI asking IP address

## Requirements

* [docker](https://www.docker.com/)
* [pipenv](https://github.com/pypa/pipenv)

```
$ pipenv install
$ pipenv shell
```

## Build

```
$ docker build -t <tag> .
```

## Use

To use this image you need to provide a kea configuration in the container at
`/kea-config.json`

By default this tool wait 60 seconds for kea to alloc ip then parse it's log

You can change the time to wait with **-t** or **--time** option

You can change how to launch kea too with **--kea-start** by default it's
`/usr/sbin/kea-dhcp4 -c /kea-config.json`
## Hack

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
