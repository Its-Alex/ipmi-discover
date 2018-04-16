import re

__version__ = '0.1.0'

def parse_kea_log(output):
    result = []

    lines = output.splitlines()
    for line in lines:
        if line.find(b'has been allocated') != -1:
            result.append({
                'ip': re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line.decode()).group(),
                'mac': re.search(r'([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})', line.decode()).group()
            })

    return result

def cli():
    print("ipmi-discover v0.1.0")

if __name__ == '__main__':
    cli()
