import plotly.graph_objects as go
from src.charts.common import bars, empty, finish
from src.datasets.schema import TOOLS, PURPOSES, ACADEMIC


def awareness(frame, mode="percent", group=None):
    return bars(frame, "awareness", TOOLS, "Quais ferramentas os estudantes conheciam?", mode, group, multi=True)


def purposes(frame, mode="percent", group=None):
    return bars(frame, "purposes", PURPOSES, "Para quais finalidades utilizaram ou consideraram utilizar?", mode, group, multi=True)


def confidence_academic(frame, mode="percent"):
    title = "Confiança na escrita × seleção da finalidade acadêmica"
    if frame.empty:
        return empty(title)
    values, custom = [[], []], [[], []]
    for score in range(1, 6):
        subset = frame[frame.confidence.eq(score)]
        n = len(subset)
        selected = int(subset.purposes.map(lambda v: ACADEMIC in v).sum())
        for row, count in enumerate((selected, n-selected)):
            pct = 100*count/n if n else None
            values[row].append((pct if mode == "percent" else count) if n else None)
            custom[row].append([count, pct, n])
    fig = go.Figure(go.Heatmap(
        x=[str(x) for x in range(1,6)], y=["Selecionou", "Não selecionou"], z=values, customdata=custom,
        colorscale=[[0, "#ffffff"], [.5, "#8caed6"], [1, "#0c3064"]], zmin=0, zmax=100 if mode == "percent" else None,
        texttemplate="%{z:.1f}%" if mode == "percent" else "%{z}", hoverongaps=False,
        colorbar=dict(title="% por nível" if mode == "percent" else "n"),
        hovertemplate="Confiança %{x} · %{y}<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Denominador deste nível=%{customdata[2]}<extra></extra>",
    ))
    fig.update_xaxes(title="Confiança na escrita (1 = baixa; 5 = alta)", type="category")
    fig.update_yaxes(title="Finalidade acadêmica")
    return finish(fig, title)
