from typing import Any, Optional

def cache(fn, self, con, *args, **kw): ...

class Inspector(object):
    bind: Any = ...
    engine: Any = ...
    dialect: Any = ...
    info_cache: Any = ...
    def __init__(self, bind) -> None: ...
    @classmethod
    def from_engine(cls, bind): ...
    @property
    def default_schema_name(self) -> Any: ...
    def get_schema_names(self): ...
    def get_table_names(
        self, schema: Optional[Any] = ..., order_by: Optional[Any] = ...
    ): ...
    def get_sorted_table_and_fkc_names(self, schema: Optional[Any] = ...): ...
    def get_temp_table_names(self): ...
    def get_temp_view_names(self): ...
    def get_table_options(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_view_names(self, schema: Optional[Any] = ...): ...
    def get_view_definition(self, view_name, schema: Optional[Any] = ...): ...
    def get_columns(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_primary_keys(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_pk_constraint(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_foreign_keys(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_indexes(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_unique_constraints(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_check_constraints(self, table_name, schema: Optional[Any] = ..., **kw): ...
    def reflecttable(
        self,
        table,
        include_columns,
        exclude_columns: Any = ...,
        _extend_on: Optional[Any] = ...,
    ): ...
