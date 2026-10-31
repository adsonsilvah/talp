from dash import dcc, html
from src.datasets.schema import label
from src.datasets.registry import available_datasets


DROPDOWN_LABELS = {"select_all":"Selecionar todos", "deselect_all":"Desmarcar todos", "selected_count":"selecionados", "search":"Buscar", "clear_search":"Limpar busca", "clear_selection":"Limpar seleção", "no_options_found":"Nenhuma opção encontrada"}


def filter_options(frame, field):
    return [{"label":label(v), "value":v} for v in sorted(frame[field].unique())] if field in frame else []


def filters(frame):
    datasets = available_datasets()
    return html.Section([
        html.Div([
            html.Label("Base de dados", htmlFor="dataset"),
            dcc.Dropdown(
                labels=DROPDOWN_LABELS,
                id="dataset",
                options=[{"label": d.name, "value": d.id} for d in datasets.values()],
                value=next(iter(datasets), None),
                clearable=False,
            ),
        ], className="filter-item"),
        html.Div([
            html.Label("Faculdade", htmlFor="faculty"),
            dcc.Dropdown(
                labels=DROPDOWN_LABELS,
                id="faculty",
                options=filter_options(frame, "faculty"),
                multi=True,
                placeholder="Todas as faculdades",
            ),
        ], className="filter-item"),
        html.Div([
            html.Label("Unidade das métricas", htmlFor="mode"),
            dcc.RadioItems(
                id="mode",
                options=[
                    {"label": " Percentuais", "value": "percent"},
                    {"label": " Contagens", "value": "count"},
                ],
                value="percent",
                inline=True,
            ),
        ], className="unit-control"),
        html.Button("Restaurar filtros", id="reset", n_clicks=0, className="secondary-button"),
    ], className="filters", **{"aria-label": "Filtros globais"})
