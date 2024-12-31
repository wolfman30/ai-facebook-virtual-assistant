from facebook_group import FacebookGroup


class FacebookGroupEngagementService:
    def __init__(self):
        self.logged_groups: list[FacebookGroup] = []

    def register_facebook_group(self, group: FacebookGroup):
        if any(logged_group.name == group.name for logged_group in self.logged_groups):
            raise ValueError(f"Group with name '{group.name}' is already logged.")
        self.logged_groups.append(group)
        return True

    def get_logged_groups(self):
        return self.logged_groups

    def find_group_by_name(self, name: str):
        # Search for a group by its name
        return next((group for group in self.logged_groups if group.name == name), None)


