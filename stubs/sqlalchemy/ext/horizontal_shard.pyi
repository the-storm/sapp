from typing import Any, Optional

from ..orm.query import Query
from ..orm.session import Session

class ShardedQuery(Query):
    id_chooser: Any = ...
    query_chooser: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def set_shard(self, shard_id): ...
    def get(self, ident, **kwargs): ...

class ShardedSession(Session):
    shard_chooser: Any = ...
    id_chooser: Any = ...
    query_chooser: Any = ...
    connection_callable: Any = ...
    def __init__(
        self,
        shard_chooser,
        id_chooser,
        query_chooser,
        shards: Optional[Any] = ...,
        query_cls: Any = ...,
        **kwargs
    ) -> None: ...
    def connection(self, *args, **kwargs): ...
    def get_bind(self, *args, **kw): ...
    def bind_shard(self, shard_id, bind): ...
