from typing import Union
import numpy as np


def sigmoid(
    x: np.ndarray,
    L: Union[int, float],
    x0: Union[int, float],
    k: Union[int, float],
    b: Union[int, float],
) -> np.ndarray:
    """Return values from a general sigmoid function."""
    y = L / (1 + np.exp(-k * (x - x0))) + b

    return y


def exponential(
    x: np.ndarray, a: Union[int, float], b: Union[int, float]
) -> np.ndarray:
    """Return values from a general exponential function."""

    return a * np.exp(b * x)


def logarithmic(
    x: np.ndarray, a: Union[int, float], b: Union[int, float], c: Union[int, float]
) -> np.ndarray:
    """Return values from a general log function."""

    return a * np.log(b * (x + c))


def inverse_sigmoid(
    y: np.ndarray,
    L: Union[int, float],
    x0: Union[int, float],
    k: Union[int, float],
    b: Union[int, float],
) -> np.ndarray:
    """Return values from a general inverse sigmoid function."""
    x = -np.log(L / (y - b) - 1) / k + x0

    return x
