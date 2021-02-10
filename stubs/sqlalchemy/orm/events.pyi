from typing import Any

from .. import event

class InstrumentationEvents(event.Events):
    def class_instrument(self, cls): ...
    def class_uninstrument(self, cls): ...
    def attribute_instrument(self, cls, key, inst): ...

class _InstrumentationEventsHold(object):
    class_: Any = ...
    def __init__(self, class_) -> None: ...
    dispatch: Any = ...

class InstanceEvents(event.Events):
    def first_init(self, manager, cls): ...
    def init(self, target, args, kwargs): ...
    def init_failure(self, target, args, kwargs): ...
    def load(self, target, context): ...
    def refresh(self, target, context, attrs): ...
    def refresh_flush(self, target, flush_context, attrs): ...
    def expire(self, target, attrs): ...
    def pickle(self, target, state_dict): ...
    def unpickle(self, target, state_dict): ...

class _EventsHold(event.RefCollection):
    class_: Any = ...
    def __init__(self, class_) -> None: ...
    class HoldEvents(object): ...
    def remove(self, event_key): ...
    @classmethod
    def populate(cls, class_, subject): ...

class _InstanceEventsHold(_EventsHold):
    all_holds: Any = ...
    def resolve(self, class_): ...
    class HoldInstanceEvents(_EventsHold.HoldEvents, InstanceEvents): ...
    dispatch: Any = ...

class MapperEvents(event.Events):
    def instrument_class(self, mapper, class_): ...
    def mapper_configured(self, mapper, class_): ...
    def before_configured(self): ...
    def after_configured(self): ...
    def before_insert(self, mapper, connection, target): ...
    def after_insert(self, mapper, connection, target): ...
    def before_update(self, mapper, connection, target): ...
    def after_update(self, mapper, connection, target): ...
    def before_delete(self, mapper, connection, target): ...
    def after_delete(self, mapper, connection, target): ...

class _MapperEventsHold(_EventsHold):
    all_holds: Any = ...
    def resolve(self, class_): ...
    class HoldMapperEvents(_EventsHold.HoldEvents, MapperEvents): ...
    dispatch: Any = ...

class SessionEvents(event.Events):
    def after_transaction_create(self, session, transaction): ...
    def after_transaction_end(self, session, transaction): ...
    def before_commit(self, session): ...
    def after_commit(self, session): ...
    def after_rollback(self, session): ...
    def after_soft_rollback(self, session, previous_transaction): ...
    def before_flush(self, session, flush_context, instances): ...
    def after_flush(self, session, flush_context): ...
    def after_flush_postexec(self, session, flush_context): ...
    def after_begin(self, session, transaction, connection): ...
    def before_attach(self, session, instance): ...
    def after_attach(self, session, instance): ...
    def after_bulk_update(self, update_context): ...
    def after_bulk_delete(self, delete_context): ...
    def transient_to_pending(self, session, instance): ...
    def pending_to_transient(self, session, instance): ...
    def persistent_to_transient(self, session, instance): ...
    def pending_to_persistent(self, session, instance): ...
    def detached_to_persistent(self, session, instance): ...
    def loaded_as_persistent(self, session, instance): ...
    def persistent_to_deleted(self, session, instance): ...
    def deleted_to_persistent(self, session, instance): ...
    def deleted_to_detached(self, session, instance): ...
    def persistent_to_detached(self, session, instance): ...

class AttributeEvents(event.Events):
    def append(self, target, value, initiator): ...
    def remove(self, target, value, initiator): ...
    def set(self, target, value, oldvalue, initiator): ...
    def init_scalar(self, target, value, dict_): ...
    def init_collection(self, target, collection, collection_adapter): ...
    def dispose_collection(self, target, collection, collection_adpater): ...

class QueryEvents(event.Events):
    def before_compile(self, query): ...
