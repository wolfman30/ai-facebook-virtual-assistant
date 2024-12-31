import unittest


from facebook_group_engagement_service import FacebookGroupEngagementService


class TestFacebookGroupEngagement(unittest.TestCase):
    def test_group_joining_logs_metrics(self):
        group_data = {
            "name": "Heart Health Group",
            "member_count": 1500, 
            "rules": ["No promotions", "Be respectful"]
        }
        
        engagement_service = FacebookGroupEngagementService()
        
        success = engagement_service.join_and_log_group(group_data)
        
        self.assertTrue(success)
        self.assertIn("Heart Health Group", engagement_service.get_logged_groups())


if __name__ == '__main__':
    unittest.main()