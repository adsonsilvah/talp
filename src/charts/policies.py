from src.charts.common import bars, empty, finish
from src.config import MIN_COMPARISON_N
from src.datasets.schema import POLICIES, label
import plotly.graph_objects as go


def policies(frame, mode="percent", group=None):
    return bars(frame, "policy", POLICIES, "Quem deve definir as regras de uso?", mode, group)


def policy_integrity(frame, mode="percent"):
    title = "Preferência de política × aceitação de uso (apoio gramatical vs. redação integral)"
    if frame.empty:
        return empty(title)
    rows = []
    for pol in POLICIES:
        subset = frame[frame.policy.eq(pol)]
        n = len(subset)
        if n < MIN_COMPARISON_N:
            continue
        gram_n = int(subset.grammar_attitude.isin(["Supportive", "Somewhat supportive"]).sum())
        essay_n = int(subset.essay_attitude.isin(["Supportive", "Somewhat supportive"]).sum())
        rows.append({
            "policy": label(pol),
            "n": n,
            "gram_n": gram_n,
            "gram_pct": 100 * gram_n / n,
            "essay_n": essay_n,
            "essay_pct": 100 * essay_n / n,
        })
    if not rows:
        return empty(title, f"Nenhuma política com pelo menos {MIN_COMPARISON_N} respostas neste recorte.")
    key = "gram_pct" if mode == "percent" else "gram_n"
    rows.sort(key=lambda r: r[key], reverse=True)
    y_labels = [r["policy"] for r in rows]
    gram_vals = [r["gram_pct"] if mode == "percent" else r["gram_n"] for r in rows]
    essay_vals = [r["essay_pct"] if mode == "percent" else r["essay_n"] for r in rows]

    fig = go.Figure()
    for r, y, x0, x1 in zip(rows, y_labels, essay_vals, gram_vals):
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y, y], mode="lines",
            line=dict(color="#cbd5e1", width=5),
            hoverinfo="skip", showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=essay_vals, y=y_labels, mode="markers+text",
        name="Favorável à redação integral",
        marker=dict(color="#ed1c24", size=14, line=dict(color="white", width=1.5)),
        text=[f"{r['essay_pct']:.0f}%" if mode == "percent" else str(r["essay_n"]) for r in rows],
        textposition="middle left",
        customdata=[[r["essay_n"], r["essay_pct"], r["n"]] for r in rows],
        hovertemplate="%{y}<br>Favorável à redação integral<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Total na política=%{customdata[2]}<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=gram_vals, y=y_labels, mode="markers+text",
        name="Favorável ao apoio gramatical",
        marker=dict(color="#0c3064", size=14, line=dict(color="white", width=1.5)),
        text=[f"{r['gram_pct']:.0f}%" if mode == "percent" else str(r["gram_n"]) for r in rows],
        textposition="middle right",
        customdata=[[r["gram_n"], r["gram_pct"], r["n"]] for r in rows],
        hovertemplate="%{y}<br>Favorável ao apoio gramatical<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Total na política=%{customdata[2]}<extra></extra>",
    ))
    if mode == "percent":
        fig.update_xaxes(range=[-8, 105], title="% favoráveis ou parcialmente favoráveis dentro de cada política", ticksuffix="%")
    else:
        max_v = max(gram_vals + [1])
        fig.update_xaxes(range=[-max_v * 0.1, max_v * 1.15], title="Respondentes favoráveis ou parcialmente favoráveis")
    finish(fig, title, horizontal=True)
    fig.update_layout(height=450, margin=dict(l=20, r=32, t=70, b=110))
    return fig
