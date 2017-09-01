import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.iosxe.show_bgp import ShowBgpAllSummary, ShowBgpAllClusterIds


class test_show_bgp_all_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf':
            {'default':
                 {'neighbor':
                      {'200.0.1.1':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': '01:07:38',
                                      'version': 4}}},
                      '200.0.2.1':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': 'never',
                                      'version': 4}}},
                      '200.0.4.1':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': '01:07:38',
                                      'version': 4}}},
                      '201.0.14.4':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 200,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': 'never',
                                      'version': 4}}},
                      '201.0.26.2':
                           {'address_family':
                                {'ipv4 unicast':
                                     {'as': 300,
                                      'attribute_entries': '1/1',
                                      'bgp_table_version': 28,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 0,
                                      'msg_sent': 0,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3672,
                                               'total_entries': 27},
                                      'prefixes':
                                          {'memory_usage': 6696,
                                           'total_entries': 27},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'total_memory': 10648,
                                      'activity_prefixes': '47/20',
                                      'activity_paths': '66/39',
                                      'scan_interval': 60,
                                      'route_identifier': '200.0.1.1',
                                      'routing_table_version': 28,
                                      'state_pfxrcd': 'Idle',
                                      'tbl_ver': 1,
                                      'up_down': '01:07:38',
                                      'version': 4}}},
                       '2000::1:1': {'address_family': {'ipv6 unicast': {'as': 100,
                                                                         'bgp_table_version': 1,
                                                                         'input_queue': 0,
                                                                         'local_as': 100,
                                                                         'msg_rcvd': 0,
                                                                         'msg_sent': 0,
                                                                         'output_queue': 0,
                                                                         'route_identifier': '200.0.1.1',
                                                                         'routing_table_version': 1,
                                                                         'state_pfxrcd': 'Idle',
                                                                         'tbl_ver': 1,
                                                                         'up_down': '01:07:38',
                                                                         'version': 4}}},
                       '2000::4:1': {'address_family': {'ipv6 unicast': {'as': 100,
                                                                         'bgp_table_version': 1,
                                                                         'input_queue': 0,
                                                                         'local_as': 100,
                                                                         'msg_rcvd': 0,
                                                                         'msg_sent': 0,
                                                                         'output_queue': 0,
                                                                         'route_identifier': '200.0.1.1',
                                                                         'routing_table_version': 1,
                                                                         'state_pfxrcd': 'Idle',
                                                                         'tbl_ver': 1,
                                                                         'up_down': '01:07:38',
                                                                         'version': 4}}},
                       '2001::14:4': {'address_family': {'ipv6 unicast': {'as': 200,
                                                                          'bgp_table_version': 1,
                                                                          'input_queue': 0,
                                                                          'local_as': 100,
                                                                          'msg_rcvd': 0,
                                                                          'msg_sent': 0,
                                                                          'output_queue': 0,
                                                                          'route_identifier': '200.0.1.1',
                                                                          'routing_table_version': 1,
                                                                          'state_pfxrcd': 'Idle',
                                                                          'tbl_ver': 1,
                                                                          'up_down': 'never',
                                                                          'version': 4}}},
                       '2001::26:2': {'address_family': {'ipv6 unicast': {'as': 300,
                                                                          'bgp_table_version': 1,
                                                                          'input_queue': 0,
                                                                          'local_as': 100,
                                                                          'msg_rcvd': 0,
                                                                          'msg_sent': 0,
                                                                          'output_queue': 0,
                                                                          'route_identifier': '200.0.1.1',
                                                                          'routing_table_version': 1,
                                                                          'state_pfxrcd': 'Idle',
                                                                          'tbl_ver': 1,
                                                                          'up_down': '01:07:38',
                                                                          'version': 4}}},
                       '3.3.3.3': {'address_family':
                                       {'vpnv4 unicast':
                                            {'as': 100,
                                             'bgp_table_version': 1,
                                             'input_queue': 0,
                                             'local_as': 100,
                                             'msg_rcvd': 0,
                                             'msg_sent': 0,
                                             'output_queue': 0,
                                             'route_identifier': '200.0.1.1',
                                             'routing_table_version': 1,
                                             'state_pfxrcd': 'Idle',
                                             'tbl_ver': 1,
                                             'up_down': 'never',
                                             'version': 4},
                                        'vpnv6 unicast':
                                            {'as': 100,
                                             'bgp_table_version': 1,
                                             'input_queue': 0,
                                             'local_as': 100,
                                             'msg_rcvd': 0,
                                             'msg_sent': 0,
                                             'output_queue': 0,
                                             'route_identifier': '200.0.1.1',
                                             'routing_table_version': 1,
                                             'state_pfxrcd': 'Idle',
                                             'tbl_ver': 1,
                                             'up_down': 'never',
                                             'version': 4}
                                        }
                                   }
                       }
                  }
             }
    }


    golden_output = {'execute.return_value': '''
        For address family: IPv4 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 28, main routing table version 28
        27 network entries using 6696 bytes of memory
        27 path entries using 3672 bytes of memory
        1/1 BGP path/bestpath attribute entries using 280 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 10648 total bytes of memory
        BGP activity 47/20 prefixes, 66/39 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        200.0.1.1       4          100       0       0        1    0    0 01:07:38 Idle
        200.0.2.1       4          100       0       0        1    0    0 never    Idle
        200.0.4.1       4          100       0       0        1    0    0 01:07:38 Idle
        201.0.14.4      4          200       0       0        1    0    0 never    Idle
        201.0.26.2      4          300       0       0        1    0    0 01:07:38 Idle

        For address family: IPv6 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2000::1:1       4          100       0       0        1    0    0 01:07:38 Idle
        2000::4:1       4          100       0       0        1    0    0 01:07:38 Idle
        2001::14:4      4          200       0       0        1    0    0 never    Idle
        2001::26:2      4          300       0       0        1    0    0 01:07:38 Idle

        For address family: VPNv4 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        3.3.3.3         4          100       0       0        1    0    0 never    Idle

        For address family: VPNv6 Unicast
        BGP router identifier 200.0.1.1, local AS number 100
        BGP table version is 1, main routing table version 1

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        3.3.3.3         4          100       0       0        1    0    0 never    Idle

        '''}

    golden_parsed_output_2 = {
        'vrf':
            {'default':
                 {'neighbor':
                      {'2.2.2.2':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 88,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 56,
                                      'up_down': '01:12:00',
                                      'version': 4},
                                'vpnv6 unicast':
                                    {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 88,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 66,
                                      'up_down': '01:12:00',
                                      'version': 4}
                                }
                           },
                      '3.3.3.3':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 89,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 56,
                                      'up_down': '01:12:06',
                                      'version': 4},
                                 'vpnv6 unicast':
                                     {'as': 100,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 82,
                                      'msg_sent': 89,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '10',
                                      'tbl_ver': 66,
                                      'up_down': '01:12:06',
                                      'version': 4}
                                 }},
                      '10.4.6.6':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 300,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 68,
                                      'msg_sent': 75,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 56,
                                      'up_down': '01:03:23',
                                      'version': 4}}},
                      '20.4.6.6':
                           {'address_family':
                                {'vpnv4 unicast':
                                     {'as': 400,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 56,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 67,
                                      'msg_sent': 72,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 3600,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 4560,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 9384,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 56,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 56,
                                      'up_down': '01:03:14',
                                      'version': 4}}},
                      '2001:DB8:4:6::6':
                           {'address_family':
                                {'vpnv6 unicast':
                                     {'as': 300,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 67,
                                      'msg_sent': 75,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 66,
                                      'up_down': '01:03:19',
                                      'version': 4}
                                 }},
                      '2001:DB8:20:4:6::6':
                           {'address_family':
                                {'vpnv6 unicast':
                                     {'as': 400,
                                      'attribute_entries': '6/4',
                                      'bgp_table_version': 66,
                                      'input_queue': 0,
                                      'local_as': 100,
                                      'msg_rcvd': 67,
                                      'msg_sent': 73,
                                      'output_queue': 0,
                                      'path': {'memory_usage': 4860,
                                               'total_entries': 45},
                                      'prefixes':
                                          {'memory_usage': 5280,
                                           'total_entries': 30},
                                      'cache_entries':
                                          {
                                              'route-map':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  },
                                              'filter-list':
                                                  {
                                                      'total_entries': 0,
                                                      'memory_usage': 0
                                                  }
                                          },
                                      'entries':
                                          {
                                              'AS-PATH':
                                                  {
                                                      'total_entries': 3,
                                                      'memory_usage': 120
                                                  },
                                              'rrinfo':
                                                  {
                                                      'total_entries': 2,
                                                      'memory_usage': 48
                                                  }
                                          },
                                      'community_entries':
                                          {'total_entries': 4,
                                           'memory_usage': 96,
                                           },
                                      'total_memory': 11364,
                                      'activity_prefixes': '85/25',
                                      'activity_paths': '120/30',
                                      'scan_interval': 60,
                                      'route_identifier': '4.4.4.4',
                                      'routing_table_version': 66,
                                      'state_pfxrcd': '5',
                                      'tbl_ver': 66,
                                      'up_down': '01:03:11',
                                      'version': 4}
                                 }
                           }

                      }
                 }
            }
        }

    golden_output_2 = {'execute.return_value': '''
        For address family: VPNv4 Unicast
        BGP router identifier 4.4.4.4, local AS number 100
        BGP table version is 56, main routing table version 56
        30 network entries using 4560 bytes of memory
        45 path entries using 3600 bytes of memory
        6/4 BGP path/bestpath attribute entries using 960 bytes of memory
        2 BGP rrinfo entries using 48 bytes of memory
        3 BGP AS-PATH entries using 120 bytes of memory
        4 BGP extended community entries using 96 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 9384 total bytes of memory
        BGP activity 85/25 prefixes, 120/30 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.2         4          100      82      88       56    0    0 01:12:00       10
        3.3.3.3         4          100      82      89       56    0    0 01:12:06       10
        10.4.6.6        4          300      68      75       56    0    0 01:03:23        5
        20.4.6.6        4          400      67      72       56    0    0 01:03:14        5

        For address family: VPNv6 Unicast
        BGP router identifier 4.4.4.4, local AS number 100
        BGP table version is 66, main routing table version 66
        30 network entries using 5280 bytes of memory
        45 path entries using 4860 bytes of memory
        6/4 BGP path/bestpath attribute entries using 960 bytes of memory
        2 BGP rrinfo entries using 48 bytes of memory
        3 BGP AS-PATH entries using 120 bytes of memory
        4 BGP extended community entries using 96 bytes of memory
        0 BGP route-map cache entries using 0 bytes of memory
        0 BGP filter-list cache entries using 0 bytes of memory
        BGP using 11364 total bytes of memory
        BGP activity 85/25 prefixes, 120/30 paths, scan interval 60 secs

        Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        2.2.2.2         4          100      82      88       66    0    0 01:12:00       10
        3.3.3.3         4          100      82      89       66    0    0 01:12:06       10
        2001:DB8:4:6::6 4          300      67      75       66    0    0 01:03:19        5
        2001:DB8:20:4:6::6
                4          400      67      73       66    0    0 01:03:11        5


            '''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_summary_obj = ShowBgpAllSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_summary_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowBgpAllSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class test_show_bgp_all_cluster_ids(unittest.TestCase):
    '''
        unit test for  show bgp all cluster_ids
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf':
            {'default':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_status': 'configured',
                    'reflection_type': 'used',
                    'cluster_status': 'enabled',
                },
                'vrf1':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_status': 'configured',
                    'reflection_type': 'used',
                    'cluster_status': 'enabled',
                },
                'vrf2':
                    {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_status': 'configured',
                    'reflection_type': 'used',
                    'cluster_status': 'enabled',
                    }
            }
    }

    golden_output = {'execute.return_value': '''
        R4_iosv#show vrf detail | inc \(VRF
        VRF VRF1 (VRF Id = 1); default RD 300:1; default VPNID <not set>
        VRF VRF2 (VRF Id = 2); default RD 400:1; default VPNID <not set>

        R4_iosv#show bgp all cluster-ids
        Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
        BGP client-to-client reflection:         Configured    Used
         all (inter-cluster and intra-cluster): ENABLED
         intra-cluster:                         ENABLED       ENABLED

        List of cluster-ids:
        Cluster-id     #-neighbors C2C-rfl-CFG C2C-rfl-USE
        '''}

    golden_parsed_output_1 = {
        'vrf':
            {'default':
                {
                    'cluster_id': '4.4.4.4',
                    'configured_id': '0.0.0.0',
                    'reflection_status': 'configured',
                    'reflection_type': 'used',
                    'cluster_status': 'enabled',
                }
            }
    }

    golden_output_1 = {'execute.return_value': '''
           R4_iosv#show vrf detail | inc \(VRF
           % unmatched ()
           % Failed to compile regular expression.

           R4_iosv#show bgp all cluster-ids
           Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
           BGP client-to-client reflection:         Configured    Used
            all (inter-cluster and intra-cluster): ENABLED
            intra-cluster:                         ENABLED       ENABLED

           List of cluster-ids:
           Cluster-id     #-neighbors C2C-rfl-CFG C2C-rfl-USE
           '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpAllClusterIds(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowBgpAllClusterIds(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
