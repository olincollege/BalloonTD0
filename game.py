"""
Main game file that initializes and runs the game loop.
"""

import pygame
from map import Track
from balloon import Balloon
from towers import Tower


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Balloon TD")

        self.track = Track()
        # Add waypoints that both balloons and towers will reference
        self.track.add_waypoint(100, 150)
        self.track.add_waypoint(200, 250)
        self.track.add_waypoint(300, 350)

        # Set these waypoints in the Balloon class
        Balloon.waypoints = self.track.waypoints

        self.balloons = []
        self.towers = []
        self.money = 1000
        self.lives = 100

    def run(self):
        """Main game loop"""
        running = True
        while running:
            # Game loop implementation
            pass


if __name__ == "__main__":
    game = Game()
    game.run()
