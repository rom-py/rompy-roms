from importlib.metadata import entry_points
from rompy_roms.config import Config


def test_config_entrypoint():
    eps = entry_points(group="rompy.config")
    names = [ep.name for ep in eps]
    assert "roms" in names