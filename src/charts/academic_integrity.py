import plotly.graph_objects as go
from src.charts.common import empty, finish, groups
from src.datasets.schema import ATTITUDES, label

COLORS = ["#0c3064", "#8caed6", "#ffffff", "#f5a1a5", "#ed1c24", "#ffffff"]


def acceptance(frame, mode="percent", group=None):
    title = "Apoio gramatical e redação integral: onde está o limite?"
    if frame.empty:
        return empty(title)
    grouped = groups(frame, group)
    if not grouped:
        return empty(title, "Nenhum grupo com pelo menos 30 respostas neste recorte.")
    details = ""
    if group:
        sizes = frame.groupby(group).size()
        omitted = sizes[sizes < 30]
        details = f"<br>Grupos n<30 omitidos: {len(omitted)} ({int(omitted.sum())} respostas)."
    fig = go.Figure()
    for category, color in zip(ATTITUDES, COLORS):
        counts, percents, totals, labels = [], [], [], []
        for group_label, subset in grouped:
            for field, scenario in (("grammar_attitude", "Apoio gramatical"), ("essay_attitude", "Redação integral")):
                count = int(subset[field].eq(category).sum())
                counts.append(count); percents.append(100*count/len(subset)); totals.append(len(subset))
                labels.append(f"{group_label}<br>{scenario}" if group else scenario)
        fig.add_bar(name=label(category), y=labels, x=percents, orientation="h", marker_color=color,
                    marker_line=dict(color="#0c3064", width=.6),
                    marker_pattern_shape="/" if category == "Other" else "",
                    customdata=list(zip(counts, percents, totals)),
                    hovertemplate=label(category)+"<br>%{y}<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Denominador=%{customdata[2]}"+details+"<extra></extra>")
    fig.update_layout(barmode="stack")
    fig.update_xaxes(range=[0,100], title="% dos respondentes · inclui Outro", ticksuffix="%")
    finish(fig, title, horizontal=True)
    fig.update_layout(height=max(540, len(grouped)*125+320), margin_b=170, legend=dict(y=-.23, traceorder="normal"))
    return fig
