"""Carregamento de produção: somente dados fechados processados."""
import json
import pandas as pd
from src.config import PROCESSED_PATH
from src.datasets.schema import CLOSED_FIELDS, CATEGORIES, TOOLS, PURPOSES, ATTITUDES


def validate(frame):
    if list(frame.columns) != list(CLOSED_FIELDS) or len(frame) != 2555:
        raise ValueError("Estrutura ou total inesperado na base processada")
    for field in CLOSED_FIELDS:
        if frame[field].isna().any():
            raise ValueError(f"Ausências não esperadas: {field}")
        if field in ("awareness", "purposes"):
            vocab = TOOLS if field == "awareness" else PURPOSES
            if not frame[field].map(lambda v: isinstance(v, list) and bool(v) and all(isinstance(x, str) for x in v) and len(v) == len(set(v)) and set(v).issubset(vocab)).all():
                raise ValueError(f"Multirresposta inválida: {field}")
        else:
            vocab = ATTITUDES if field.endswith("attitude") else CATEGORIES[field]
            if not set(frame[field]).issubset(vocab):
                raise ValueError(f"Categoria inválida: {field}")
    return frame


def load(path=PROCESSED_PATH):
    payload = json.loads(path.read_text())
    if payload.get("schema_version") != 1 or payload.get("dataset_id") != "liverpool2023" or payload.get("respondents") != 2555:
        raise ValueError("Metadados incompatíveis")
    return validate(pd.DataFrame(payload["records"], columns=list(payload["records"][0])))
