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


def tools_academic(frame, mode="percent"):
    title = "Conhecimento da ferramenta × conversão para finalidade acadêmica"
    if frame.empty:
        return empty(title)
    from src.charts.common import PALETTE
    from src.datasets.schema import label
    total = len(frame)
    rows = []
    for tool in TOOLS:
        if tool == "None of the above":
            continue
        subset = frame[frame.awareness.map(lambda v: tool in v)]
        n_known = len(subset)
        if not n_known:
            continue
        n_acad = int(subset.purposes.map(lambda v: ACADEMIC in v).sum())
        rows.append({
            "tool": label(tool),
            "known_n": n_known,
            "known_pct": 100 * n_known / total,
            "acad_n": n_acad,
            "acad_pct": 100 * n_acad / n_known,
            "total": total,
        })
    if not rows:
        return empty(title)
    x_vals = [r["known_pct"] if mode == "percent" else r["known_n"] for r in rows]
    y_vals = [r["acad_pct"] if mode == "percent" else r["acad_n"] for r in rows]
    max_acad = max(r["acad_n"] for r in rows) or 1
    sizes = [max(16, 46 * (r["acad_n"] / max_acad) ** 0.5) for r in rows]
    fig = go.Figure(go.Scatter(
        x=x_vals, y=y_vals,
        mode="markers+text",
        text=[r["tool"] for r in rows],
        textposition="top center",
        marker=dict(
            size=sizes,
            color=PALETTE[0],
            opacity=0.82,
            line=dict(color=PALETTE[1], width=2),
        ),
        customdata=[[r["known_n"], r["known_pct"], r["acad_n"], r["acad_pct"], r["total"]] for r in rows],
        hovertemplate=(
            "<b>%{text}</b><br>"
            "Conhecem a ferramenta: n=%{customdata[0]} (%{customdata[1]:.1f}% do total=%{customdata[4]})<br>"
            "Selecionaram finalidade acadêmica: n=%{customdata[2]} (%{customdata[3]:.1f}% dos que conhecem)<extra></extra>"
        ),
    ))
    if mode == "percent":
        fig.update_xaxes(title="Conhecimento da ferramenta (% do recorte)", ticksuffix="%", range=[-5, 105])
        fig.update_yaxes(title="Finalidade acadêmica (% dos que conhecem)", ticksuffix="%", range=[0, 105])
    else:
        max_x = max(x_vals + [1])
        max_y = max(y_vals + [1])
        fig.update_xaxes(title="Estudantes que conhecem a ferramenta (n)", range=[-max_x * 0.08, max_x * 1.15])
        fig.update_yaxes(title="Estudantes com finalidade acadêmica (n)", range=[0, max_y * 1.2])
    return finish(fig, title)


def repertoire(frame, mode="percent", group=None):
    title = "Repertório: número de ferramentas conhecidas por estudante"
    if frame.empty:
        return empty(title)
    from src.charts.common import PALETTE, groups
    copy = frame.copy()
    copy["tool_count"] = copy.awareness.map(
        lambda v: "4+" if sum(1 for x in v if x != "None of the above") >= 4 else str(sum(1 for x in v if x != "None of the above"))
    )
    categories = ["0", "1", "2", "3", "4+"]
    grouped = groups(copy, group)
    if not grouped:
        return empty(title, "Nenhum grupo com pelo menos 30 respostas neste recorte.")
    fig = go.Figure()
    for idx, (group_label, subset) in enumerate(grouped):
        n = len(subset)
        counts = [int(subset.tool_count.eq(cat).sum()) for cat in categories]
        percents = [100 * c / n for c in counts]
        y_vals = percents if mode == "percent" else counts
        color = PALETTE[idx % len(PALETTE)]
        fig.add_trace(go.Scatter(
            x=categories,
            y=y_vals,
            name=group_label,
            mode="lines+markers+text" if not group else "lines+markers",
            line=dict(color=color, width=3),
            marker=dict(size=10, color=color, line=dict(color="white", width=1.5)),
            fill="tozeroy" if not group else "none",
            fillcolor="rgba(12, 48, 100, 0.12)" if not group else None,
            text=[f"{p:.1f}%" if mode == "percent" else str(c) for c, p in zip(counts, percents)] if not group else None,
            textposition="top center",
            customdata=[[c, p, n, group_label] for c, p in zip(counts, percents)],
            hovertemplate="Ferramentas conhecidas: %{x}<br>%{customdata[3]}<br>n=%{customdata[0]} · %{customdata[1]:.1f}%<br>Denominador=%{customdata[2]}<extra></extra>",
        ))
    max_y = max((max(trace.y) for trace in fig.data if len(trace.y)), default=1)
    fig.update_xaxes(title="Quantidade de ferramentas conhecidas (0 a 4+)", type="category", range=[-0.35, 4.35])
    fig.update_yaxes(
        title="% dos respondentes" if mode == "percent" else "Respondentes",
        ticksuffix="%" if mode == "percent" else "",
        range=[0, max_y * 1.22 if max_y else 10],
    )
    finish(fig, title)
    fig.update_layout(showlegend=bool(group))
    return fig
