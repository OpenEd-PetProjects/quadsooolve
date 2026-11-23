from math import isfinite


def _read_coefficient(name: str) -> float:
    value = float(input(f"Enter {name}: "))
    if not isfinite(value):
        raise ValueError
    return value


def main() -> int:
    try:
        a, b, c = (_read_coefficient(name) for name in ("a", "b", "c"))
    except (ValueError, EOFError):
        print("Error: enter a finite numeric value.")
        return 1

    if a <= 0:
        print("Not a quadratic equation: a = 0.")
        return 1

    print(f"Coefficients accepted: a = {a}, b = {b}, c = {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
