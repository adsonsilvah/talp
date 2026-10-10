"""Registro explícito: novas bases exigem adaptador, metadados e capacidades."""
from dataclasses import dataclass
from typing import Callable
import pandas as pd
from src.config import PROCESSED_PATH
from src.datasets.liverpool import load
from src.datasets.schema import CLOSED_FIELDS


@dataclass(frozen=True)
class Dataset:
    id: str
    name: str
    collection_year: int
    institution: str
    country: str
    reference: str
    respondents: int
    variables: tuple[str, ...]
    limitations: tuple[str, ...]
    loader: Callable[[], pd.DataFrame]
    available: Callable[[], bool]

    def supports(self, *fields):
        return set(fields).issubset(self.variables)


REGISTRY = {
    "liverpool2023": Dataset(
        "liverpool2023", "Liverpool 2023", 2023, "University of Liverpool", "Reino Unido",
        "https://doi.org/10.1007/s40979-024-00149-4", 2555, CLOSED_FIELDS,
        ("Amostra voluntária de uma instituição; sem representatividade garantida.",
         "Uso e consideração do uso não podem ser distinguidos.",
         "Associações observacionais não demonstram causalidade.",
         "Coleta de 2023: não descreve o cenário atual de ferramentas de IA."),
        load, PROCESSED_PATH.is_file,
    )
}


def available_datasets():
    return {key: value for key, value in REGISTRY.items() if value.available()}


def get_dataset(key):
    if key not in available_datasets():
        raise ValueError("Base não disponível")
    return REGISTRY[key]
