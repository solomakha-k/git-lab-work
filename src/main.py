#!/usr/bin/env python

def greet(name: str) -> str:
    """Повертає вітальне повідомлення."""
    return f"Привіт, {name}! "

if __name__=="__main__ ":
    print(greet("Студент "))

def farewell(name: str) -> str:
    """Повертає прощальне повідомлення. """
    return f"До поьачення, {name}!"
