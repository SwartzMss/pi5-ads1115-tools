import argparse

from ads_reader import read_channel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read ADS1115 channel voltage")
    parser.add_argument(
        "--pin",
        type=int,
        default=0,
        help="ADS1115 channel number (0-3)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    read_channel(args.pin)


if __name__ == "__main__":
    main()
