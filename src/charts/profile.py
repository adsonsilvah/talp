from src.charts.common import bars
from src.datasets.schema import CATEGORIES


def confidence(frame, mode="percent", group=None):
    return bars(frame, "confidence", [1,2,3,4,5], "Como se distribui a confiança na escrita?", mode, group, horizontal=False, ordered=True)


def faculty(frame, mode="percent"):
    return bars(frame, "faculty", CATEGORIES["faculty"], "Quem respondeu: faculdades", mode)


def study_level(frame, mode="percent"):
    return bars(frame, "study_level", CATEGORIES["study_level"], "Quem respondeu: níveis de estudo", mode)
