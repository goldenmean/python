import socket_con_cil_udp
import json

#Send Message to TM port: 3005
socket_cil = socket_con_cil_udp.SocketDeviceCILUDP("192.168.2.3",3005)

#Construct JSON payload to send
#command = json.dumps({'troposErrorCode':'SUCCESS', 'command':'SXMSG_BT_AUDIO_CONNECT_NOTIFICATION', "btAddress":"00:01:23:45:67:89", "deviceName":"Fake BT Device", "a2dpSrc":"NotSupported", "a2dpSnk":"Supported", "cod":"Mobile Phone", "a2dpConnected":"YES", "localRole":"Source", "serviceId":{'IPAddr':"192.168.2.12","moduleId":8192}})
command = json.dumps({'messageName':'SXMSG_STOP_SERVICE', "serviceId":{'IPAddr':"192.168.2.3","moduleId":8208}})

msg_header = {}
msg_header["customer"] = 0 
msg_header["dest"] = 4096
msg_header["type"] = int("0x00000007",16)
msg_header["source_dest"] = 4097
msg_header["source_type"] = int("0xFFFFFFFF",16)
msg_header["format_info"] = 2
msg_header["ref_number"] = 12324 
socket_cil.senCILCommand(msg_header,command)


"""
msg_header = {}
msg_header["customer"] = 0 
msg_header["dest"] = int("0x1001",16) 
msg_header["type"] = int("0x00000007",16)
msg_header["source_dest"] = int("0x00002000",16) 
msg_header["source_type"] = int("0x0002000F",16)
msg_header["format_info"] = 2
msg_header["ref_number"] = 12324
socket_cil.senCILCommand(msg_header,command)

"""