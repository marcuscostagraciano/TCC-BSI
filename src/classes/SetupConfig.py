"""Módulo para classes de configuração do setup"""
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


@dataclass
class SetupConfig:
    """Classe de configuração para setup do Cython"""
    project_root: Path
    cython_root: Path
    folder_filter: Tuple[str, ...] = ("build", ".", "__pycache__")
