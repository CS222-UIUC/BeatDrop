"""file that defines a scene as abstract class"""
from abc import ABC, abstractmethod

# pylint: disable=W0107

class Scene(ABC):
    """abstract class for scenes"""
    # @abstractmethod
    # def process_input(self, events, pressed_keys):
    #     """processes human input

    #     Args:
    #         events (Any): pygame events
    #         pressed_keys (Any): pygame pressed keys
    #     """
    #     pass

    @abstractmethod
    def initialize(self):
        """initialize any components of the scene"""
        pass

    @abstractmethod
    def update(self):
        """update the scene and its components"""
        pass

    @abstractmethod
    def render(self, screen):
        """render the scene and its components"""
        pass

    @abstractmethod
    def terminate(self):
        """terminate the scene and its components"""
        pass
