from time import sleep
import threading
from helpers import locate, locateAndClick, locateAndClickMoveAfter, getAttacks, getFullPaths, attack


prefix = './images/clan'

imageNames = {
    'ClanBattle': 'ClanBattle.png',
    'ClanToAttack': 'image.png',
    'AttackBtn': "AttackBtn.png",
    'ManualOption': "ManualOption.png",
    'BattleWon': 'BattleWon.png',
    'StaminaZero': 'StaminaZero.png',
    'IncreaseStamina': "IncreaseStamina.png",
    'UseRoll': 'UseRoll.png',
    'RestoreStamina': "RestoreStamina.png",
    'attacks': getAttacks()
}


class ClanBattleBot:
    def __init__(self):
        self.images = getFullPaths(pathPrefix=prefix, imageNames=imageNames)
        self.running = False
        self.loop_finished = False
        self.loop_count = 0
        self.turn = 0
        self.thread = None

    def checkIfStaminaIsZero(self):
        return locate(self.images['StaminaZero'], confidence=0.9)

    def restoreStamina(self):
        if locateAndClick(self.images['IncreaseStamina']):
            if locateAndClick(self.images['UseRoll']):
                if locateAndClick(self.images['RestoreStamina']):
                    sleep(2)
                    return True

    def clickClanAndAttack(self):
        actions = [
            (0, self.images['ClanBattle']),
            (1, self.images['ClanToAttack']),
            (2, self.images['AttackBtn']),
            (3, self.images['AttackBtn']),
            (4, self.images['ManualOption'])
        ]
        for index, image in actions:
            if index == 4:
                locateAndClickMoveAfter(image, confidence=0.9)
            else:
                locateAndClickMoveAfter(image)
            if index == 0:
                sleep(1)
            else:
                sleep(0.5)
        return True

    def run(self):
        while self.running:
            self.loop_finished = False
            if self.checkIfStaminaIsZero():
                self.restoreStamina()
            else:
                if self.clickClanAndAttack():
                    sleep(1)
                    while not self.loop_finished:
                        if locateAndClick(self.images['BattleWon']):
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
