from src.datasets.schema import ACADEMIC, POLICIES


def percentage(count, denominator):
    return 100 * count / denominator if denominator else None


def apply_filters(frame, faculties=None, levels=None, confidence=None):
    result = frame
    for field, values in (("faculty", faculties), ("study_level", levels), ("confidence", confidence)):
        if values:
            result = result[result[field].isin(values)]
    return result.copy()


def selection(frame, field, option):
    return int(frame[field].map(lambda values: option in values).sum())


def metrics(frame):
    n = len(frame)
    counts = {
        "Conhecia o ChatGPT": selection(frame, "awareness", "Chat GPT"),
        "Finalidade acadêmica": selection(frame, "purposes", ACADEMIC),
        "Apoio gramatical · favoráveis": int(frame.grammar_attitude.isin(["Supportive", "Somewhat supportive"]).sum()),
        "Redação integral · contrários": int(frame.essay_attitude.isin(["Unsupportive", "Somewhat unsupportive"]).sum()),
        "Política institucional única": int(frame.policy.eq(POLICIES[0]).sum()),
    }
    return {name: {"count": count, "denominator": n, "percent": percentage(count, n)} for name, count in counts.items()}
