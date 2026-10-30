"""Audita e prepara apenas variáveis fechadas; nunca publica dados."""
import argparse
import hashlib
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config import RAW_PATH, PROCESSED_PATH, ROOT
from src.datasets.schema import COLUMN_MAP, OPEN_FIELDS, TOOLS, PURPOSES, ACADEMIC, label
from src.processing.liverpool_cleaning import read_raw, clean, save_processed
from src.processing.metrics import metrics, selection
from src.datasets.liverpool import validate


def run(source, destination):
    raw = read_raw(source)
    frame = validate(clean(raw))
    expected = {"Finalidade acadêmica": 1302, "Apoio gramatical · favoráveis": 1366, "Redação integral · contrários": 1800, "Política institucional única": 1049}
    calculated = metrics(frame)
    for name, count in expected.items():
        if calculated[name]["count"] != count:
            raise ValueError(f"Verificação de referência falhou: {name}")
    if frame.faculty.value_counts().to_dict() != {"Humanities and Social Sciences": 1033, "Health and Life Sciences": 759, "Science and Engineering": 680, "Not sure": 83}:
        raise ValueError("Totais por faculdade divergentes")
    save_processed(frame, source, destination)
    lines = ["# Auditoria — Liverpool 2023", "", "Relatório gerado por `python scripts/prepare_data.py`; nenhuma resposta aberta individual é reproduzida.", "", f"Uma aba (`Sheet 1`), {len(raw):,} respostas, {len(raw.columns)} colunas. SHA-256 da fonte: `{hashlib.sha256(source.read_bytes()).hexdigest()}`.", "", "## Dicionário de dados", "", "| Coluna | Nome interno | Tipo analítico | Ausências | Valores distintos | Cabeçalho original |", "|---|---|---|---:|---:|---|"]
    for index, (original, field) in enumerate(COLUMN_MAP.items()):
        kind = "Texto livre (excluído)" if field in OPEN_FIELDS else "Ordinal 1–5" if field == "confidence" else "Ordinal + Outro" if field.endswith("attitude") else "Nominal multirresposta" if field in ("awareness", "purposes") else "Nominal"
        lines.append(f"| {chr(65+index)} | {field} | {kind} | {raw[field].isna().sum()} | {raw[field].nunique()} | {original} |")
    lines += ["", "Nível de estudo é apresentado como nominal: Foundation/graduação/pós-graduação têm relações institucionais, mas modalidades de pós-graduação não constituem uma escala numérica. Confiança e opiniões são ordinais, nunca médias numéricas. Consentimento é verificado e excluído do produto processado.", "", "## Categorias e frequências observadas", ""]
    for field in raw.columns:
        if field in OPEN_FIELDS:
            continue
        lines += [f"### {field}", "", "| Categoria original | n |", "|---|---:|"]
        if field in ("awareness", "purposes"):
            vocab = TOOLS if field == "awareness" else PURPOSES
            lines += [f"| {option} | {selection(frame, field, option)} |" for option in vocab]
            lines += ["", f"{raw[field].nunique()} combinações distintas. Frequências de seleções; denominador = 2.555 respondentes, não o total de seleções. A soma pode ultrapassar 100%."]
        else:
            lines += [f"| {v} | {n} |" for v,n in raw[field].value_counts().items()]
        lines += [""]
    awareness_conflict = frame.awareness.map(lambda x: "None of the above" in x and len(x)>1).sum()
    purpose_conflict = frame.purposes.map(lambda x: PURPOSES[3] in x and len(x)>1).sum()
    prefer_conflict = frame.purposes.map(lambda x: PURPOSES[4] in x and len(x)>1).sum()
    lines += ["## Inconsistências e decisões", "", f"- {awareness_conflict} respostas selecionam 'None of the above' junto a outra alternativa.", f"- {purpose_conflict} respostas selecionam 'I have not used or considered using them' junto a outra alternativa; {prefer_conflict} selecionam 'Prefer not to say' junto a outra alternativa. Há sobreposição entre esses indicadores.", f"- {raw.duplicated().sum()} linhas completamente iguais. Foram preservadas: sem identificadores não há evidência de submissões duplicadas; respostas fechadas iguais podem ser legítimas.", "- Nenhuma ausência nas nove colunas fechadas, incluindo consentimento. Ausências nos textos opcionais não são imputadas.", "- Nenhuma alternativa desconhecida foi aceita. A grafia original DALI-E foi preservada; Chat GPT é exibido como ChatGPT.", "- O parser consome alternativas completas de um vocabulário validado; vírgulas internas de G não delimitam alternativas.", "- Todas as seleções contraditórias são mantidas. 'Não selecionou finalidade acadêmica' não significa que nunca utilizou IA; inclui recusas e outras finalidades.", "", "## Comparação com o artigo", "", "| Indicador | Planilha: n / 2.555 | Calculado | Artigo |", "|---|---:|---:|---:|"]
    article = {"Conhecia o ChatGPT":68.9, "Finalidade acadêmica":50.9, "Apoio gramatical · favoráveis":54.1, "Redação integral · contrários":70.4, "Política institucional única":41.1}
    for name, m in calculated.items():
        lines.append(f"| {name} | {m['count']} / 2.555 | {m['percent']:.4f}% | {article[name]}% |")
    lines += ["", "Grammarly: " + str(selection(frame,"awareness","Grammarly")) + "/2.555 (artigo: 88,5%). Os totais por faculdade e os cinco totais de referência foram verificados pelo script.", "", "Apoio gramatical: 1.366/2.555 = 53,4638%, contra 54,1% no artigo (diferença −0,6362 ponto percentual). Excluindo os 33 'Outro', 1.366/2.522 = 54,1634% (54,2% por arredondamento convencional). Isso sugere diferença de denominador e/ou arredondamento, mas não comprova a metodologia publicada. Não se alteraram registros para reproduzir 54,1%. O artigo informa exclusão de 'Other' nas análises ordinais; isso não esclarece integralmente o percentual do resumo.", "", "## Privacidade, origem e reutilização", "", "Fonte local: planilha fornecida no projeto. Artigo: Johnston, Wells, Shanks, Boey e Parsons (2024), DOI https://doi.org/10.1007/s40979-024-00149-4. Repositório de dados citado: https://doi.org/10.17638/datacat.liverpool.ac.uk/2297.", "", "O artigo declara CC BY 4.0 para seu conteúdo e CC0 para dados disponibilizados no artigo salvo indicação contrária. O catálogo externo foi consultado em 10/10/2026: Raw data.xlsx e seu README estão explicitamente sob CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). A comparação pandas entre a fonte local e o arquivo oficial confirmou igualdade dos 2.555 × 16 valores e cabeçalhos, embora os hashes dos arquivos Excel difiram. Veja data_provenance.md para evidências e atribuição.", "", "Respostas livres podem mencionar pessoas, circunstâncias ou detalhes identificáveis. Foi examinada sua estrutura e presença, sem reproduzir seus conteúdos: a decisão conservadora é excluir integralmente F, H, J, L, N, O e P. Não há classificação automática nem declaração de anonimização desses textos. Brutos e PDFs permanecem ignorados pelo Git.", "", "O derivado contém oito variáveis fechadas, sem consentimento, índices originais ou textos livres; mantém categorias inglesas. Combinações raras podem permitir inferências. A divulgação do derivado também requer autorização do proprietário, atribuição CC BY 4.0 e indicação das transformações; remoção de textos não equivale a anonimização formal. Não há download de microdados na interface. Comparações agrupadas omitem grupos com n<30, regra descritiva que não garante sigilo ou precisão estatística.", "", "## Limitações e denominadores", "", "Amostra voluntária, uma instituição do Reino Unido, março–abril de 2023; 8,86% da população universitária segundo o artigo. Sem ponderação, inferência causal ou extrapolação para todos os estudantes. As ferramentas do questionário incluem assistentes que não são estritamente IA generativa. Não há medida de uso efetivo separada de intenção/consideração.", "", "KPIs e barras: denominador = todos os respondentes do filtro; agrupadas = total do grupo dentro do filtro. Likert: cinco categorias em ordem, com Outro como sexta categoria separada semanticamente, denominador inclui Outro. Heatmap: denominador = total em cada nível de confiança dentro do filtro; colunas sem respondentes ficam sem estimativa. Arredondamento visual a uma casa, cálculos em precisão completa."]
    (ROOT/"docs/data_audit.md").write_text("\n".join(lines)+"\n")
    print(f"Auditoria concluída: {len(frame)} respostas; apenas {len(frame.columns)} variáveis fechadas no derivado.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=RAW_PATH)
    parser.add_argument("--output", type=Path, default=PROCESSED_PATH)
    args = parser.parse_args()
    run(args.input, args.output)
