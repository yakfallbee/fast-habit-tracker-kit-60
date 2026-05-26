import json
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

_DEFAULTS = {
    "version": "0.5.0",
    "output_format": "text",
    "verbose": False,
}

def load_config():
    config = dict(_DEFAULTS)
    if CONFIG_FILE.exists():
        try:
            user_cfg = json.loads(CONFIG_FILE.read_text())
            config.update(user_cfg)
        except (json.JSONDecodeError, IOError):
            pass
    return config
