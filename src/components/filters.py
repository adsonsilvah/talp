from dash import dcc, html
from src.datasets.schema import label
from src.datasets.registry import available_datasets


DROPDOWN_LABELS = {"select_all":"Selecionar todos", "deselect_all":"Desmarcar todos", "selected_count":"selecionados", "search":"Buscar", "clear_search":"Limpar busca", "clear_selection":"Limpar seleção", "no_options_found":"Nenhuma opção encontrada"}


def filter_options(frame, field):
    return [{"label":label(v), "value":v} for v in sorted(frame[field].unique())] if field in frame else []


def filters(frame):
    datasets = available_datasets()
    return html.Section([
        html.Div([html.Label("Base de dados", htmlFor="dataset"), dcc.Dropdown(labels=DROPDOWN_LABELS, id="dataset", options=[{"label": d.name, "value": d.id} for d in datasets.values()], value=next(iter(datasets), None), clearable=False)]),
        html.Div([html.Label("Faculdade", htmlFor="faculty"), dcc.Dropdown(labels=DROPDOWN_LABELS, id="faculty", options=filter_options(frame,"faculty"), multi=True, placeholder="Todas as faculdades")]),
        html.Div([html.Label("Nível de estudo", htmlFor="study-level"), dcc.Dropdown(labels=DROPDOWN_LABELS, id="study-level", options=filter_options(frame,"study_level"), multi=True, placeholder="Todos os níveis")]),
        html.Div([html.Label("Confiança na escrita", htmlFor="confidence"), dcc.Dropdown(labels=DROPDOWN_LABELS, id="confidence", options=filter_options(frame,"confidence"), multi=True, placeholder="Todos: 1–5")]),
        html.Button("Restaurar filtros", id="reset", n_clicks=0, className="secondary-button"),
        html.Div([html.Label("Unidade das barras e heatmap", htmlFor="mode"), dcc.RadioItems(id="mode", options=[{"label":" Percentuais", "value":"percent"},{"label":" Contagens", "value":"count"}], value="percent", inline=True)], className="unit-control"),
        html.Div([html.Label("Agrupar gráficos · n≥30", htmlFor="group"), dcc.Dropdown(labels=DROPDOWN_LABELS, id="group", options=[{"label":"Sem agrupamento", "value":"none"},{"label":"Por faculdade", "value":"faculty"},{"label":"Por nível de estudo", "value":"study_level"},{"label":"Por confiança (integridade)", "value":"confidence"}], value="none", clearable=False)], className="group-control"),
    ], className="filters", **{"aria-label":"Filtros globais"})
