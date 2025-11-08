"""Módulo para manipulação do setup do Cython"""
import os
from numpy import get_include
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

from .SetupConfig import SetupConfig


class CythonSetup:
    """Gerencia a configuração e compilação dos módulos Cython"""
    __config: SetupConfig
    
    @classmethod
    def discover_cython_folders(cls) -> list[str]:
        """Descobre todas as pastas de módulos Cython válidas"""
        return [
            path
            for path in os.listdir(cls.__config.cython_root)
            if not any(filter in path for filter in cls.__config.folder_filter)
        ]
    
    @classmethod
    def create_extensions(cls) -> list[Extension]:
        """Cria objetos Extension para cada módulo Cython"""
        cython_folders = cls.discover_cython_folders()
        print(f"{cython_folders = }")
        
        ext_modules: list[Extension] = []
        for folder in cython_folders:
            ext_modules.append(
                Extension(
                    f"src.pureCython.{folder}",
                    [str(cls.__config.cython_root / folder / "*.pyx")],
                    include_dirs=[get_include()],
                    language="c",
                )
            )
        return ext_modules
    
    @classmethod
    def build(cls, config: SetupConfig) -> None:
        """Compila todas as extensões Cython"""
        cls.__config = config

        ext_modules = cls.create_extensions()
        setup(ext_modules=cythonize(ext_modules))
