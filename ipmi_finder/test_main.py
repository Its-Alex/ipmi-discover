from ipmi_finder import parse_kea_log, mac_lookup

def test_parse_kea_log():
    # Kea log format

    output = b"""
2018-04-13 11:33:02.082 INFO  [kea-dhcp4.leases/1] DHCP4_LEASE_ADVERT [hwtype=1 08:00:27:72:c6:76], cid=[no info], tid=0xf192aa47: lease 192.168.0.10 will be advertised
2018-04-13 11:33:02.083 INFO  [kea-dhcp4.leases/1] DHCP4_LEASE_ALLOC [hwtype=1 08:00:27:72:c6:76], cid=[no info], tid=0xf192aa47: lease 192.168.0.10 has been allocated
2018-04-13 11:34:14.047 INFO  [kea-dhcp4.leases/1] DHCP4_LEASE_ADVERT [hwtype=1 d4:ae:52:d3:0f:76], cid=[no info], tid=0x57d30f76: lease 192.168.0.13 will be advertised
2018-04-13 11:34:18.091 INFO  [kea-dhcp4.leases/1] DHCP4_LEASE_ALLOC [hwtype=1 d4:ae:52:d3:0f:76], cid=[no info], tid=0x57d30f76: lease 192.168.0.13 has been allocated
2018-04-13 11:34:24.085 INFO  [kea-dhcp4.leases/1] DHCP4_LEASE_ADVERT [hwtype=1 d4:ae:52:d0:43:b5], cid=[01:d4:ae:52:d0:43:b5], tid=0x3c55d864: lease 192.168.0.19 will be advertised
2018-04-13 11:34:24.145 INFO  [kea-dhcp4.leases/1] DHCP4_LEASE_ALLOC [hwtype=1 d4:ae:52:d0:43:b5], cid=[01:d4:ae:52:d0:43:b5], tid=0x3c55d864: lease 192.168.0.19 has been allocated
"""

    result = parse_kea_log(output)

    assert result[0]['ip'] == '192.168.0.10'
    assert result[0]['mac'] == '08:00:27:72:c6:76'
    assert result[0]['vendor']['name'] == 'PcsCompu'
    assert result[1]['ip'] == '192.168.0.13'
    assert result[1]['mac'] == 'd4:ae:52:d3:0f:76'
    assert result[1]['vendor']['name'] == 'Dell'
    assert result[2]['ip'] == '192.168.0.19'
    assert result[2]['mac'] == 'd4:ae:52:d0:43:b5'
    assert result[2]['vendor']['name'] == 'Dell'

