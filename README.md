# IPMI-Discover

This project aim to discover mac address of all IPMI asking IP address

## Requirements

* [docker](https://www.docker.com/)
* [pipenv](https://github.com/pypa/pipenv)
* [direnv](https://direnv.net/)

```
$ pipenv install
$ pipenv shell
```

## Build

You can build docker image

```
$ make build
```

## Use

Build this image then launch it on server that receive request

You can find an exemple with docker-compose [here](/docker)

## Hack

To enter inside image use:

```
$ make run
```

## License
[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License)
