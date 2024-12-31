from dataclasses import dataclass


@dataclass
class Interaction: 
    interaction_type: str
    group_name: str
    content: str
    timestamp: str
    metadata: dict
    
    