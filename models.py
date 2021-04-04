from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class Lang(str, Enum):
    eng = "eng"
    fra = "fra"
    dan = "dan"
    nld = "nld"
    fin = "fin"
    deu = "deu"
    hun = "hun"
    ita = "ita"
    nor = "nor"
    por = "por"
    ron = "ron"
    rus = "rus"
    spa = "spa"
    swe = "swe"
    tur = "tur"


class Document(BaseModel):
    pid: UUID
    lang: List[Lang]
    status: str
    input: Path
    output: Path
    output_json: Path
    output_txt: Path
    result: Optional[str] = None
    code: Optional[int] = None
    created: datetime
    processing: Optional[datetime] = None
    expire: datetime
    finished: Optional[datetime] = None

    def delete_all_files(self):
        if self.input.exists():
            self.input.unlink()
        if self.output.exists():
            self.output.unlink()
        if self.output_json.exists():
            self.output_json.unlink()
        if self.output_json.exists():
            self.output_json.unlink()
