from ipmi_finder import parse_kea_log

def test_parse_kea_log():
    # Kea log format

    output = b"""
2018-04-13 11:32:55.312 INFO  [kea-dhcp4.dhcp4/1] DHCP4_STARTING Kea DHCPv4 server version 1.3.0 starting
2018-04-13 11:32:55.321 INFO  [kea-dhcp4.dhcpsrv/1] DHCPSRV_CFGMGR_ADD_IFACE listening on interface enp0s8
2018-04-13 11:32:55.321 INFO  [kea-dhcp4.dhcpsrv/1] DHCPSRV_CFGMGR_SOCKET_TYPE_DEFAULT "dhcp-socket-type" not specified , using default socket type raw
2018-04-13 11:32:55.327 INFO  [kea-dhcp4.dhcpsrv/1] DHCPSRV_CFGMGR_NEW_SUBNET4 a new subnet has been added to configuration: 192.168.0.0/24 with params: t1=1000, t2=2000, valid-lifetime=4000
2018-04-13 11:32:55.327 INFO  [kea-dhcp4.dhcp4/1] DHCP4_CONFIG_COMPLETE DHCPv4 server has completed configuration: added IPv4 subnets: 1; DDNS: disabled
2018-04-13 11:32:55.327 INFO  [kea-dhcp4.dhcpsrv/1] DHCPSRV_MEMFILE_DB opening memory file lease database: type=memfile universe=4
2018-04-13 11:32:55.327 INFO  [kea-dhcp4.dhcpsrv/1] DHCPSRV_MEMFILE_LEASE_FILE_LOAD loading leases from file /var/kea/kea-leases4.csv
2018-04-13 11:32:55.327 INFO  [kea-dhcp4.dhcpsrv/1] DHCPSRV_MEMFILE_LFC_SETUP setting up the Lease File Cleanup interval to 3600 sec
2018-04-13 11:32:55.327 INFO  [kea-dhcp4.dhcp4/1] DHCP4_STARTED Kea DHCPv4 server version 1.3.0 started
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
    assert result[1]['ip'] == '192.168.0.13'
    assert result[1]['mac'] == 'd4:ae:52:d3:0f:76'
    assert result[2]['ip'] == '192.168.0.19'
    assert result[2]['mac'] == 'd4:ae:52:d0:43:b5'

