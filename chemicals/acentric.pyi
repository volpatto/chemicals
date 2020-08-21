# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    Callable,
    List,
    Optional,
    Union,
)


def LK_omega(Tb: float, Tc: float, Pc: float) -> float: ...


def Stiel_polar_factor(Psat: int, Pc: float, omega: float) -> float: ...


def omega(
    CASRN: str,
    get_methods: bool = ...,
    method: Optional[Union[int, str, Callable]] = ...
) -> Optional[Union[List[str], float]]: ...


def omega_definition(Psat: int, Pc: float) -> float: ...

__all__: List[str]