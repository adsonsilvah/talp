"""Dashboard em página única e servidor WSGI de produção."""
import os
from functools import lru_cache
from dash import Dash, Input, Output, dcc, html
from src.config import ROOT, TITLE
from src.datasets.registry import available_datasets, get_dataset
from src.processing.metrics import apply_filters
from src.components.filters import filters, filter_options
from pages.dashboard import render


@lru_cache(maxsize=4)
def dataset_frame(key):
    return get_dataset(key).loader()


app = Dash(__name__, assets_folder=str(ROOT / "assets"), title=TITLE, update_title="Atualizando…")
server = app.server


def layout():
    datasets = available_datasets()
    if not datasets:
        return html.Main(html.H1("Base processada não encontrada"))
    frame = dataset_frame(next(iter(datasets)))
    return html.Main([
        html.Header(html.H1(TITLE), className="dashboard-header"),
        filters(frame),
        dcc.Loading(html.Div(id="dashboard-content"), type="circle", color="#0c3064"),
    ], className="dashboard")


app.layout = layout


@app.callback(
    Output("faculty", "options"), Output("faculty", "value"), Output("mode", "value"),
    Input("dataset", "value"), Input("reset", "n_clicks"),
)
def reset_filters(dataset_id, clicks):
    frame = dataset_frame(dataset_id)
    return filter_options(frame, "faculty"), [], "percent"


@app.callback(
    Output("dashboard-content", "children"),
    Input("dataset", "value"), Input("faculty", "value"), Input("mode", "value"),
)
def render_dashboard(dataset_id, faculties=None, *args, **kwargs):
    if len(args) >= 3:
        mode = args[2]
    elif len(args) == 1:
        mode = args[0]
    else:
        mode = kwargs.get("mode", "percent")
    dataset = get_dataset(dataset_id)
    frame = apply_filters(dataset_frame(dataset_id), faculties=faculties)
    return render(frame, dataset, mode)


@server.get("/healthz")
def health():
    available = available_datasets()
    if not available:
        return {"status": "error", "reason": "processed dataset unavailable"}, 503
    for key in available:
        dataset_frame(key)
    return {"status": "ok", "datasets": list(available)}


if __name__ == "__main__":
    app.run(host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8050")), debug=False)
