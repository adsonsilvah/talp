import pytest
from src.processing.metrics import metrics, percentage, selection, apply_filters
from src.datasets.schema import ACADEMIC


def test_reference_counts(frame):
    assert frame.faculty.value_counts().to_dict() == {'Humanities and Social Sciences':1033,'Health and Life Sciences':759,'Science and Engineering':680,'Not sure':83}
    m=metrics(frame)
    assert m['Finalidade acadêmica']['count']==1302
    assert m['Apoio gramatical · favoráveis']['count']==1366
    assert m['Redação integral · contrários']['count']==1800
    assert m['Política institucional única']['count']==1049
    assert m['Conhecia o ChatGPT']['count']==1761
    assert m['Apoio gramatical · favoráveis']['percent']==pytest.approx(53.46379647749511)
    assert all(x['denominator']==2555 for x in m.values())


def test_percentage():
    assert percentage(1,4)==25
    assert percentage(0,4)==0
    assert percentage(0,0) is None


def test_filters_and_denominators(frame):
    result=apply_filters(frame,['Health and Life Sciences'],['Undergraduate'],[1,2])
    assert len(result)>0
    assert set(result.faculty)=={'Health and Life Sciences'}
    assert set(result.study_level)=={'Undergraduate'}
    assert set(result.confidence).issubset({1,2})
    assert all(x['denominator']==len(result) for x in metrics(result).values())
    assert len(frame)==2555
    assert len(apply_filters(frame,[],[],[]))==2555


def test_empty(frame):
    result=apply_filters(frame,['missing'])
    assert result.empty
    assert all(m['percent'] is None for m in metrics(result).values())
    assert selection(result,'purposes',ACADEMIC)==0
