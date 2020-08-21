# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from numpy import str_
from pandas.core.frame import DataFrame
from typing import (
    Dict,
    List,
    Optional,
    Union,
)


def Chueh_Prausnitz_Tc(
    zs: List[float],
    Tcs: List[float],
    Vcs: List[float],
    taus: List[List[float]]
) -> float: ...


def Chueh_Prausnitz_Vc(zs: List[float], Vcs: List[float], nus: List[List[float]]) -> float: ...


def Grieves_Thodos(
    zs: List[float],
    Tcs: Union[List[float], List[Optional[float]]],
    Aijs: List[List[float]]
) -> float: ...


def Grigoras(Tc: Optional[float] = ..., Pc: Optional[float] = ..., Vc: Optional[float] = ...) -> float: ...


def Ihmels(Tc: Optional[float] = ..., Pc: Optional[float] = ..., Vc: Optional[float] = ...) -> float: ...


def Li(zs: List[float], Tcs: List[float], Vcs: List[float]) -> float: ...


def Meissner(Tc: Optional[float] = ..., Pc: Optional[float] = ..., Vc: Optional[float] = ...) -> float: ...


def Mersmann_Kind_predictor(
    atoms: Dict[str, int],
    coeff: float = ...,
    power: float = ...,
    covalent_radii: Dict[str, float] = ...
) -> float: ...


def Pc(CASRN: str, get_methods: bool = ..., method: None = ...) -> None: ...


def Tc(
    CASRN: Union[str, str_],
    get_methods: bool = ...,
    method: Optional[str] = ...
) -> Optional[Union[List[str], float]]: ...


def __getattr__(name: str) -> DataFrame: ...


def _add_Zc_to_df(df: DataFrame) -> None: ...


def _assert_two_critical_properties_provided(critical_properties: Union[List[None], List[Optional[float]]]) -> None: ...


def _load_critical_data() -> None: ...


def critical_surface(
    Tc: Optional[float] = ...,
    Pc: Optional[float] = ...,
    Vc: None = ...,
    get_methods: bool = ...,
    method: Optional[str] = ...
) -> Union[List[str], float]: ...


def modified_Wilson_Tc(zs: List[float], Tcs: List[float], Aijs: List[List[float]]) -> float: ...


def modified_Wilson_Vc(zs: List[float], Vcs: List[float], Aijs: List[List[float]]) -> float: ...


def third_property(CASRN: Optional[str] = ..., T: bool = ..., P: bool = ..., V: bool = ...) -> None: ...

__all__: List[str]