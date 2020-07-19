import rockBlock

from rockBlock import rockBlockProtocol

class mtExample(rockBlockProtocol):

    def main(self):
        rb = rockBlock.rockBlock("/dev/ttyUSB0", self)

        rb.requestMessageCheck()

        rb.close()

    def rockBlockRxStarted(self):
        print("rockBlockRxStarted")

    def rockBlockRxFailed(self):
        print("rockBlockRxFailed")

    def rockBlockRxReceived(self, mtmsn, data):
        print("rockBlockRxReceived " + str(mtmsn) + " " + data)

    def rockBlockRxMessageQueue(self, count):
        print("rockBlockRxMessageQueue " + str(count))


if __name__ == '__main__':
    mtExample().main()