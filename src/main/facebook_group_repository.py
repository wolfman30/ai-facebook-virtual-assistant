from src.main.facebook_group import FacebookGroup

from src.main.facebook_group_validator import FacebookGroupValidator

from src.main.facebook_group_validator import FacebookGroupValidator

class FacebookGroupRepository:
    def __init__(self):
        self.groups = []

    def save(self, group: FacebookGroup):
        FacebookGroupValidator.validate_group_data(group)
        FacebookGroupValidator.validate_unique_group(group, self.groups)
        self.groups.append(group)

    def find_by_name(self, name: str):
        return next((group for group in self.groups if group.name == name), None)


