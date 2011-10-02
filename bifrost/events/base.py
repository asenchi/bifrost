import time
import uuid

from collections import namedtuple

import tnetstring

# ==========
# I like this, but since it can't be serialized I am not sure it's what we want.
# Consider these type instead:
# CAN'T BE SERIALIZED WITHOUT SOME WORK
def event(func):
    varnames = ['event_id', 'timestamp']
    for var in func.__code__.co_varnames:
        varnames.append(var)

    return namedtuple(func.__name__, tuple(varnames))

@event
def TestEvent(message):
    pass
# ==========

# ==========
# I like this too, but again, can't be serialized.
class Test2Event(namedtuple('Test2Event', 'message')):
    @property
    def event_id(self):
        eid = str(uuid.uuid1())
        return eid

    @property
    def timestamp(self):
        ts = int(time.time())
        return ts

    def serialize(self):
        pass
# =========

 class BaseEvent(dict):
     def __init__(self):
         self._event_id = str(uuid.uuid1())
         self._timestamp = int(time.time())
 
     @property
     def event_id(self):
         return self._event_id
 
     @property
     def timestamp(self):
         return self._timestamp
 
     def serialize(self):
         return tnetstring.dumps(self.__dict__)


 class NodeEvent(BaseEvent):
     def __init__(self, message):
         super(NodeEvent, self).__init__()
         self._message = message
 
     @property
     def message(self):
         return self._message
 
 
 class PeerEvent(BaseEvent):
     def __init__(self, version, generation):
         super(PeerEvent, self).__init__()
         self._version = version
         self._generation = generation
 
     @property
     def version(self):
         return self._version
 
     @property
     def generation(self):
         return self._generation
