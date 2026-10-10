import numpy as np
import pytest
from src.charts.awareness import awareness,purposes,confidence_academic
from src.charts.profile import confidence,faculty,study_level
from src.charts.academic_integrity import acceptance
from src.charts.policies import policies
from src.datasets.schema import ATTITUDES,label

CHARTS=[awareness,purposes,confidence_academic,confidence,faculty,study_level,acceptance,policies]

@pytest.mark.parametrize('chart',CHARTS)
@pytest.mark.parametrize('mode',['count','percent'])
def test_figures_and_empty(frame,chart,mode):
    fig=chart(frame,mode)
    assert fig.data
    assert len(fig.to_json())>100
    empty=chart(frame.iloc[:0],mode)
    assert not empty.data
    assert 'Nenhuma resposta' in empty.layout.annotations[0].text


def test_likert_order_and_denominator(frame):
    fig=acceptance(frame)
    assert [t.name for t in fig.data]==[label(v) for v in ATTITUDES]
    np.testing.assert_allclose(np.array([t.x for t in fig.data]).sum(axis=0),[100,100])
    assert fig.data[0].customdata[0][2]==2555
    assert fig.data[-1].customdata[0][0]==33
    assert fig.data[-1].customdata[1][0]==40


def test_heatmap_denominators(frame):
    fig=confidence_academic(frame)
    np.testing.assert_allclose(np.array(fig.data[0].z).sum(axis=0),[100]*5)
    assert [v[2] for v in fig.data[0].customdata[0]]==[43,228,952,1059,273]
    filtered=confidence_academic(frame[frame.confidence.eq(1)])
    assert filtered.data[0].z[0][1] is None
    assert filtered.data[0].customdata[0][1][2]==0


def test_group_sizes(frame):
    fig=policies(frame,group='study_level')
    groups={row[3] for trace in fig.data for row in trace.customdata}
    assert 'Preparatório (Foundation)' not in groups
    assert 'Não identificado' not in groups
    assert len(groups)==3
    for trace in fig.data:
        for count,pct,n,_ in trace.customdata:
            assert n>=30
            assert pct==pytest.approx(100*count/n)
    fig=policies(frame[frame.study_level.eq('Foundation')],group='study_level')
    assert not fig.data


def test_confidence_order(frame):
    assert list(confidence(frame).layout.xaxis.categoryarray)==['1','2','3','4','5']
