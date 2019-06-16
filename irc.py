import socket
import time


class IRC:
    irc = socket.socket()

    def __init__(self, ):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        """Sends a message in a channel

        Args:

            channel (string): channel name
            msg (string): message to send through the channel
        """
        # Sending a private message
        self.irc.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def connect(self, server, port):
        """Connects to an IRC server

        Args:

            server (string): server address
            port (integer): server port
        """
        # Connecting to server
        print("Connecting to: " + server + ":" + port)
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
