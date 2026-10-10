"""Único contrato de cabeçalhos e categorias originais do questionário."""
import json
from pathlib import Path

SCHEMA = json.loads(Path(__file__).with_name("liverpool_schema.json").read_text())
COLUMN_MAP = SCHEMA["columns"]
CATEGORIES = SCHEMA["categories"]
OPEN_FIELDS = ("other_tools", "other_purposes", "grammar_reason", "essay_reason", "policy_reason", "other_study_uses", "comments")
TOOLS = ("Grammarly", "Chat GPT", "ChatSonic", "Jasper Chat", "QuillBot", "DALI-E", "None of the above", "Other")
PURPOSES = (
    "Personal e.g. translations, recipes",
    "Academic e.g. checking grammar, formatting references",
    "Professional e.g. creating to-do lists, rotas, e-mails",
    "I have not used or considered using them", "Prefer not to say", "Other",
)
ACADEMIC = PURPOSES[1]
LIKERT = ("Supportive", "Somewhat supportive", "Neutral", "Somewhat unsupportive", "Unsupportive")
ATTITUDES = (*LIKERT, "Other")
POLICIES = tuple(CATEGORIES["policy"])
CLOSED_FIELDS = ("faculty", "study_level", "confidence", "awareness", "purposes", "grammar_attitude", "essay_attitude", "policy")
LABELS = {
    "Humanities and Social Sciences": "Humanidades e Ciências Sociais",
    "Health and Life Sciences": "Saúde e Ciências da Vida",
    "Science and Engineering": "Ciências e Engenharia", "Not sure": "Não identificado",
    "Undergraduate": "Graduação", "Postgraduate - Taught": "Pós-graduação (disciplinas)",
    "Postgraduate - Research": "Pós-graduação (pesquisa)", "Foundation": "Preparatório (Foundation)",
    "Chat GPT": "ChatGPT", "DALI-E": "DALI-E (grafia da base)",
    "None of the above": "Nenhuma das opções", "Other": "Outro",
    PURPOSES[0]: "Pessoal", PURPOSES[1]: "Acadêmica", PURPOSES[2]: "Profissional",
    PURPOSES[3]: "Não utilizou nem considerou", PURPOSES[4]: "Prefere não informar",
    "Supportive": "Favorável", "Somewhat supportive": "Parcialmente favorável", "Neutral": "Neutro",
    "Somewhat unsupportive": "Parcialmente contrário", "Unsupportive": "Contrário",
    "Have a university wide policy on when they are and or not appropriate to use": "Política única da universidade",
    "Let departments/faculties decide the policy when they are or are not appropriate to use": "Políticas por faculdade",
    "Let lecturers decide individual policies for individual assignments on when they are or are not appropriate to use": "Decisão de cada professor",
    "Allow them to be used however the students wish": "Liberdade de uso",
    "Ban them entirely": "Banimento completo",
}

def label(value):
    return LABELS.get(value, str(value))
