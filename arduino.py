'''
Arduino communications for PC-Drone

Copyright (c) 2023 Simon D. Levy

MIT License
'''

import serial
import struct

class Arduino:

    def __init__(self, portname='/dev/ttyACM0'):

        # Support hot-plugging Arduino
        self.port = None
        self.portname = portname

    def write(self, demands):

        print('%i,%i,%i,%i' % (demands[0], demands[1], demands[2], demands[3]), end= ' ')

        if self.port is None:

            try:
                self.port = serial.Serial(self.portname, 115200, timeout=.001)
            except:
                pass

        else:

            try:

                # Use zero as a sentinel
                self.port.write(
                        struct.pack(
                            'HHHHH', 
                            0, 
                            int(demands[0]), 
                            int(demands[1]), 
                            int(demands[2]), 
                            int(demands[3])))

                print('*', end=' ')

            except Exception as e:
                print('\nArduino error: ' + str(e))

        print()

    def readline(self):

        return None if self.port is None else self.port.readline()

    def close(self):

        if self.port is not None:
            self.port.close()
