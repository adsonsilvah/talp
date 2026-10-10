import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.config import MIN_COMPARISON_N
from src.datasets.schema import label

PALETTE = ["#0c3064", "#ed1c24", "#4d79b1", "#a80e18", "#a4bfdf"]


def finish(fig, title, note="", horizontal=False):
    fig.update_layout(
        template="plotly_white", title=dict(text=title, font=dict(size=17), x=0),
        font=dict(family="Arial, sans-serif", size=13, color="#0c3064"),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=16, r=24, t=70, b=90), height=430,
        legend=dict(orientation="h", yanchor="top", y=-0.22, x=0, title_text="", traceorder="normal"),
        meta={"methodology": note}, hoverlabel=dict(bgcolor="white"),
    )
    fig.update_xaxes(automargin=True, fixedrange=False, zeroline=False)
    fig.update_yaxes(automargin=True, fixedrange=False, zeroline=False)
    if horizontal:
        fig.update_yaxes(autorange="reversed")
    return fig


def empty(title, message="Nenhuma resposta para esta combinação de filtros."):
    fig = go.Figure()
    fig.add_annotation(text=message, x=.5, y=.5, xref="paper", yref="paper", showarrow=False, font=dict(size=15))
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return finish(fig, title)


def groups(frame, group=None):
    if not group:
        return [("Todos no recorte", frame)]
    return [(label(value), subset) for value, subset in frame.groupby(group, sort=True) if len(subset) >= MIN_COMPARISON_N]


def bars(frame, field, options, title, mode="percent", group=None, multi=False, horizontal=True, ordered=False):
    if frame.empty:
        return empty(title)
    rows = []
    for group_label, subset in groups(frame, group):
        for option in options:
            count = int(subset[field].map(lambda values: option in values).sum()) if multi else int(subset[field].eq(option).sum())
            rows.append(dict(category=label(option), group=group_label, count=count, denominator=len(subset), percent=100*count/len(subset)))
    if not rows:
        return empty(title, f"Nenhum grupo com pelo menos {MIN_COMPARISON_N} respostas neste recorte.")
    table = pd.DataFrame(rows)
    order = [label(v) for v in options]
    if not ordered and not group:
        order = table.sort_values("count", ascending=False, kind="stable").category.tolist()
    value = "percent" if mode == "percent" else "count"
    fig = px.bar(table, x=value if horizontal else "category", y="category" if horizontal else value,
                 color="group" if group else None, orientation="h" if horizontal else "v", barmode="group",
                 category_orders={"category": order}, color_discrete_sequence=PALETTE,
                 custom_data=["count", "percent", "denominator", "group"],
                 labels={value: "% dos respondentes" if mode == "percent" else "Respondentes", "category": "", "group": "Grupo"})
    category_axis = "y" if horizontal else "x"
    details = "<br>Multirresposta: a soma pode ultrapassar 100%." if multi else ""
    if group:
        sizes = frame.groupby(group).size()
        omitted = sizes[sizes < MIN_COMPARISON_N]
        details += f"<br>Grupos n<30 omitidos: {len(omitted)} ({int(omitted.sum())} respostas)."
    fig.update_traces(hovertemplate=f"%{{{category_axis}}}<br>%{{customdata[3]}}<br>n=%{{customdata[0]}} · %{{customdata[1]:.1f}}%<br>Denominador=%{{customdata[2]}}" + details + "<extra></extra>")
    if not group:
        fig.update_traces(marker_color=PALETTE[0])
    finish(fig, title, horizontal=horizontal)
    if group:
        fig.update_layout(height=max(540, len(options)*len(table.group.unique())*22 + 210))
    return fig
