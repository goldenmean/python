"""
:Authors:       Nick Wright
:Copyright:     Cambridge Silicon Radio Ltd. All Rights Reserved.

This class contains functions for using the Command-Acknowledge protocol developed by CSR.

A simple Command-Acknowledge protocol that runs over UDP has been developed by CSR.
It is used by...
Tropos
Critique (Audio Analyser)
"""

import socket
import struct
import time

class SocketDeviceCILUDP(object):
    
    def __init__(self,host,port,timeout=0.1):
        """
        PARAMETERS
            *host* The IP address of the socket being connected to.
            *port* The port of the socket being connected to.
            *timeout* The timeout to be used for the socket connection.

        """
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(timeout)
        self.sock.connect((host, port))

        self.lastUsedRefNumber = 0

    def getRefNumber(self):
        """
        Returns a unique reference number. 
        Used so received messages can be matched up with sent messages.
        """

        self.lastUsedRefNumber += 1

        return self.lastUsedRefNumber


    def uSec2time(self,usec):
        """
        Converts milli seconds since midnight to a time.
        PARAMETERS:
            *usec* Number of milli seconds since midnight.
            
        Returns:
            A string containing a time.
        """
        
        return  time.strftime('%H:%M:%S',time.gmtime(usec / 1000)) + ".%s" % (usec % 1000)

    def time2uSec(self,time=None):
        # 15:00
        
        return 54000000

    def number2fourBytes(self,number):
        """
        A function that packs a number into 4-bytes ready for sending in a UDP packet.
        PARAMETERS:
            *number* A number that is to be packed into 4 bytes.

        Returns:
            4 bytes of data containing the number ready for use in a UDP message.

        """
        return struct.pack('<I',number)
        

    def fourbytes2number(self,fourBytes):
        """
        A function that unpacks a number from 4-bytes of data for decoding UDP messages.
        PARAMETERS:
            *fourBytes* 4 Bytes of data containing a number.
        Returns: 
            The number that was packed into the 4 bytes of data.

        """
        return struct.unpack('<I', fourBytes)
        
    def nbytes2number(self,nbytes,n):
        if n is 2:
            return struct.unpack('<H', fourBytes)
        elif n is 4:
            return struct.unpack('<I', fourBytes)
        elif n is 8:
            return struct.unpack('<Q', fourBytes)
        else:
            raise Exception("n should be 2, 4, or 8")
        
    def number2nBytes(self,number,n):
        if n is 2:
            return struct.pack('<H',number)
        elif n is 4:
            return struct.pack('<I',number)
        elif n is 8:
            return struct.pack('<Q',number)
        else:
            raise Exception("n should be 2, 4, or 8")        

    def decodeReceivedMessage(self,msg,num4bytes):
        """
        A function for decoding messages received over UDP.

        UDP messages contain a number of 4-byte blocks containing 
        numbers optionally followed by a text string.
        
        This function converts the UDP messages into the required amount 
        of 4-byte sections and then converts them to numbers.

        PARAMETERS:
            *msg* The USP messages that is to be decoded.
            *num4bytes* The number of 4-byte blocks in the UDP message before the text string.

        Returns:
            A list containing all the 4-byte blocks converted to numbers, 
            with the last element being the text string if it exists.

        """
        msg_data = []
        
        for x in range(0,num4bytes*4,4):
            msg_data.append(self.fourbytes2number(msg[x:x+4]))
            
        msg_data.append(msg[len(num4bytes*4*chr(0)):])
        
        return msg_data

    def listenForLineOfData(self,amounOfData=1024):
        """
        A function that listens for 1 line of data on the UDP socket.

        This function is used when a message is expected.

        PARAMETERS
            *amounOfData* The maximum size the data will be.
        Returns:
            A string containing the UDP message received.
        """

        return self.sock.recv(amounOfData)
    
    def listenForNSecs(self,duration,timeStampIndex=None,print_func=None,silent=False):
        """
        A function that keeps listening for data on the UDP socket, for a set time duration.

        This function is used when messages may or may not be expected. 

        The functions assumes the UDP messages received contain one of the following:
            4 lots of 4-bytes with no text string.
            5 lots of 4-bytes with a text string.

        PARAMETERS
            *duration* The amount of time the function is to listen on the socket for.
            *timeStampIndex* The index of the 4-byte number that contains the time stamp.
                                If given the number will be converted into a time stamp.
                                If None then nothing will be done.
            *print_func* A function that takes a single string argument. 
                                Every time a message is received the function is called with the message as the argument.
                                Used for printing to log files.
                                If None any message received is printed to the screen.
            *silent* When set to True any received message will not be printed.

        Returns
            A list containing all the UDP messages received during the time given.


        """
        start_time = time.time()
        receivedMessages = []
        while 1:
            try:
                recv_msg = self.sock.recv(2048)
                if len(recv_msg) == 16:
                    num_bytes = 4
                else:
                    num_bytes = 5
                decoded_recv_msg = self.decodeReceivedMessage(recv_msg,num_bytes)
                
                if timeStampIndex is not None:
                    decoded_recv_msg[timeStampIndex] = (self.uSec2time(decoded_recv_msg[timeStampIndex][0]),)
                    
                receivedMessages.append(decoded_recv_msg)

                if not silent:
                    if print_func is not None:
                        print_func("Received: %s" % decoded_recv_msg)
                    else:
                        print decoded_recv_msg
            except:
                pass
            
            if time.time() >= start_time + duration:
                break
                
        return receivedMessages
                
    def sendCommand(self,refNumber,command,type=2):
        """
        A function for sending command message to a UDP socket.

        A command message is assumed to be of the form:
        4-bytes containing a number giving details of the message type.
        4-bytes containing a reference number.
        Text string containing the command.

        PARAMETERS
            *refNumber* Any number. Replies will use the same reference number.
            *command* The command to be sent to the UDP socket.
            *type* The command type default is 2 = ASCII Command.

        """
        msg= self.number2fourBytes(type) + self.number2fourBytes(refNumber) + command
        self.sock.send(msg)
        
    def senCILCommand(self,header,command):
        customer_length = 2
        dest_length = 2
        type_length = 4
        source_dest_length = 4
        source_type_length = 4
        ref_number_length = 4
        timestamp_length = 4
        format_info_length = 4
        
        if "timestamp" not in header:
            header["timestamp"] = self.time2uSec()
        
        msg = self.number2nBytes(header["dest"],dest_length)        
        msg += self.number2nBytes(header["customer"],customer_length)
        
        msg += self.number2nBytes(header["type"],type_length)
        msg += self.number2nBytes(header["source_dest"],source_dest_length)
        msg += self.number2nBytes(header["source_type"],source_type_length)
        msg += self.number2nBytes(header["ref_number"],ref_number_length)
        msg += self.number2nBytes(header["timestamp"],timestamp_length)
        msg += self.number2nBytes(header["format_info"],format_info_length)
        msg += command
        
        print msg
        
        self.sock.send(msg)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
