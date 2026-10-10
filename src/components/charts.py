from dash import dcc, html


def chart_card(figure, wide=False):
    title = figure.layout.title.text
    figure.update_layout(title_text=None, margin_t=25)
    return html.Section([
        html.H3(title, className="chart-title"),
        dcc.Graph(figure=figure, responsive=True, config={"displaylogo": False, "locale": "pt-BR", "locales": {"pt-BR": {"dictionary": {"Download plot as a PNG": "Baixar gráfico em PNG", "Zoom": "Ampliar", "Pan": "Mover", "Zoom in": "Aproximar", "Zoom out": "Afastar", "Autoscale": "Ajustar escala", "Reset axes": "Restaurar eixos"}, "format": {"decimal": ",", "thousands": ".", "grouping": [3]}}}, "modeBarButtonsToRemove": ["sendDataToCloud", "sendChartToCloud", "select2d", "lasso2d"], "toImageButtonOptions": {"format": "png", "scale": 2}}, style={"width":"100%", "height":f"{figure.layout.height or 430}px"}),
    ], className="chart-card" + (" wide" if wide else ""))


def unavailable():
    return html.Div("Esta base não oferece os atributos necessários para esta análise.", className="notice")
