from pathlib import Path
from src.classes import CLIHandler, CythonSetup, SetupConfig


def main():
    # Configurações do CLI
    cli = CLIHandler()
    args = cli.setup_parser().parse_args()

    if args.help_setup:
        cli.show_help()
        return

    # Configurações do setup
    config = SetupConfig(
        project_root=Path(__file__).parent,
        cython_root=Path(__file__).parent / "src" / "pureCython",
    )

    # Executa o comando de build diretamente através do método de classe
    CythonSetup.build(config)


if __name__ == "__main__":
    main()
