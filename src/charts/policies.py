from src.charts.common import bars, empty, finish
from src.config import MIN_COMPARISON_N
from src.datasets.schema import POLICIES, label
import plotly.graph_objects as go


def policies(frame, mode="percent", group=None):
    return bars(frame, "policy", POLICIES, "Quem deve definir as regras de uso?", mode, group)


def policy_integrity(frame, mode="percent", *args, **kwargs):
    title = "Preferência de política × aceitação de uso (apoio gramatical vs. redação integral)"
    if frame.empty:
        return empty(title)
    rows = []
    for pol in POLICIES:
        subset = frame[frame.policy.eq(pol)]
        n = len(subset)
        if n == 0:
            continue
        gram_n = int(subset.grammar_attitude.isin(["Supportive", "Somewhat supportive"]).sum())
        essay_n = int(subset.essay_attitude.isin(["Supportive", "Somewhat supportive"]).sum())
        rows.append({
            "policy": label(pol),
            "n": n,
            "gram_n": gram_n,
            "gram_pct": 100 * gram_n / n if n else 0,
            "essay_n": essay_n,
            "essay_pct": 100 * essay_n / n if n else 0,
        })
    if not rows:
        return empty(title)

    rows.sort(key=lambda r: r["gram_pct"], reverse=True)
    y_labels = [r["policy"] for r in rows]
    gram_vals = [r["gram_pct"] if mode == "percent" else r["gram_n"] for r in rows]
    essay_vals = [r["essay_pct"] if mode == "percent" else r["essay_n"] for r in rows]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=y_labels,
        x=gram_vals,
        name="Favorável ao apoio gramatical",
        orientation="h",
        marker_color="#0c3064",
        text=[f"{v:.1f}%" if mode == "percent" else str(v) for v in gram_vals],
        textposition="outside",
        customdata=[[r["gram_n"], r["gram_pct"], r["n"]] for r in rows],
        hovertemplate="%{y}<br>Favorável ao apoio gramatical<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Total na política=%{customdata[2]}<extra></extra>",
    ))
    fig.add_trace(go.Bar(
        y=y_labels,
        x=essay_vals,
        name="Favorável à redação integral",
        orientation="h",
        marker_color="#ed1c24",
        text=[f"{v:.1f}%" if mode == "percent" else str(v) for v in essay_vals],
        textposition="outside",
        customdata=[[r["essay_n"], r["essay_pct"], r["n"]] for r in rows],
        hovertemplate="%{y}<br>Favorável à redação integral<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Total na política=%{customdata[2]}<extra></extra>",
    ))

    fig.update_layout(
        barmode="group",
        height=480,
        legend=dict(orientation="h", yanchor="top", y=-0.18, x=0, title_text=""),
        margin=dict(l=16, r=48, t=70, b=90),
    )
    if mode == "percent":
        fig.update_xaxes(range=[0, 100], title="% favoráveis ou parcialmente favoráveis dentro de cada política", ticksuffix="%")
    else:
        max_v = max(gram_vals + essay_vals + [1])
        fig.update_xaxes(range=[0, max_v * 1.15], title="Respondentes favoráveis")

    finish(fig, title, horizontal=True)
    return fig
