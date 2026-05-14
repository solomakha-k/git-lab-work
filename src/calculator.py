#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """Повертає суму двох чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Повертає різницю двох чисел."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Повертає добуток двох чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Повертає частку. Викликає помилку при ділення на нуль."""
    if b == 0:
        raise ValueError("Ділення на нуль!")
    return a / b
