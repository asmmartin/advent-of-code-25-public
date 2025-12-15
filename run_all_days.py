import importlib
import os
from time import perf_counter

INPUT_FILE_EXTENSION = ".txt"


def main():
    start = perf_counter()
    names = [
        os.path.splitext(file)[0]
        for file in sorted(os.listdir("inputs"))
        if os.path.splitext(file)[1] == INPUT_FILE_EXTENSION
    ]

    for name in names:
        print(f"{name.capitalize()}:")
        print("------")
        module = importlib.import_module(f"advent_of_code_25.{name}")
        with open(f"inputs/{name}.txt") as f:
            text = f.read()
        module.main(text)
        print()

    end = perf_counter()
    print(f"All {len(names)} days took {end - start:.6f} seconds.")


if __name__ == "__main__":
    main()
