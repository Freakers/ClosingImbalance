from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


class ppro_datagram(DatagramProtocol):
    def startProtocol(self):
        # code here what you want to start upon listner creation..
        # I use this space to connect to my logging backend and inter process communication library
        print('starting up..')

    def datagramReceived(self, data, addr):
        # decode byte data from UDP port into string, and replace spaces with NONE
        msg = data.decode("utf-8").replace(' ', 'NONE')

        # empty dict we will populate with the string data
        message_dict = {}

        # when processing PPro8 data feeds, processing the line into a dictionary is very useful:
        for item in msg.split(','):
            couple = item.split('=')
            message_dict[couple[0]] = couple[1]
        # now you can call specific data by name in the line you're processing instead of counting colums
        # See the print statement below for examples

        print('{} {} {}'.format(message_dict['Symbol'], message_dict['Message'], msg))

        # but any named column will not be callable:
        # message_dict['MarketTime']
        # message_dict['Price']

    def connectionRefused(self):
        print("No one listening")


reactor.listenUDP(5555, ppro_datagram())
reactor.run()
