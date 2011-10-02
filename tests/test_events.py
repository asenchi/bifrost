import unittest

from bifrost.events import BaseEvent, NodeEvent

class TestBaseEvent(unittest.TestCase):
    def setUp(self):
        self.base_event = BaseEvent()

    def test_members(self):
        assert hasattr(self.base_event, '_event_id')
        assert hasattr(self.base_event, '_timestamp')

    def test_serialize(self):
        # TODO Get these numbers programmatically
        assert len(self.base_event.serialize()) == 84
        assert type(self.base_event.serialize()) == str

class TestNodeEvent(unittest.TestCase):
    def setUp(self):
        self.node_event = NodeEvent("testing")

    def test_message_member(self):
        assert hasattr(self.node_event, '_message')

    def test_serialize(self):
        # TODO Get these numbers programmatically
        assert len(self.node_event.serialize()) == 106
        assert type(self.node_event.serialize()) == str
