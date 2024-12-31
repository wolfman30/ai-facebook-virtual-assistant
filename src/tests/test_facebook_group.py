import unittest
from unittest import TestCase

from src.main.models.facebook_group import FacebookGroup


class TestFacebookGroup(TestCase):

    def setUp(self):
        self.group = FacebookGroup(name="Test Group", member_count=100, rules=["Be kind", "No spam", "Respect others"])
        self.empty_group = FacebookGroup(name="Empty Group", member_count=0, rules=[])

    def test_is_rule_valid_with_existing_rule(self):
        self.assertTrue(self.group.is_rule_valid("Be kind"))

    def test_is_rule_valid_with_non_existing_rule(self):
        self.assertFalse(self.group.is_rule_valid("No advertising"))
        
    def test_is_rule_valid_with_empty_rule(self):
        self.assertFalse(self.group.is_rule_valid(""))
        
    def test_is_rule_valid_with_none_rule(self):
        self.assertFalse(self.group.is_rule_valid(None))
        
    def test_is_rule_valid_with_rule_not_string(self):
        self.assertFalse(self.group.is_rule_valid(123))
        
    def test_is_rule_valid_with_empty_group(self):
        self.assertFalse(self.empty_group.is_rule_valid("Be kind"))

if __name__ == '__main__': # pragma: no cover
    unittest.main()