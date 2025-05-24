"""Módulo para manipulação da interface de linha de comando"""
import argparse


class CLIHandler:
    """Gerencia a interface de linha de comando e mensagens de ajuda"""
    
    @staticmethod
    def setup_parser() -> argparse.ArgumentParser:
        """Cria e configura o analisador de argumentos"""
        parser = argparse.ArgumentParser(
            description="Script de configuração para compilar módulos Cython"
        )
        parser.add_argument(
            "--help-setup",
            action="store_true",
            help="Mostra ajuda detalhada sobre a configuração e comandos disponíveis",
        )
        parser.add_argument(
            "command",
            nargs="?",
            choices=["build_ext", "clean"],
            help="Comando a ser executado (build_ext ou clean)",
        )
        parser.add_argument(
            "--inplace",
            action="store_true",
            help="Compila as extensões no local original"
        )
        parser.add_argument(
            "--all",
            action="store_true",
            help="Limpa todos os arquivos de compilação"
        )
        return parser
    
    @staticmethod
    def show_help() -> None:
        """Exibe informações de ajuda"""
        print("""
            Guia de Ajuda do Setup.py
            ------------------------

            Este script é usado para compilar módulos Cython no projeto.

            Comandos disponíveis:

            1. Compilar Extensões:
            python setup.py build_ext --inplace
            - Compila todos os módulos Cython encontrados em src/pureCython/
            - --inplace: Compila as extensões no local original dos arquivos

            2. Limpar Arquivos de Compilação:
            python setup.py clean --all
            - Remove todos os arquivos de compilação e extensões compiladas
            - --all: Remove todos os artefatos de compilação

            3. Mostrar Esta Ajuda:
            python setup.py --help-setup
            - Exibe esta mensagem de ajuda

            Como funciona:
            - O script descobre automaticamente todos os módulos Cython em src/pureCython/
            - Cada módulo é compilado para C e depois para uma extensão binária
            - Os headers do Numpy são incluídos na compilação
            - As extensões são compiladas usando C como linguagem alvo
        """)
