import sys
from pathlib import Path
import pytest
from dash.testing.application_runners import import_app

# Explicitly add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def app():
    return import_app("app")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsels" in header.text


def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-selector")
    assert radio_items is not None
