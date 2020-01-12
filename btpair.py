import socket_con_cil_udp
import json

socket_to_mac_mini = socket_con_cil_udp.SocketDeviceCILUDP("192.168.2.20",3030)

command = json.dumps({'troposErrorCode':'SUCCESS', 'command':'SXMSG_BT_PAIR_NOTIFICATION', "btAddress":"00:01:23:45:67:89", "deviceName":"Fake BT Device", "a2dpSrc":"NotSupported", "a2dpSnk":"Supported", "cod":"Mobile Phone", "serviceId":{'IPAddr':"192.168.2.12","moduleId":8192}})

msg_header = {}
msg_header["customer"] = 0 
msg_header["dest"] = int("0x1001",16) 
msg_header["type"] = int("0x00000007",16)
msg_header["source_dest"] = int("0x00002000",16) 
msg_header["source_type"] = int("0x00020012",16)
msg_header["format_info"] = 2
msg_header["ref_number"] = 12323

socket_to_mac_mini.senCILCommand(msg_header,command)

