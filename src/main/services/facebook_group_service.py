import csv
from src.main.models.interaction import Interaction
from src.main.validators.facebook_group_validator import FacebookGroupValidator

class FacebookGroupEngagementService:
    def __init__(self, repository):
        self.repository = repository
        self.interactions: list[Interaction] = []

    def register_group(self, group):
        # Delegate validation
        FacebookGroupValidator.validate_group_data(group)
        self.repository.save(group)
        return True

    def get_registered_groups(self):
        return self.repository.groups

    def find_group_by_name(self, name: str):
        return self.repository.find_by_name(name)
    
    def register_interaction(self, interaction: Interaction):
        self.interactions.append(interaction)
        
    def get_logged_interactions(self):
        return self.interactions
    
    def export_interactions_to_csv(self, filename: str):
        """Exports logged interactions to a CSV file."""
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["interaction_type", "group_name", "content", "timestamp", "metadata"])
            writer.writeheader()
            for interaction in self.interactions:
                writer.writerow({
                    "interaction_type": interaction.interaction_type,
                    "group_name": interaction.group_name,
                    "content": interaction.content,
                    "timestamp": interaction.timestamp,
                    "metadata": str(interaction.metadata),
                })
                
    def analyze_interactions(self):
        """Analyze logged interactions."""
        analysis = {"post": 0, "comment": 0, "response": 0}
        for interaction in self.interactions:
            analysis[interaction.interaction_type] += 1
        return analysis
    
    def analyze_and_alert_interactions(self, 
                                       like_threshold=10, 
                                       comment_threshold=5):
        """Identifies interactions with high engagement."""
        alerts = []
        for interaction in self.interactions:
            likes = interaction.metadata.get("likes", 0)
            comments = interaction.metadata.get("comments", 0)
            if likes >= like_threshold or comments >= comment_threshold:
                alerts.append(interaction)
        return alerts
    
    def generate_weekly_report(self):
        """Generates a summary report of all interactions."""
        analysis = self.analyze_interactions()
        report = [
            f"Weekly Report:",
            f"Posts: {analysis['post']}",
            f"Comments: {analysis['comment']}",
            f"Responses: {analysis['response']}"
        ]
        return "\n".join(report)
