class FacebookGroupEngagementService:
    def __init__(self):
        self.logged_groups = []

    def join_and_log_group(self, group_data):
        self.logged_groups.append(group_data["name"])
        return True

    def get_logged_groups(self):
        return self.logged_groups

