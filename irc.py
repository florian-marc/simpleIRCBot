import sys
import socket
import time


class IRC:
    irc = socket.socket()

    def __init__(self, ):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendPrivateMessage(self, receiver, msg):
        """Sending a private message to a receiver or a list of receiver

        Args:

            receiver (iterable<string>): The receiver(s) of the message. May be the nickname of the receiver, a list of names or channels separated by commas
            msg (sting): The message to be sent
        """
        self.irc.send(bytes("PRIVMSG " + ','.join(receiver) +
                            " :" + msg + "\n", "UTF-8"))
        print("PRIVMSG " + receiver + " :" + msg + "\n")
        time.sleep(5)

    def connect(self, server, port):
        """Connects to an IRC server

        Args:

            server (string): server address
            port (integer): server port
        """
        # Connecting to server
        print("Connecting to: " + server + ":" + str(port))
        self.irc.connect((server, port))

    def authentify(self, botNick, botRealName):
        """Performs authentication on the server

        Args:

            botNick (string): nickname of the bot
            botRealName (string): bot real name
        """
        # Perform user authentication
        self.irc.send(bytes("NICK " + botNick + "\n", "UTF-8"))
        self.irc.send(bytes("USER " + botNick + " " + botNick +
                            " " + botNick + " :" + botRealName + "\n", "UTF-8"))
        time.sleep(5)

    def joinChannel(self, channel):
        """Joins a channel

        Args:

            channel (string): channel to communicate on
        """
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def simpleConnect(self, server, port, channel, botNick, botRealName=""):
        """Performs a connection to a server, authentication procedure and channel connection

        Args:

            server (string): server address
            port (integer): server port
            channel (string): channel to communicate on
            botNick (string): nickname of the bot
            botRealName (string): bot real name. Defaults to botNick.
        """
        self.connect(server, port)
        if(botRealName != ""):
            self.authentify(botNick, botRealName)
        else:
            self.authentify(botNick, botNick)
        self.joinChannel(channel)

    def getResponse(self):
        """Reads the response from the server
        """
        time.sleep(1)
        # Get the response
        resp = self.irc.recv(2040)
        if resp.decode("UTF-8", "ignore").find("PING") != -1:
            print("RECEIVED PING\n" + resp.decode("UTF-8", "ignore") + "\n")
            self.irc.send(
                bytes("PONG " + resp.decode("UTF-8", "ignore").split(" ")[1] + "\r\n", "UTF-8"))
            print("SENT: \"" + "PONG " +
                  resp.decode("UTF-8", "ignore").split(" ")[1] + "\"")
        return resp.decode("UTF-8", "ignore")
