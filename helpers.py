from pyautogui import locateOnScreen, click, ImageNotFoundException

region = (0, 260, 960, 540)
default_confidence = 0.7
default_offset_left = 20
default_offset_top = 20


attackPathPrefix = './images/attacks'

attackNames = ['first.png', 'second.png',
               'third.png', 'fourth.png', 'fifth.png']


def getAttacks():
    attacks = []
    for attack in attackNames:
        attacks.append(attackPathPrefix + '/' + attack)
    return attacks


def getFullPaths(pathPrefix, imageNames):
    images = {}
    for key, value in imageNames.items():
        if not isinstance(value, list):
            images[key] = pathPrefix + '/' + value
        else:
            images[key] = value
    return images


def attack(self):
    if self.turn < len(self.images['attacks']):
        attack_name = self.images['attacks'][self.turn]
        if locateAndClick(attack_name):
            self.turn += 1


def locate(image, confidence=default_confidence, ):
    try:
        locateOnScreen(
            image, confidence=confidence, region=region)
        return True
    except ImageNotFoundException:
        return False


def locateAndClick(image, confidence=default_confidence, left=default_offset_left, top=default_offset_top):
    try:
        location = locateOnScreen(
            image, confidence=confidence, region=region)
        click(location.left + left, location.top + top)
        return True
    except ImageNotFoundException:
        return False


def locateAndClickMoveAfter(image, confidence=default_confidence, left=default_offset_left, top=default_offset_top):
    try:
        location = locateOnScreen(
            image, confidence=confidence, region=region)
        click(location.left + left, location.top + top)
        click(location.left, location.top)
        return True
    except ImageNotFoundException:
        return False
