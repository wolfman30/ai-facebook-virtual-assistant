class FacebookGroupValidator:
    
    @staticmethod
    def validate_group_data(group):
        if group is None or not hasattr(group, "name"):
            raise ValueError("Invalid group object.")
        if group.member_count < 10:
            raise ValueError("Group must have at least 10 members.")
        if len(group.rules) < 1:
            raise ValueError("Group must have at least one rule.")
        
    @staticmethod
    def validate_unique_group(group, existing_groups):
        """Checks if a group with the same name already exists."""
        if any(existing_group.name == group.name for existing_group in existing_groups):
            raise ValueError(f"Group with name '{group.name}' already exists.")

