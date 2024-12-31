import unittest
from unittest import TestCase

from src.main.facebook_group import FacebookGroup
from src.main.facebook_group_repository import FacebookGroupRepository
from src.main.facebook_group_service import FacebookGroupEngagementService
from src.main.facebook_group_validator import FacebookGroupValidator


class TestFacebookGroupEngagement(TestCase):
    def setUp(self):
        self.repository = FacebookGroupRepository()
        self.engagement_service = FacebookGroupEngagementService(
            self.repository
        )
        self.sample_group = FacebookGroup(
            name="Heart Health Group",
            member_count=1500,
            rules=["No promotions", "Be respectful"]
        )

    def test_register_group(self):
        success = self.engagement_service.register_group(self.sample_group)
        self.assertTrue(success)
        self.assertEqual(len(self.engagement_service.get_registered_groups()), 1)

    def test_duplicate_group_not_registered(self):
        self.engagement_service.register_group(self.sample_group)
        with self.assertRaises(ValueError):
            self.engagement_service.register_group(self.sample_group)

    def test_find_group_by_name(self):
        self.engagement_service.register_group(self.sample_group)
        found_group = self.engagement_service.find_group_by_name("Heart Health Group")
        self.assertIsNotNone(found_group)
        self.assertEqual(found_group.name, "Heart Health Group")

    def test_find_group_by_name_not_found(self):
        found_group = self.engagement_service.find_group_by_name("Nonexistent Group")
        self.assertIsNone(found_group)

if __name__ == '__main__':
    unittest.main()
