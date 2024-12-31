import os
import csv
import unittest
from unittest import TestCase

from src.main.models.facebook_group import FacebookGroup
from src.main.models.interaction import Interaction
from src.main.repositories.facebook_group_repository import FacebookGroupRepository
from src.main.services.facebook_group_service import FacebookGroupEngagementService


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
        self.sample_interaction = Interaction(
            interaction_type="post",
            group_name="Heart Health Group",
            content="What are your thoughts on vagus nerve exercises?",
            timestamp="2024-12-31T12:00:00",
            metadata={"likes": 12, "comments": 25}
        )

    def test_register_group(self):
        success = self.engagement_service.register_group(self.sample_group)
        self.assertTrue(success)
        self.assertEqual(len(self.engagement_service.get_registered_groups()), 1)

    def test_invalid_group_member_count(self):
        small_group = FacebookGroup(name="Small Group", member_count=5, rules=["Be respectful"])
        with self.assertRaises(ValueError):
            self.engagement_service.register_group(small_group)

    def test_invalid_group_rules(self):
        no_rules_group = FacebookGroup(name="No Rules Group", member_count=20, rules=[])
        with self.assertRaises(ValueError):
            self.engagement_service.register_group(no_rules_group)

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

    def test_log_interaction(self):
        self.engagement_service.register_interaction(self.sample_interaction)
        logged = self.engagement_service.get_logged_interactions()
        self.assertEqual(len(logged), 1)
        self.assertEqual(logged[0].group_name, "Heart Health Group")

    def test_export_interactions_to_csv(self):
        self.engagement_service.register_interaction(self.sample_interaction)
        filename = "test_interactions.csv"
        self.engagement_service.export_interactions_to_csv(filename)

        # Verify file content
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["group_name"], "Heart Health Group")

        # Cleanup
        os.remove(filename)

    def test_analyze_interactions(self):
        self.engagement_service.register_interaction(self.sample_interaction)
        self.engagement_service.register_interaction(
            Interaction(
                interaction_type="comment",
                group_name="Heart Health Group",
                content="Great post!",
                timestamp="2024-12-31T12:30:00",
                metadata={"likes": 5}
            )
        )

        analysis = self.engagement_service.analyze_interactions()
        self.assertEqual(analysis["post"], 1)
        self.assertEqual(analysis["comment"], 1)
        self.assertEqual(analysis["response"], 0)
        
    def test_alerts_for_high_engagement(self):
        self.engagement_service.register_interaction(
            Interaction(
                interaction_type="post",
                group_name="Heart Health Group",
                content="High engagement post",
                timestamp="2024-12-31T12:00:00",
                metadata={"likes": 20, "comments": 15}
            )
        )
        alerts = self.engagement_service.analyze_and_alert_interactions(like_threshold=10, comment_threshold=10)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0].content, "High engagement post")
        
    def test_generate_weekly_report(self):
        self.engagement_service.register_interaction(self.sample_interaction)
        self.engagement_service.register_interaction(
            Interaction(
                interaction_type="comment",
                group_name="Heart Health Group",
                content="Great comment",
                timestamp="2024-12-31T12:30:00",
                metadata={"likes": 5}
            )
        )
        report = self.engagement_service.generate_weekly_report()
        self.assertIn("Posts: 1", report)
        self.assertIn("Comments: 1", report)
        self.assertIn("Responses: 0", report)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
