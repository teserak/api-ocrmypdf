from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    workdir: Path = "workdir"
    base_command_ocr: str = "/usr/local/bin/ocrmypdf"
    api_key_secret: str = "changeme"
    base_command_option: str = "--output-type pdf --fast-web-view 0 --optimize 0"


config = Settings()
