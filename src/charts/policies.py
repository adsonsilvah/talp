from src.charts.common import bars
from src.datasets.schema import POLICIES


def policies(frame, mode="percent", group=None):
    return bars(frame, "policy", POLICIES, "Quem deve definir as regras de uso?", mode, group)
