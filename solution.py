from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\nThis class gives me a headache"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = "smtp.gmail.com"
    port = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024)
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')
    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM: <mail@mail.com>\r\n'
    clientSocket.send(mailfromCommand)
    recv2 = clientSocket.recv(1024)
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO: <adeyaadi@gmail.com>\r\n'
    clientSocket.send(rcptToCommand)
    recv3 = clientSocket.recv(1024)
    print(recv3)
    if recv3[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'data\r\n'
    print(dataCommand)
    clientSocket.send(dataCommand)
    recv4 = clientSocket.recv(1024)
    print(recv4)
    if recv4[:3] != '354':
        print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start

    clientSocket.send(endmsg)
    recv5 = clientSocket.recv(1024)
    print(recv5)
    if recv5[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    print(quitCommand)
    clientSocket.send(quitCommand)
    recv6 = clientSocket.recv(1024)
    print(recv6)
    if recv6[:3] != '221':
        print('221 reply not received from server.')
    clientSocket.close()
# Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
