from time import sleep
import threading
from helpers import locateAndClick, locateAndClickMoveAfter, getAttacks, getFullPaths, attack

prefix = './images/xp'

imageNames = {
    'AcceptMission': 'AcceptMission.png',
    'Done': 'Done.png',
    'Grade': "Grade.png",
    'Mission': "Mission.png",
    'MissionBtn': 'MissionBtn.png',
    'RightBtn': 'RightBtn.png',
    'attacks': getAttacks()
}


class XPFarmBot:
    def __init__(self):
        self.images = getFullPaths(pathPrefix=prefix, imageNames=imageNames)
        self.running = False
        self.loop_finished = False
        self.loop_count = 0
        self.turn = 0
        self.thread = None

    def gotoMissions(self):
        locateAndClick(self.images['MissionBtn'])
        sleep(1)
        return True

    def clickGrade(self):
        locateAndClick(self.images['Grade'], confidence=0.9)
        sleep(0.5)
        return True

    def movePage(self):
        locateAndClick(self.images['RightBtn'])
        sleep(0.5)
        return True

    def mission(self):
        return locateAndClick(self.images['Mission'])

    def acceptMission(self):
        return locateAndClickMoveAfter(self.images['AcceptMission'], left=350, top=400)

    def run(self):
        while self.running:
            self.loop_finished = False
            if self.gotoMissions():
                if self.clickGrade():
                    if self.movePage():
                        if self.mission():
                            if self.acceptMission():
                                while not self.loop_finished:
                                    if locateAndClick(self.images['Done'], left=50, top=50):
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
