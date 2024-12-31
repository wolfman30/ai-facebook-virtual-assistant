from src.main.facebook_group_validator import FacebookGroupValidator

class FacebookGroupEngagementService:
    def __init__(self, repository):
        self.repository = repository

    def register_group(self, group):
        # Delegate validation
        FacebookGroupValidator.validate_group_data(group)
        self.repository.save(group)
        return True

    def get_registered_groups(self):
        return self.repository.groups

    def find_group_by_name(self, name):
        return self.repository.find_by_name(name)
