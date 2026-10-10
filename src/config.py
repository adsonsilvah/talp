from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data/raw/liverpool2023.xlsx"
PROCESSED_PATH = ROOT / "data/processed/liverpool2023.json"
MIN_COMPARISON_N = 30  # Regra descritiva; não garante representatividade.
TITLE = "IA no Ensino Superior"
