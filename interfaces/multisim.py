'''
pc-drone using MultiSim

Copyright (c) 2023 Simon D. Levy

MIT License
'''

from multicopter_server import MulticopterServer


class Interface:

    def __init__(self, log_dir, timestamp):

        pass

    def acquireState(self):

        return True

    def display(self, command, flighttoc, flighttic, x_target, ypos_target):

        return 0

    def getState(self):

        return None

    def isReady(self):

        return True

    def record(self):

        pass

    def sendCommand(self, command):

        pass

    def getCommandResponse(self):

        return ''

    def resetComms(self):

        pass

    def close(self):

        pass

    def takeSnapshot(self, index):

        pass
