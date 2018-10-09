from threading import Event


class Scenario:

    def __init__(self, event_factories):
        self.event_factories = iter(event_factories)
        self.finished = Event()

    def __call__(self):
        try:
            event_factory = next(self.event_factories)
            return event_factory()
        except StopIteration:
            if not self.finished.is_set():
                self.finished.set()
            return []
