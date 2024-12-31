import unittest
from facebook_group import FacebookGroup

class TestFacebookGroup(unittest.TestCase):

    def setUp(self):
        self.group = FacebookGroup(name="Test Group", member_count=100, rules=["Be kind", "No spam", "Respect others"])

    def test_is_rule_valid_with_existing_rule(self):
        self.assertTrue(self.group.is_rule_valid("Be kind"))

    def test_is_rule_valid_with_non_existing_rule(self):
        self.assertFalse(self.group.is_rule_valid("No advertising"))

if __name__ == '__main__':
    unittest.main()