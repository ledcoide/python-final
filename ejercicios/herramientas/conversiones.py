KM_POR_MILLA = 1.609344


def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def km_a_millas(km):
    return km / KM_POR_MILLA


def millas_a_km(millas):
    return millas * KM_POR_MILLA


if __name__ == "__main__":
    print(f"__name__ = {__name__!r}  (ejecutado directamente)")
    print(f"100 °C = {celsius_a_fahrenheit(100):.1f} °F")
    print(f"98.6 °F = {fahrenheit_a_celsius(98.6):.1f} °C")
    print(f"42.195 km = {km_a_millas(42.195):.2f} millas")
    print(f"1 milla = {millas_a_km(1):.3f} km")
