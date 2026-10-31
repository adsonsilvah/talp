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


def faculty_study_level(frame, mode="percent", *args, **kwargs):
    title = "Composição demográfica: faculdade × nível de estudo"
    if frame.empty:
        return empty(title)
    fac_order = [
        "Humanities and Social Sciences",
        "Health and Life Sciences",
        "Science and Engineering",
        "Not sure",
    ]
    level_order = [
        "Undergraduate",
        "Postgraduate - Taught",
        "Postgraduate - Research",
        "Foundation",
        "Not sure",
    ]
    present_facs = [f for f in fac_order if (frame.faculty == f).any()]
    if not present_facs:
        present_facs = sorted(frame.faculty.unique())

    fig = go.Figure()
    palette = ["#0c3064", "#2b5c8f", "#4d79b1", "#a80e18", "#718096"]

    for idx, lvl in enumerate(level_order):
        c_name = label(lvl)
        x_vals, y_vals, texts, custom = [], [], [], []
        for fac in present_facs:
            sub = frame[frame.faculty == fac]
            n_fac = len(sub)
            count = int((sub.study_level == lvl).sum())
            pct = 100 * count / n_fac if n_fac else 0
            x_vals.append(label(fac))
            y_vals.append(pct if mode == "percent" else count)
            texts.append(f"n={count}<br>({pct:.1f}%)" if count > 0 else "")
            custom.append([count, pct, n_fac, label(fac)])

        if sum(c[0] for c in custom) > 0:
            fig.add_trace(go.Bar(
                x=x_vals,
                y=y_vals,
                name=c_name,
                orientation="v",
                marker_color=palette[idx % len(palette)],
                text=texts,
                textposition="outside",
                cliponaxis=False,
                textfont=dict(size=12, color="#0c3064", family="Arial, sans-serif"),
                customdata=custom,
                hovertemplate=(
                    "%{customdata[3]}<br>"
                    "<b>" + c_name + "</b><br>"
                    "Quantidade exata: n=%{customdata[0]}<br>"
                    "Proporção: %{customdata[1]:.1f}% da faculdade<br>"
                    "Total da faculdade=%{customdata[2]}<extra></extra>"
                ),
            ))

    fig.update_layout(
        barmode="group",
        height=520,
        legend=dict(orientation="h", yanchor="top", y=-0.18, x=0, title_text=""),
        margin=dict(l=16, r=32, t=70, b=90),
    )
    if fig.data:
        if mode == "percent":
            max_y = max([row[1] for trace in fig.data for row in trace.customdata] or [80])
            fig.update_yaxes(range=[0, min(100, max_y * 1.25)], title="% dos estudantes dentro de cada faculdade", ticksuffix="%")
        else:
            max_y = max([row[0] for trace in fig.data for row in trace.customdata] or [800])
            fig.update_yaxes(range=[0, max_y * 1.25], title="Respondentes (quantidade exata)")
    fig.update_xaxes(title="Faculdade")

    finish(fig, title, horizontal=False)
    return fig
