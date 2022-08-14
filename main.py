"Lights mind game"
import pygame


class Light:
    """Light class"""
    def __init__(self, screen, x, y, r, c, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.arrPos = (r, c)
        self.size = size


    def changeNeighbours(self, arr):
        """Change Neighbours Color"""
        for r in range(self.arrPos[1]-1, self.arrPos[1]+2):
            for c in range(self.arrPos[0]-1, self.arrPos[0]+2):
                if 0 <= r < 4 and 0 <= c < 4:
                    # change color

                    if arr[c][r] == "y":
                        arr[c][r] = "w"
                    elif arr[c][r] == "w":
                        arr[c][r] = "y"

        return arr

    def checkClick(self, arr):
        """Check Click"""
        x, y = pygame.mouse.get_pos()
        if self.x <= x <= self.x+self.size and self.y <= y <= self.y+self.size:
            return self.changeNeighbours(arr)
        return arr

    def draw(self, arr):
        """Draw light"""
        # change color
        if arr[self.arrPos[0]][self.arrPos[1]] == "y": color = (255, 255, 0)
        else: color = (255, 255, 255)
        pygame.draw.rect(self.screen, color, pygame.rect.Rect((self.x, self.y), (self.size, self.size)))


class Main:
    """Main class"""
    def __init__(self):
        """Initialize Main Class"""
        # sizes
        self.sqNum = 4
        self.sqSize = 75
        self.winSize = self.sqNum*self.sqSize

        # define screen
        self.screen = pygame.display.set_mode((self.winSize, self.winSize))
        pygame.display.set_caption("Light Game")

        self.yellow = (255, 255, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.running = True
        self.arr = [["y", "y", "y", "w"], ["w", "y", "w", "y"], ["y", "y", "y", "w"], ["w", "w", "w", "w"]]
        self.lights = []

        # create lights
        for r in range(4):
            for c in range(4):
                self.lights.append(Light(self.screen, c*self.sqSize, r*self.sqSize, r, c, self.sqSize))

    def event(self):
        """Event loop"""

        for event in pygame.event.get():
            # check exiting game
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("d")
                for l in self.lights:
                    self.arr = l.checkClick(self.arr)


    def main(self):
        """Main Function"""
        self.running = True
        while self.running:
            self.event()
            self.draw()

    def drawGrids(self):
        """Start drawing grids"""
        for r in range(self.sqNum):
            for c in range(self.sqNum):
                pygame.draw.line(self.screen, self.black, (0, c * self.sqSize), (self.winSize, c * self.sqSize), 1)
                pygame.draw.line(self.screen, self.black, (r * self.sqSize, 0), (r * self.sqSize, self.winSize), 1)

    def draw(self):
        """Draw function"""
        self.screen.fill(self.white)
        for l in self.lights:
            l.draw(self.arr)
        self.drawGrids()
        pygame.display.flip()


if __name__ == '__main__':
    Main().main()
