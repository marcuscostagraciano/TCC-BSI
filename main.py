from src.tests import Tests


def main() -> None:
    Tests.set_download(
        download=True,
        download_folder="graphs",
        only_download=True,
    )
    Tests.run_max_value_tests()


if __name__ == "__main__":
    main()
