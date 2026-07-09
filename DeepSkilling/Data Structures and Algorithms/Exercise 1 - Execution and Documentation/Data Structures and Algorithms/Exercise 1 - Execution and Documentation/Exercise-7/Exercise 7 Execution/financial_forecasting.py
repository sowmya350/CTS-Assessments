from typing import List


def average_change(values: List[float]) -> float:
    """Return the average change between consecutive historical values."""
    if len(values) < 2:
        return 0.0

    differences = [values[i] - values[i - 1] for i in range(1, len(values))]
    return sum(differences) / len(differences)


def forecast_recursive(values: List[float], periods: int) -> List[float]:
    """
    Recursively forecast future values using the average change from past data.
    Each forecast becomes part of the next recursive step.
    """
    if periods < 0:
        raise ValueError("periods must be non-negative")

    if periods == 0:
        return []

    next_value = values[-1] + average_change(values)
    return [next_value] + forecast_recursive(values + [next_value], periods - 1)


def main() -> None:
    history = [100, 110, 120, 130]
    forecasted_values = forecast_recursive(history, 3)

    print("Historical data:", history)
    print("Forecasted values:", forecasted_values)


if __name__ == "__main__":
    main()
