from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n This class gives me a headache"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = "smtp.gmail.com"
    port = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    

    # Fill in start
    clientSocket = socket.socket()
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024)
    print received
    if recv[:3] != '220':
	    print '220 reply not received from server.'
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: ' + sender + '\r\n'
    clientSocket.write(mailFromCommand)
    recv2 = clientSocket.read(1024)
    print recv2
    if recv2[:3] != '250':
	      print '250 reply not received from server.'
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO: ' + recipient + '\r\n'
    clientSocket.write(rcptToCommand)
    recv3 = ssl_clientSocket.read(1024)
    print recv3
    if recv3[:3] != '250':
	      print '250 reply not received from server.'
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.write(dataCommand)
    recv4 = ssl_clientSocket.read(1024)
    print recv4
    if recv4[:3] != '354':
	      print '354 reply not received from server.'
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.write(msg)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
   ssl_clientSocket.write(endmsg)
   recv5 = ssl_clientSocket.read(1024)
   print recv5
   if recv5[:3] != '250':
	      print '250 reply not received from server.'
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    ssl_clientSocket.write(quitCommand)
    recv6 = ssl_clientSocket.read(1024)
    print recv6
    if recv6[:3] != '221':
	      print '221 reply not received from server.'
    # Fill in end
