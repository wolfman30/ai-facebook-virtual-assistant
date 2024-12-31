from dataclasses import dataclass

@dataclass
class FacebookGroup: 
    name: str
    member_count: int
    rules: list
    
    def is_rule_valid(self, rule: str) -> bool:
        return rule in self.rules
    
    