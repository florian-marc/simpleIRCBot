from irc import IRC

server = "" #Provide a valid IP address
port = 6667
channel = "#" #Provide a valid channel name
myNick = "myNickname"

irc = IRC()

irc.simpleConnect(server, port, channel, myNick, myNick)
irc.getResponse()
