import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent.parent / "config" / "config.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config