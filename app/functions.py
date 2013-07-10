import csv
import os
from django.http import HttpResponse, HttpResponseForbidden
from django.db.models.loading import get_model
from django.conf import settings

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

def exp_csv(qs, fname):
    model = qs.model
    #response = HttpResponse()
    #response['Content-Type'] = 'text/csv; charset=utf-8'
    #response['Content-Disposition'] = 'attachment; filename=%s.csv' % fname
    #response.write("\xEF\xBB\xBF")
    if os.path.isdir(settings.MEDIA_ROOT+'csv'):
        pass
    else:
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'csv'))

    f = os.path.join(settings.MEDIA_ROOT, 'csv/'+fname+'.csv')
    fs = open(f, 'w')
    fs.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(fs)
    #writer = csv.writer(response)
    
    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)
    
    for obj in qs:
        row = []
        for field in headers:
            if field == 'brewer':
                field = 'brewer_id'
            if field == 'style':
                field = 'style_id'
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == unicode:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)

    fs.closed
    #return response
