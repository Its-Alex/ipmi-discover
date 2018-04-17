import re
import subprocess
import argparse
from json import load, dumps
from time import sleep
from pathlib import Path

__version__ = '0.1.0'

# Oui database import
mac_db = load(Path(__file__).absolute().parent.joinpath(
    'mac-database.json').open())


def parse_kea_log(output):
    result = []

    lines = output.splitlines()
    for line in lines:
        if line.find(b'DHCP4_LEASE_ALLOC') != -1:
            mac = re.search(
                r'([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})', line.decode()).group()
            result.append({
                'ip': re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line.decode()).group(),
                'mac': mac,
                'vendor': mac_lookup(mac)
            })
    return result

def mac_lookup(mac):
    mac_prefix = ":".join(mac.split(':')[0:3]).upper()
    if mac_prefix not in mac_db:
        return None
    else:
        return mac_db[mac_prefix]

def is_ipmiping(ip):
    p = subprocess.Popen(
        "/usr/bin/ipmiping -c 2 " + ip,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    _, err = p.communicate()
    if p.returncode == 0:
        return True
    else:
        if p.returncode != 1:
            print("ipmiping on " + ip + " failed: " +
                err.decode('utf-8'), end='')
            exit(1)
        return False

def cli():
    print("ipmi-discover v0.1.0")

if __name__ == '__main__':
    cli()
