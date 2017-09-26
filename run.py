import sys
import logging
from yowsup.stacks import YowStackBuilder
from layer import EchoLayer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer

logFormatter = logging.Formatter("%(asctime)s - %(message)s")
logger = logging.getLogger()

fileHandler = logging.FileHandler("on_votar.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

logger.setLevel(logging.INFO)


CREDENTIALS = ("yowsup_id", "yowsup_password")


class YowsupEchoStack(object):
    def __init__(self, credentials, encryptionEnabled=True):
        stackBuilder = YowStackBuilder()

        self.stack = stackBuilder\
            .pushDefaultLayers(encryptionEnabled)\
            .push(EchoLayer)\
            .build()

        self.stack.setCredentials(credentials)

        self.stack.broadcastEvent(
            YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    def start(self):
        try:
            print("\nIniciant loop...")
            self.stack.loop()
        except AuthError as e:
            print("Authentication Error: %s" % e.message)


def initialize():
    stack = YowsupEchoStack(CREDENTIALS)
    run(stack)


def run(stack):
    try:        
        stack.start()
    except KeyboardInterrupt:
        print("\nHasta nunqui!")
        sys.exit(0)
    except:
        print("\nExcepcio descontrolada, tornem a executar")
    run(stack)


if __name__ == '__main__':
    initialize()
