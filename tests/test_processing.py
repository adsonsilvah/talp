import json
from pathlib import Path
import pytest
from src.config import RAW_PATH, PROCESSED_PATH
from src.datasets.schema import COLUMN_MAP, CLOSED_FIELDS, OPEN_FIELDS, PURPOSES, TOOLS
from src.datasets.liverpool import load, validate
from src.processing.liverpool_cleaning import parse_multi, read_raw, clean


def test_processed_contract(frame):
    assert len(frame) == 2555
    assert list(frame.columns) == list(CLOSED_FIELDS)
    assert not set(frame).intersection(OPEN_FIELDS)
    assert frame.confidence.between(1,5).all()
    assert not frame.isna().any().any()


def test_parser_internal_commas():
    value = ','.join(PURPOSES[:3])
    assert parse_multi(value,PURPOSES) == list(PURPOSES[:3])
    assert parse_multi(PURPOSES[1],PURPOSES) == [PURPOSES[1]]
    assert parse_multi('Grammarly,Chat GPT',TOOLS) == ['Grammarly','Chat GPT']


@pytest.mark.parametrize('value', ['',None,'Unknown',PURPOSES[1]+',broken',PURPOSES[1]+',',PURPOSES[1]+','+PURPOSES[1]])
def test_parser_fails_closed(value):
    with pytest.raises(ValueError):
        parse_multi(value,PURPOSES)


def test_conflicts_preserved(frame):
    assert frame.awareness.map(lambda x: 'None of the above' in x and len(x)>1).sum() == 4
    assert frame.purposes.map(lambda x: PURPOSES[3] in x and len(x)>1).sum() == 17


def test_invalid_processed_rejected(frame):
    frame.loc[0,'confidence'] = 9
    with pytest.raises(ValueError):
        validate(frame)


def test_invalid_metadata_rejected(tmp_path):
    payload=json.loads(PROCESSED_PATH.read_text()); payload['schema_version']=99
    path=tmp_path/'bad.json'; path.write_text(json.dumps(payload))
    with pytest.raises(ValueError):
        load(path)


@pytest.mark.skipif(not RAW_PATH.exists(), reason='Excel privado ausente: teste opcional de reprocessamento local')
def test_raw_round_trip(frame):
    from pandas.testing import assert_frame_equal
    assert_frame_equal(clean(read_raw(RAW_PATH)),frame,check_dtype=False)
