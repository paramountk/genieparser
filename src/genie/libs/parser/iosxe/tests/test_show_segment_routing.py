import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_segment_routing import (ShowSegmentRoutingMplsLB)

# ============================================
# Parser for 'show segment-routing mpls state'
# ============================================

class test_show_routing_mpls_state(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'label_min': 15000,
        'label_max': 15999,
        'state': 'ENABLED',
        'default': 'Yes',
    }
    
    golden_output = {'execute.return_value': '''
        show segment-routing mpls lb
        LABEL-MIN  LABEL_MAX  STATE           DEFAULT
        15000      15999      ENABLED         Yes
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsLB(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsLB(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()