"""Exportação opcional: Kaleido/Chrome nunca são importados pelo servidor."""
import argparse
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config import ROOT
from src.datasets.registry import get_dataset
from src.processing.metrics import apply_filters
from src.charts.awareness import awareness, purposes, confidence_academic
from src.charts.profile import confidence
from src.charts.academic_integrity import acceptance
from src.charts.policies import policies

FIGURES = {"v1":awareness, "v2":confidence, "v3":purposes, "v4":acceptance, "v5":confidence_academic, "v6":policies}
NOTES = {
    "v1":"Multirresposta: soma pode ultrapassar 100%. Denominador = total do recorte.",
    "v2":"Escala ordinal: 1 = nada confiante; 5 = muito confiante. Denominador = total do recorte.",
    "v3":"Utilizou OU considerou utilizar. Multirresposta; soma pode ultrapassar 100%. Denominador = total do recorte.",
    "v4":"Cada cenário soma 100% do recorte. Outro incluído no denominador, separado das cinco categorias ordinais.",
    "v5":"Percentuais por coluna de confiança. Não selecionar não significa nunca usar. Associação não implica causa.",
    "v6":"Escolha única. Denominador = total do recorte, incluindo Outro.",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["png","svg"], default="png")
    parser.add_argument("--charts", nargs="+", choices=list(FIGURES), default=list(FIGURES))
    parser.add_argument("--output", type=Path, default=ROOT/"exports")
    parser.add_argument("--faculty", action="append")
    parser.add_argument("--level", action="append")
    parser.add_argument("--confidence", type=int, choices=range(1,6), action="append")
    args = parser.parse_args()
    dataset = get_dataset("liverpool2023")
    frame = apply_filters(dataset.loader(),args.faculty,args.level,args.confidence)
    if frame.empty:
        parser.error("Filtros sem respostas; nenhuma imagem gerada.")
    args.output.mkdir(parents=True, exist_ok=True)
    local_chrome = ROOT / ".local/chrome/chrome-linux64/chrome"
    if local_chrome.is_file():
        os.environ.setdefault("BROWSER_PATH", str(local_chrome))
    try:
        import kaleido  # noqa: F401 — dependência deliberadamente opcional
        for name in args.charts:
            fig = FIGURES[name](frame)
            note = NOTES[name]
            if name == "v5":
                totals = ", ".join(f"{score}: n={int(frame.confidence.eq(score).sum())}" for score in range(1,6))
                note += "<br>Denominadores por confiança: " + totals
            fig.update_layout(margin=dict(b=210), legend=dict(y=-.1), paper_bgcolor="white", plot_bgcolor="white")
            fig.add_annotation(x=0,y=-.26,xref="paper",yref="paper",xanchor="left",showarrow=False,align="left",font=dict(size=11),text=f"Liverpool 2023 · n={len(frame)} · Johnston et al. (2024) · DOI: 10.1007/s40979-024-00149-4<br>{note}")
            fig.write_image(args.output/f"{name}.{args.format}",width=1400,height=800,scale=2)
            print(f"Exportado: {args.output/name}.{args.format}")
        (args.output/"README.md").write_text(f"# Figuras Liverpool 2023\n\nRespondentes: {len(frame)}.\n\nFiltros originais: faculdade={args.faculty}; nível={args.level}; confiança={args.confidence}.\n\nPercentuais, denominadores por grupo de confiança em V5. Fonte: {dataset.reference}.\n")
    except (ImportError, RuntimeError) as exc:
        raise SystemExit("Exportação indisponível. Instale requirements-export.txt e um Chrome/Chromium compatível. Execute .venv/bin/plotly_get_chrome se necessário. Detalhe: "+str(exc)) from exc


if __name__ == "__main__":
    main()
