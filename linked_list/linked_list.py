from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    val: Optional[Any] = None
    next: Optional[Node] = None
