import unittest
from unittest import TestCase

from src.main.facebook_group import FacebookGroup
from src.main.facebook_group_validator import FacebookGroupValidator


class TestFacebookGroupValidator(TestCase):
    def setUp(self):
        self.existing_groups = [
            FacebookGroup(name="Existing Group", member_count=20, rules=["Rule 1"]),
        ]

    def test_valid_group(self):
        group = FacebookGroup(name="New Group", member_count=50, rules=["Be respectful"])
        FacebookGroupValidator.validate_group_data(group)  # Should not raise an exception

    def test_invalid_member_count(self):
        group = FacebookGroup(name="Small Group", member_count=5, rules=["Be kind"])
        with self.assertRaises(ValueError):
            FacebookGroupValidator.validate_group_data(group)

    def test_invalid_rules(self):
        group = FacebookGroup(name="No Rules Group", member_count=50, rules=[])
        with self.assertRaises(ValueError):
            FacebookGroupValidator.validate_group_data(group)

    def test_invalid_group_object(self):
        with self.assertRaises(ValueError):
            FacebookGroupValidator.validate_group_data(None)

    def test_duplicate_group(self):
        group = FacebookGroup(name="Existing Group", member_count=50, rules=["Rule 2"])
        with self.assertRaises(ValueError):
            FacebookGroupValidator.validate_unique_group(group, self.existing_groups)

    def test_unique_group(self):
        group = FacebookGroup(name="Unique Group", member_count=50, rules=["Rule 3"])
        FacebookGroupValidator.validate_unique_group(group, self.existing_groups)  # Should not raise an exception

 
            
if __name__ == '__main__':
    unittest.main()
