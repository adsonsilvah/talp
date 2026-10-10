import json
import os
import shutil
import subprocess
import sys
import pytest
import app
from src.config import ROOT
from src.datasets.registry import available_datasets,get_dataset


def test_registry():
    assert list(available_datasets())==['liverpool2023']
    assert get_dataset('liverpool2023').supports('confidence','purposes')
    assert not get_dataset('liverpool2023').supports('geography')
    with pytest.raises(ValueError):
        get_dataset('liverpool2025')


def test_http():
    client=app.server.test_client()
    for path in ['/','/healthz','/_dash-layout','/_dash-dependencies','/assets/style.css']:
        assert client.get(path).status_code==200


@pytest.mark.parametrize('mode,group', [('percent','none'), ('count','faculty'), ('percent','study_level'), ('percent','confidence')])
def test_single_page(mode, group):
    result = app.render_dashboard('liverpool2023', [], [], [], mode, group)
    assert len(result.children) == 4
    cards = [card for section in result.children for card in section.children[1].children]
    assert len(cards) == 8
    assert all(len(card.children) == 2 for card in cards)
    empty = app.render_dashboard('liverpool2023', ['missing'], [], [], mode, group)
    for section in empty.children:
        for card in section.children[1].children:
            assert not card.children[1].figure.data


def test_callback_http():
    client=app.server.test_client()
    key='dashboard-content.children'
    outputs={'id':'dashboard-content','property':'children'}
    inputs=[{'id':id,'property':prop,'value':value} for id,prop,value in [
        ('dataset','value','liverpool2023'),('faculty','value',['Health and Life Sciences']),
        ('study-level','value',[]),('confidence','value',[]),('mode','value','percent'),('group','value','none')]]
    response=client.post('/_dash-update-component',json={'output':key,'outputs':outputs,'inputs':inputs,'state':[],'changedPropIds':['faculty.value']})
    assert response.status_code==200
    content = response.get_json()['response']['dashboard-content']['children']
    first_graph = content['props']['children'][0]['props']['children'][1]['props']['children'][0]['props']['children'][1]
    assert first_graph['type'] == 'Graph'
    figure = first_graph['props']['figure']
    assert all(row[2] == 759 for trace in figure['data'] for row in trace['customdata'])


def test_reset():
    reset=app.reset_filters('liverpool2023',1)
    assert reset[3:]==([],[],[],'none','percent')


def test_production_without_raw(tmp_path):
    """Execute em cópia isolada contendo somente artefatos de produção."""
    for folder in ['src','pages','assets','data/processed']:
        shutil.copytree(ROOT/folder,tmp_path/folder,ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copy(ROOT/'app.py',tmp_path/'app.py')
    assert not (tmp_path/'data/raw').exists()
    code="import app; assert app.server.test_client().get('/healthz').status_code == 200; assert app.server.test_client().get('/_dash-layout').status_code == 200; assert len(app.dataset_frame('liverpool2023')) == 2555"
    result=subprocess.run([sys.executable,'-c',code],cwd=tmp_path,capture_output=True,text=True,timeout=30)
    assert result.returncode==0,result.stderr


def test_responsive_graph_has_explicit_height(frame):
    from src.charts.awareness import awareness
    from src.components.charts import chart_card
    card = chart_card(awareness(frame))
    graph = card.children[1]
    assert graph.responsive is True
    assert int(graph.style['height'].removesuffix('px')) >= 400
    assert 'sendChartToCloud' in graph.config['modeBarButtonsToRemove']
