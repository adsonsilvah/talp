import plotly.graph_objects as go
from src.charts.common import empty, finish, groups
from src.datasets.schema import ATTITUDES, label

COLORS = ["#0c3064", "#8caed6", "#cbd5e1", "#f5a1a5", "#ed1c24", "#e2e8f0"]


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


def attitude_matrix(frame, mode="percent"):
    title = "Matriz de transição ética: apoio gramatical × redação integral"
    if frame.empty:
        return empty(title)
    total = len(frame)
    labels = [label(v) for v in ATTITUDES]
    values, custom = [], []
    for g_att in ATTITUDES:
        row_val, row_custom = [], []
        for e_att in ATTITUDES:
            count = int((frame.grammar_attitude.eq(g_att) & frame.essay_attitude.eq(e_att)).sum())
            pct = 100 * count / total
            row_val.append(pct if mode == "percent" else count)
            row_custom.append([count, pct, total])
        values.append(row_val)
        custom.append(row_custom)
    fig = go.Figure(go.Heatmap(
        x=labels, y=labels, z=values, customdata=custom,
        colorscale=[[0, "#ffffff"], [0.4, "#8caed6"], [1, "#0c3064"]],
        zmin=0,
        texttemplate="%{z:.1f}%" if mode == "percent" else "%{z}",
        colorbar=dict(title="% do total" if mode == "percent" else "n"),
        hovertemplate="Apoio gramatical: %{y}<br>Redação integral: %{x}<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Denominador=%{customdata[2]}<extra></extra>",
    ))
    fig.update_xaxes(title="Redação integral com IA", type="category")
    fig.update_yaxes(title="Apoio gramatical com IA", type="category", autorange="reversed")
    fig = finish(fig, title)
    fig.update_layout(height=520, margin=dict(l=24, r=24, t=70, b=110))
    return fig
