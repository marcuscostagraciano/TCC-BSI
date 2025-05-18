from src.tests import Tests


def main() -> None:
    Tests.\
        run_max_value_tests().\
        run_mean_value_tests()


if __name__ == "__main__":
    main()
