from typing import Any, Optional

from ...orm import interfaces

def instrument_declarative(cls, registry, metadata): ...
def has_inherited_table(cls): ...

class DeclarativeMeta(type):
    def __init__(cls, classname, bases, dict_) -> None: ...
    def __setattr__(cls, key, value): ...

def synonym_for(name, map_column: bool = ...): ...
def comparable_using(comparator_factory): ...

class declared_attr(interfaces._MappedAttribute, property):
    __doc__: Any = ...
    def __init__(self, fget, cascading: bool = ...) -> None: ...
    def __get__(desc, self, cls): ...
    def cascading(cls): ...

class _stateful_declared_attr(declared_attr):
    kw: Any = ...
    def __init__(self, **kw) -> None: ...
    def __call__(self, fn): ...

def declarative_base(
    bind: Optional[Any] = ...,
    metadata: Optional[Any] = ...,
    mapper: Optional[Any] = ...,
    cls: Any = ...,
    name: str = ...,
    constructor: Any = ...,
    class_registry: Optional[Any] = ...,
    metaclass: Any = ...,
): ...
def as_declarative(**kw): ...

class ConcreteBase(object):
    @classmethod
    def __declare_first__(cls): ...

class AbstractConcreteBase(ConcreteBase):
    __no_table__: bool = ...
    @classmethod
    def __declare_first__(cls): ...

class DeferredReflection(object):
    @classmethod
    def prepare(cls, engine): ...
