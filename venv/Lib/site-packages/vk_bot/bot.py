from vk_client import VkClient
from .dispatcher import Dispatcher


class VkBot(Dispatcher):

    def __init__(self, access_token):
        self._vk = VkClient(access_token)
        self._blp = self.vk.BotsLongPoll.get()
        super().__init__(event_factory=self._blp.get_updates)

    @property
    def vk(self):
        return self._vk
