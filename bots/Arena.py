from time import sleep
import threading
from helpers import locate, locateAndClick,  getAttacks, getFullPaths, attack


prefix = './images/arena'

imageNames = {
    'Arena': 'Arena.png',
    'Fight': 'Fight.png',
    'OfflineMode': "OfflineMode.png",
    'ZeroStamina': "Zero.png",
    'Done': 'Done.png',
    'attacks': getAttacks()
}


class ArenaBot:
    def __init__(self):
        self.images = getFullPaths(pathPrefix=prefix, imageNames=imageNames)
        self.running = False
        self.loop_finished = False
        self.loop_count = 0
        self.turn = 0
        self.thread = None

    def gotoArena(self):
        return locateAndClick(self.images['Arena'])

    def clickOfflineMode(self):
        locateAndClick(self.images['OfflineMode'])
        sleep(1)
        return True

    def fight(self):
        locateAndClick(self.images['Fight'])
        sleep(1.5)
        return True

    def checkIfStaminaIsZero(self):
        return locate(self.images['ZeroStamina'], confidence=0.9)

    def run(self):
        while self.running:
            self.loop_finished = False
            if self.gotoArena():
                if self.clickOfflineMode():
                    if self.checkIfStaminaIsZero():
                        print('here')
                        self.stop()
                    if self.fight():
                        print('here 2')
                        while not self.loop_finished:
                            print('here 3')
                            if locateAndClick(self.images['Done']):
                                self.loop_count += 1
                                self.loop_finished = True
                                self.turn = 0
                                sleep(1)
                            else:
                                attack(self)
                                sleep(1)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None and self.thread.is_alive():
            self.thread.join()
