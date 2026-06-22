"""Módulo de funciones trigonométricas básicas.

Provee: `sin`, `cos`, `tan`, `sec`, `csc`, `cot`, y funciones inversas.
Todas las funciones aceptan un ángulo en radianes por defecto. Pase
`degrees=True` para usar grados.

Ejemplo:
	from funciones_trigonometricas import sin
	sin(90, degrees=True)  # devuelve 1.0
"""

from __future__ import annotations

import math
from typing import Optional

__all__ = [
	"sin",
	"cos",
	"tan",
	"sec",
	"csc",
	"cot",
	"asin",
	"acos",
	"atan",
]


def _to_radians(angle: float, degrees: bool) -> float:
	return math.radians(angle) if degrees else angle


def sin(angle: float, degrees: bool = False) -> float:
	"""Seno del ángulo.

	Args:
		angle: Ángulo en radianes (por defecto) o grados si `degrees=True`.
		degrees: Si True, interpreta `angle` en grados.

	Returns:
		El valor de `sin(angle)`.
	"""
	return math.sin(_to_radians(angle, degrees))


def cos(angle: float, degrees: bool = False) -> float:
	"""Coseno del ángulo."""
	return math.cos(_to_radians(angle, degrees))


def tan(angle: float, degrees: bool = False) -> float:
	"""Tangente del ángulo.

	Lanza `ValueError` si la tangente no está definida (coseno cercano a 0).
	"""
	a = _to_radians(angle, degrees)
	c = math.cos(a)
	if math.isclose(c, 0.0, abs_tol=1e-12):
		raise ValueError("tan no definida para este ángulo (coseno ≈ 0)")
	return math.tan(a)


def sec(angle: float, degrees: bool = False) -> float:
	"""Secante = 1 / cos(angle)."""
	c = cos(angle, degrees=degrees)
	if math.isclose(c, 0.0, abs_tol=1e-12):
		raise ValueError("sec no definida para este ángulo (coseno ≈ 0)")
	return 1.0 / c


def csc(angle: float, degrees: bool = False) -> float:
	"""Cosecante = 1 / sin(angle)."""
	s = sin(angle, degrees=degrees)
	if math.isclose(s, 0.0, abs_tol=1e-12):
		raise ValueError("csc no definida para este ángulo (seno ≈ 0)")
	return 1.0 / s


def cot(angle: float, degrees: bool = False) -> float:
	"""Cotangente = 1 / tan(angle)."""
	t = tan(angle, degrees=degrees)
	if math.isclose(t, 0.0, abs_tol=1e-12):
		raise ValueError("cot no definida para este ángulo (tan ≈ 0)")
	return 1.0 / t


def asin(value: float) -> float:
	"""Arco seno, devuelve ángulo en radianes."""
	return math.asin(value)


def acos(value: float) -> float:
	"""Arco coseno, devuelve ángulo en radianes."""
	return math.acos(value)


def atan(value: float) -> float:
	"""Arco tangente, devuelve ángulo en radianes."""
	return math.atan(value)
