/dev/sde1: UUID="2d0605e1-b5a7-4c93-b300-d4039e2276d7" TYPE="crypto_LUKS" PARTLABEL="GREENBACKUP" PARTUUID="87437853-e9ca-4526-bd32-10fbd276e44d"

kalibur@kalibur-mce:~$ sudo cryptsetup luksDump /dev/sde1
LUKS header information for /dev/sde1

Version:       	1
Cipher name:   	aes
Cipher mode:   	xts-plain64
Hash spec:     	sha256
Payload offset:	4096
MK bits:       	256
MK digest:     	d3 48 46 57 d3 43 83 5b 5b 6e 1a 58 65 b9 09 93 5d e6 00 08 
MK salt:       	9b 1d 82 21 5e 52 a8 9e 7d e2 ef 06 51 c4 37 50 
               	07 e7 4e 65 79 30 cc c7 a5 97 a6 7e d4 56 c8 0f 
MK iterations: 	156000
UUID:          	2d0605e1-b5a7-4c93-b300-d4039e2276d

root@kalibur-mce:~# cryptsetup status GREENBACKUPS
/dev/mapper/GREENBACKUPS is active.
  type:    LUKS1
  cipher:  aes-xts-plain64
  keysize: 256 bits
  device:  /dev/sde1
  offset:  4096 sectors
  size:    3907022848 sectors
  mode:    read/write

