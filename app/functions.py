def get_crc32( string ):
    string = string.lower()        
    bytes = bytearray(string.encode())
    crc = 0xffffffff;
    for b in bytes:
        crc = crc ^ (b << 24)          
        for i in range(8):
            if (crc & 0x80000000 ):                 
                crc = (crc << 1) ^ 0x04C11DB7                
            else:
                crc = crc << 1;                        
        crc = crc & 0xFFFFFFFF
        
    return '%08x' % crc

def rchop(thestring, ending):
  if thestring.endswith(ending):
    return thestring[:-len(ending)]
  return thestring