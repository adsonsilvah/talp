"""Todos os gráficos na mesma página, organizados apenas por categoria."""
from dash import html
from src.charts import profile, awareness, academic_integrity, policies
from src.components.charts import chart_card


def render(frame, dataset, mode, group):
    comparison = group if group in ("faculty", "study_level") else None
    sections = []

    def section(title, specifications):
        cards = []
        for fields, builder, heading, grouping, wide in specifications:
            if dataset.supports(*fields):
                figure = builder(frame, mode, grouping) if grouping is not False else builder(frame, mode)
                figure.update_layout(title_text=heading)
                cards.append(chart_card(figure, wide=wide))
        if cards:
            sections.append(html.Section([
                html.H2(title, className="section-title"),
                html.Div(cards, className="chart-grid"),
            ], className="chart-section"))

    section("Perfil dos respondentes", [
        (("faculty",), profile.faculty, "Faculdade", False, False),
        (("study_level",), profile.study_level, "Nível de estudo", False, False),
        (("faculty", "study_level"), profile.faculty_study_level, "Composição demográfica: faculdade × nível de estudo", False, True),
        (("confidence",), profile.confidence, "Confiança na escrita acadêmica · 1–5", comparison, True),
    ])
    section("Conhecimento e finalidades", [
        (("awareness",), awareness.awareness, "Ferramentas conhecidas", comparison, False),
        (("purposes",), awareness.purposes, "Finalidades de utilização ou consideração do uso", comparison, False),
        (("awareness", "purposes"), awareness.tools_academic, "Ferramenta conhecida × finalidade acadêmica", False, False),
        (("awareness",), awareness.repertoire, "Repertório: número de ferramentas conhecidas", comparison, False),
        (("confidence", "purposes"), awareness.confidence_academic, "Confiança × finalidade acadêmica", False, True),
    ])
    section("Integridade acadêmica", [
        (("grammar_attitude", "essay_attitude"), academic_integrity.acceptance, "Aceitação: apoio gramatical × redação integral", group, True),
        (("grammar_attitude", "essay_attitude"), academic_integrity.attitude_matrix, "Matriz de transição ética: apoio gramatical × redação integral", False, True),
    ])
    section("Políticas institucionais", [
        (("policy",), policies.policies, "Preferências de políticas institucionais", comparison, True),
        (("policy", "grammar_attitude", "essay_attitude"), policies.policy_integrity, "Preferência de política × aceitação de uso (apoio gramatical vs. redação integral)", False, True),
    ])
    return html.Div(sections)
