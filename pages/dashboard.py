"""Todos os gráficos na mesma página, organizados apenas por categoria."""
from dash import html
from src.charts import profile, awareness, academic_integrity, policies
from src.components.charts import chart_card


def render(frame, dataset, mode="percent", *args, **kwargs):
    sections = []

    def section(title, specifications):
        cards = []
        for fields, builder, heading, wide in specifications:
            if dataset.supports(*fields):
                figure = builder(frame, mode)
                figure.update_layout(title_text=heading)
                cards.append(chart_card(figure, wide=wide))
        if cards:
            sections.append(html.Section([
                html.H2(title, className="section-title"),
                html.Div(cards, className="chart-grid"),
            ], className="chart-section"))

    section("Perfil dos respondentes", [
        (("faculty",), profile.faculty, "Faculdade", False),
        (("study_level",), profile.study_level, "Nível de estudo", False),
        (("faculty", "study_level"), profile.faculty_study_level, "Composição demográfica: faculdade × nível de estudo", True),
        (("confidence",), profile.confidence, "Confiança na escrita acadêmica · 1–5", True),
    ])
    section("Conhecimento e finalidades", [
        (("awareness",), awareness.awareness, "Ferramentas conhecidas", False),
        (("purposes",), awareness.purposes, "Finalidades de utilização ou consideração do uso", False),
        (("awareness", "purposes"), awareness.tools_academic, "Ferramenta conhecida × conversão para finalidade acadêmica", False),
        (("awareness",), awareness.repertoire, "Repertório: número de ferramentas conhecidas", False),
        (("confidence", "purposes"), awareness.confidence_academic, "Confiança × finalidade acadêmica", True),
    ])
    section("Integridade acadêmica", [
        (("grammar_attitude", "essay_attitude"), academic_integrity.acceptance, "Aceitação: apoio gramatical × redação integral", True),
        (("grammar_attitude", "essay_attitude"), academic_integrity.attitude_matrix, "Matriz de transição ética: apoio gramatical × redação integral", True),
    ])
    section("Políticas institucionais", [
        (("policy",), policies.policies, "Preferências de políticas institucionais", True),
        (("policy", "grammar_attitude", "essay_attitude"), policies.policy_integrity, "Preferência de política × aceitação de uso (apoio gramatical vs. redação integral)", True),
    ])
    return html.Div(sections)
