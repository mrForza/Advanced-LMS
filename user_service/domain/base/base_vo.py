from abc import ABC
from typing import Any, Tuple


class BaseValueObject(ABC):
    def _get_atomic_components(self) -> Tuple[Any]:
        pass

    def _validate(self, *args, **kwargs) -> None:
        pass

    def __hash__(self) -> int:
        hashed_value = 11
        for value in self._get_atomic_components():
            hashed_value += (hash(value) * 19 + 31)
        return hashed_value
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) != self.__class__:
            return False
        return self._get_atomic_components() == __value._get_atomic_components()
    
    def __ne__(self, __value: object) -> bool:
        return not self == __value     

    def __repr__(self) -> str:
        return f'BaseValueObjects with values: {self._get_atomic_components()}'