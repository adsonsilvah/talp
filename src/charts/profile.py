import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.charts.common import PALETTE, bars, empty, finish
from src.datasets.schema import CATEGORIES, label


def confidence(frame, mode="percent", group=None):
    return bars(frame, "confidence", [1, 2, 3, 4, 5], "Como se distribui a confiança na escrita?", mode, group, horizontal=False, ordered=True)


def faculty(frame, mode="percent", group=None):
    return bars(frame, "faculty", CATEGORIES["faculty"], "Quem respondeu: faculdades", mode, group)


def study_level(frame, mode="percent", group=None):
    title = "Quem respondeu: níveis de estudo"
    if frame.empty:
        return empty(title)
    if group:
        return bars(frame, "study_level", CATEGORIES["study_level"], title, mode, group)
    total = len(frame)
    labels_list, counts, percents = [], [], []
    for opt in CATEGORIES["study_level"]:
        c = int(frame.study_level.eq(opt).sum())
        labels_list.append(label(opt))
        counts.append(c)
        percents.append(100 * c / total)
    fig = go.Figure(go.Pie(
        labels=labels_list,
        values=percents if mode == "percent" else counts,
        hole=0.55,
        sort=True,
        marker=dict(colors=PALETTE, line=dict(color="white", width=2)),
        textinfo="label+percent" if mode == "percent" else "label+value",
        textposition="outside",
        customdata=list(zip(counts, percents, [total] * len(counts))),
        hovertemplate="%{label}<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Denominador=%{customdata[2]}<extra></extra>",
    ))
    finish(fig, title)
    fig.update_layout(showlegend=True, margin=dict(l=24, r=24, t=70, b=95))
    return fig


def faculty_study_level(frame, mode="percent"):
    title = "Composição demográfica: faculdade × nível de estudo"
    if frame.empty:
        return empty(title)
    total = len(frame)
    rows = []
    for fac in CATEGORIES["faculty"]:
        for lvl in CATEGORIES["study_level"]:
            count = int((frame.faculty.eq(fac) & frame.study_level.eq(lvl)).sum())
            if count > 0:
                rows.append({
                    "faculty": label(fac),
                    "study_level": label(lvl),
                    "count": count,
                    "percent": 100 * count / total,
                    "denominator": total,
                })
    if not rows:
        return empty(title)
    table = pd.DataFrame(rows)
    fig = px.treemap(
        table,
        path=["faculty", "study_level"],
        values="percent" if mode == "percent" else "count",
        color="faculty",
        color_discrete_sequence=["#0c3064", "#2b5c8f", "#4d79b1", "#8caed6"],
        custom_data=["count", "percent", "denominator"],
    )
    fig.update_traces(
        textinfo="label+percent root" if mode == "percent" else "label+value",
        hovertemplate="<b>%{label}</b><br>n=%{customdata[0]} · %{customdata[1]:.1f}% da amostra<br>Denominador=%{customdata[2]}<extra></extra>",
        marker=dict(cornerradius=4),
    )
    finish(fig, title)
    fig.update_layout(height=460, margin=dict(l=16, r=16, t=65, b=24))
    return fig
