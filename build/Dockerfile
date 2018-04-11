FROM ubuntu:18.04 AS build

ENV LANG C.UTF-8
ENV KEA_VERSION 1.3.0

RUN apt-get update && apt-get -y --no-install-recommends --no-upgrade install \
# FreeIPMI tools
    freeipmi-tools \
# Build deps
    make \
    automake \
    g++ \
    dh-autoreconf \
# Tools deps
    unzip \
    wget \
# kea deps
    libtool \
    autoconf \
    libssl-dev \
    liblog4cplus-dev \
    libboost-system-dev \
    libpq-dev \
    postgresql-server-dev-all \
## build kea
    && cd / \
    && wget -O kea.tar.gz --no-check-certificate https://ftp.isc.org/isc/kea/$KEA_VERSION/kea-$KEA_VERSION.tar.gz \
    && mkdir -p /usr/src/kea \
    && tar xf kea.tar.gz --strip-components=1 -C /usr/src/kea \
    && rm kea.tar.gz \
    && cd /usr/src/kea \
    && autoreconf \
        --install \
    && CXXFLAGS='-Os' ./configure \
        --prefix=/usr \
        --sysconfdir=/etc \
        --localstatedir=/var \
        --with-log4cplus \
        --with-dhcp-pgsql \
        --with-openssl \
        --enable-static=false \
    && make -j "$(getconf _NPROCESSORS_ONLN)" \
    && make install \
## cleanup
    && apt purge -y \
        make \
        automake \
        g++ \
        dh-autoreconf \
        unzip \
        wget \
        libtool \
        autoconf \
        libssl-dev \
        liblog4cplus-dev \
        libboost-system-dev \
        libpq-dev \
        e2fslibs \
        postgresql-server-dev-all \
    && apt remove --purge -y $(apt-mark showauto) \
    && apt autoremove -y

EXPOSE 67/udp

CMD ["/usr/local/sbin/kea-dhcp4", "--help"]
