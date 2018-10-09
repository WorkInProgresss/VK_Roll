from queue import Queue
from threading import Thread, Event
from collections import defaultdict


SENTINEL = None


class Producer(Thread):

    def __init__(self, queue, produce, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = queue
        self.produce = produce
        self.finished = Event()

    def run(self):
        while not self.finished.is_set():
            for task in self.produce():
                self.queue.put(task)


class Consumer(Thread):

    def __init__(self, queue, consume, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = queue
        self.consume = consume

    def run(self):
        while True:
            task = self.queue.get()
            if task is not SENTINEL:
                self.consume(task)
                self.queue.task_done()
            else:
                self.queue.task_done()
                break


class Dispatcher:

    def __init__(self, event_factory):
        self._event_factory = event_factory
        self._queue = Queue()
        self._producer = None
        self._consumers = []
        self._event_handlers = defaultdict(list)

    def add_event_handler(self, event_type, event_handler):
        self._event_handlers[event_type].append(event_handler)

    def on(self, event_types):
        """
        Decorator version of `self.add_event_handler`.
        """
        def registering_wrapper(event_handler):
            for event_type in event_types:
                self.add_event_handler(event_type, event_handler)
            return event_handler

        return registering_wrapper

    def run(self, n_workers=1):
        self._producer = self._create_producer()

        for i in range(n_workers):
            consumer = self._create_consumer(i)
            self._consumers.append(consumer)

        self._producer.start()

        for consumer in self._consumers:
            consumer.start()

    def stop(self):
        self._producer.finished.set()

        for _ in self._consumers:
            self._queue.put(SENTINEL)

        self._queue.join()

    def _create_producer(self):
        return Producer(
            queue=self._queue,
            produce=self._event_factory,
            name='Producer'
        )

    def _create_consumer(self, i):
        return Consumer(
            queue=self._queue,
            consume=self._dispatch_event,
            name=f'Consumer-{i}'
        )

    def _dispatch_event(self, event):
        for event_handler in self._event_handlers[event.type]:
            event_handler(event.object)
