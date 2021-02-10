from typing import Any, Optional

def track_cascade_events(descriptor, prop): ...

class UOWTransaction(object):
    session: Any = ...
    attributes: Any = ...
    deps: Any = ...
    mappers: Any = ...
    presort_actions: Any = ...
    postsort_actions: Any = ...
    dependencies: Any = ...
    states: Any = ...
    post_update_states: Any = ...
    def __init__(self, session) -> None: ...
    @property
    def has_work(self): ...
    def was_already_deleted(self, state): ...
    def is_deleted(self, state): ...
    def memo(self, key, callable_): ...
    def remove_state_actions(self, state): ...
    def get_attribute_history(self, state, key, passive: Any = ...): ...
    def has_dep(self, processor): ...
    def register_preprocessor(self, processor, fromparent): ...
    def register_object(
        self,
        state,
        isdelete: bool = ...,
        listonly: bool = ...,
        cancel_delete: bool = ...,
        operation: Optional[Any] = ...,
        prop: Optional[Any] = ...,
    ): ...
    def issue_post_update(self, state, post_update_cols): ...
    def filter_states_for_dep(self, dep, states): ...
    def states_for_mapper_hierarchy(self, mapper, isdelete, listonly): ...
    def execute(self): ...
    def finalize_flush_changes(self): ...

class IterateMappersMixin(object): ...

class Preprocess(IterateMappersMixin):
    dependency_processor: Any = ...
    fromparent: Any = ...
    processed: Any = ...
    setup_flush_actions: bool = ...
    def __init__(self, dependency_processor, fromparent) -> None: ...
    def execute(self, uow): ...

class PostSortRec(object):
    disabled: bool = ...
    def __new__(cls, uow, *args): ...
    def execute_aggregate(self, uow, recs): ...

class ProcessAll(IterateMappersMixin, PostSortRec):
    dependency_processor: Any = ...
    delete: Any = ...
    fromparent: Any = ...
    def __init__(self, uow, dependency_processor, delete, fromparent) -> None: ...
    def execute(self, uow): ...
    def per_state_flush_actions(self, uow): ...

class IssuePostUpdate(PostSortRec):
    mapper: Any = ...
    isdelete: Any = ...
    def __init__(self, uow, mapper, isdelete) -> None: ...
    def execute(self, uow): ...

class SaveUpdateAll(PostSortRec):
    mapper: Any = ...
    def __init__(self, uow, mapper) -> None: ...
    def execute(self, uow): ...
    def per_state_flush_actions(self, uow): ...

class DeleteAll(PostSortRec):
    mapper: Any = ...
    def __init__(self, uow, mapper) -> None: ...
    def execute(self, uow): ...
    def per_state_flush_actions(self, uow): ...

class ProcessState(PostSortRec):
    dependency_processor: Any = ...
    delete: Any = ...
    state: Any = ...
    def __init__(self, uow, dependency_processor, delete, state) -> None: ...
    def execute_aggregate(self, uow, recs): ...

class SaveUpdateState(PostSortRec):
    state: Any = ...
    mapper: Any = ...
    def __init__(self, uow, state, mapper) -> None: ...
    def execute_aggregate(self, uow, recs): ...

class DeleteState(PostSortRec):
    state: Any = ...
    mapper: Any = ...
    def __init__(self, uow, state, mapper) -> None: ...
    def execute_aggregate(self, uow, recs): ...
