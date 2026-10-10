import hashlib
import json
import pandas as pd
from src.datasets.schema import (COLUMN_MAP, CATEGORIES, CLOSED_FIELDS, TOOLS, PURPOSES, ATTITUDES)


def parse_multi(value, vocabulary):
    """Consome alternativas completas, inclusive suas vírgulas internas.

    Rejeita resíduos, alternativas repetidas e categorias não reconhecidas.
    Não transforma ausência de resposta em ausência de seleção.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Resposta multirresposta ausente ou inválida")
    remaining, selected = value.strip(), []
    while remaining:
        matches = [v for v in vocabulary if remaining == v or remaining.startswith(v + ",")]
        if len(matches) != 1:
            raise ValueError(f"Alternativa não reconhecida: {remaining!r}")
        option = matches[0]
        if option in selected:
            raise ValueError("Alternativa repetida")
        selected.append(option)
        remaining = remaining[len(option):]
        if remaining == ",":
            raise ValueError("Separador sem alternativa")
        remaining = remaining.removeprefix(",").lstrip()
    return selected


def read_raw(path):
    book = pd.ExcelFile(path)
    if book.sheet_names != ["Sheet 1"]:
        raise ValueError("Abas diferentes do contrato Liverpool 2023")
    frame = pd.read_excel(book)
    if list(frame.columns) != list(COLUMN_MAP):
        raise ValueError("Cabeçalhos ou ordem diferentes do contrato Liverpool 2023")
    return frame.rename(columns=COLUMN_MAP)


def clean(raw):
    for field, expected in CATEGORIES.items():
        if raw[field].isna().any() or not set(raw[field]).issubset(expected):
            raise ValueError(f"Categoria ausente/desconhecida em {field}")
    result = raw.loc[:, CLOSED_FIELDS].copy()
    result["awareness"] = raw.awareness.map(lambda v: parse_multi(v, TOOLS))
    result["purposes"] = raw.purposes.map(lambda v: parse_multi(v, PURPOSES))
    for field in ("grammar_attitude", "essay_attitude"):
        result[field] = raw[field].map(lambda v: v.split(" – ", 1)[0])
        if not set(result[field]).issubset(ATTITUDES):
            raise ValueError(f"Opinião desconhecida: {field}")
    result["confidence"] = result.confidence.astype(int)
    return result


def save_processed(frame, raw_path, destination):
    payload = {
        "schema_version": 1, "dataset_id": "liverpool2023",
        "source_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
        "respondents": len(frame), "records": frame.to_dict(orient="records"),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
