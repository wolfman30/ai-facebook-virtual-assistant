import unittest
from unittest import TestCase
from src.main.facebook_group import FacebookGroup
from src.main.facebook_group_repository import FacebookGroupRepository


class TestFacebookGroupRepository(TestCase):
    def setUp(self):
        self.repository = FacebookGroupRepository()
        self.sample_group = FacebookGroup(
            name="Heart Health Group",
            member_count=1500,
            rules=["No promotions", "Be respectful"]
        )

    def test_save_group(self):
        self.repository.save(self.sample_group)
        self.assertEqual(len(self.repository.groups), 1)

    def test_duplicate_group_not_saved(self):
        self.repository.save(self.sample_group)
        with self.assertRaises(ValueError):
            self.repository.save(self.sample_group)

    def test_find_by_name(self):
        self.repository.save(self.sample_group)
        found_group = self.repository.find_by_name("Heart Health Group")
        self.assertIsNotNone(found_group)
        self.assertEqual(found_group.name, "Heart Health Group")

    def test_find_by_name_not_found(self):
        found_group = self.repository.find_by_name("Nonexistent Group")
        self.assertIsNone(found_group)
        
if __name__ == '__main__':
    unittest.main()