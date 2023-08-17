import pygame

class Sound:

    def __init__(self, path):
        pygame.mixer.init()  # Initialize the pygame mixer
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)