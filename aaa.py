def compute_sum(x: float, y: float, z: float = 0.0, round: int | None = None) -> float:
    return x + y


s: float = compute_sum(1,4) #warning: non restituisce una stringa anche se funziona lo stesso
print(s)

a: dict[str,int]
a: list | tuple # a può essere o una lista o una tupla
