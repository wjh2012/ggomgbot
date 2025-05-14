from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict


@dataclass
class User:
    user_id: str
    display_name: str
    preferences: Dict[str, str] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    last_active_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def update_last_active(self) -> None:
        self.last_active_at = datetime.now(timezone.utc)

    def set_preference(self, key: str, value: str) -> None:
        self.preferences[key] = value
