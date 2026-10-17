"""Exportação opcional: Kaleido/Chrome nunca são importados pelo servidor."""
import argparse
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from inspect import signature
from src.config import ROOT
from src.datasets.registry import get_dataset
from src.processing.metrics import apply_filters
from src.charts.awareness import awareness, purposes, confidence_academic, tools_academic, repertoire
from src.charts.profile import confidence, faculty, study_level, faculty_study_level
from src.charts.academic_integrity import acceptance, attitude_matrix
from src.charts.policies import policies, policy_integrity

FIGURES = {
    "v1": awareness,
    "v2": confidence,
    "v3": purposes,
    "v4": acceptance,
    "v5": confidence_academic,
    "v6": policies,
    "v7": attitude_matrix,
    "v8": policy_integrity,
    "v9": tools_academic,
    "v10": repertoire,
    "profile_faculty": faculty,
    "profile_level": study_level,
    "profile_cross": faculty_study_level,
}
NOTES = {
    "v1": "Multirresposta: soma pode ultrapassar 100%. Denominador = total do recorte.",
    "v2": "Escala ordinal: 1 = nada confiante; 5 = muito confiante. Denominador = total do recorte.",
    "v3": "Utilizou OU considerou utilizar. Multirresposta; soma pode ultrapassar 100%. Denominador = total do recorte.",
    "v4": "Cada cenário soma 100% do recorte. Outro incluído no denominador, separado das cinco categorias ordinais.",
    "v5": "Percentuais por coluna de confiança. Não selecionar não significa nunca usar. Associação não implica causa.",
    "v6": "Escolha única. Denominador = total do recorte, incluindo Outro.",
    "v7": "Cruzamento individual 6×6 entre apoio gramatical e redação integral. Denominador = total do recorte.",
    "v8": "Distribuição de opinião sobre redação integral dentro de cada preferência de política (grupos n≥30).",
    "v9": "Proporção com finalidade acadêmica dentro dos que conhecem cada ferramenta (denominador = grupo da ferramenta).",
    "v10": "Quantidade de ferramentas conhecidas por estudante (excluindo 'Nenhuma das opções'). Denominador = total do recorte.",
    "profile_faculty": "Distribuição da amostra voluntária por faculdade. Denominador = total do recorte.",
    "profile_level": "Distribuição da amostra voluntária por nível de estudo. Denominador = total do recorte.",
    "profile_cross": "Composição demográfica cruzada (faculdade × nível de estudo, grupos n≥30).",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["png", "svg"], default="png")
    parser.add_argument("--charts", nargs="+", choices=list(FIGURES), default=list(FIGURES))
    parser.add_argument("--output", type=Path, default=ROOT / "exports")
    parser.add_argument("--mode", choices=["percent", "count"], default="percent")
    parser.add_argument("--group", choices=["none", "faculty", "study_level", "confidence"], default="none")
    parser.add_argument("--faculty", action="append")
    parser.add_argument("--level", action="append")
    parser.add_argument("--confidence", type=int, choices=range(1, 6), action="append")
    args = parser.parse_args()
    dataset = get_dataset("liverpool2023")
    frame = apply_filters(dataset.loader(), args.faculty, args.level, args.confidence)
    if frame.empty:
        parser.error("Filtros sem respostas; nenhuma imagem gerada.")
    args.output.mkdir(parents=True, exist_ok=True)
    local_chrome = ROOT / ".local/chrome/chrome-linux64/chrome"
    if local_chrome.is_file():
        os.environ.setdefault("BROWSER_PATH", str(local_chrome))
    group = None if args.group == "none" else args.group
    try:
        import kaleido  # noqa: F401 — dependência deliberadamente opcional
        for name in args.charts:
            builder = FIGURES[name]
            params = signature(builder).parameters
            fig = builder(frame, mode=args.mode, group=group) if "group" in params and group else builder(frame, mode=args.mode)
            note = NOTES[name]
            if name == "v5":
                totals = ", ".join(f"{score}: n={int(frame.confidence.eq(score).sum())}" for score in range(1, 6))
                note += "<br>Denominadores por confiança: " + totals
            fig.update_layout(margin=dict(b=210), legend=dict(y=-0.1), paper_bgcolor="white", plot_bgcolor="white")
            fig.add_annotation(
                x=0, y=-0.26, xref="paper", yref="paper", xanchor="left", showarrow=False, align="left",
                font=dict(size=11),
                text=f"Liverpool 2023 · n={len(frame)} · Johnston et al. (2024) · DOI: 10.1007/s40979-024-00149-4<br>{note}",
            )
            suffix = f"_by_{group}" if group and "group" in params else ""
            target = args.output / f"{name}{suffix}.{args.format}"
            fig.write_image(target, width=1400, height=800, scale=2)
            print(f"Exportado: {target}")
        (args.output / "README.md").write_text(
            f"# Figuras Liverpool 2023\n\nRespondentes: {len(frame)}.\n\n"
            f"Filtros originais: faculdade={args.faculty}; nível={args.level}; confiança={args.confidence}; agrupamento={group}; modo={args.mode}.\n\n"
            f"Percentuais, denominadores por grupo de confiança em V5. Fonte: {dataset.reference}.\n"
        )
    except (ImportError, RuntimeError) as exc:
        raise SystemExit(
            "Exportação indisponível. Instale requirements-export.txt e um Chrome/Chromium compatível. "
            "Execute .venv/bin/plotly_get_chrome se necessário. Detalhe: " + str(exc)
        ) from exc


if __name__ == "__main__":
    main()
