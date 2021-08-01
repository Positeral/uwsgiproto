import struct
import platform


def uwsgipacker(modifier1, modifier2=0):
    pack_header = struct.Struct('<BHB').pack
    pack_uint16 = struct.Struct('<H').pack

    def pack(kw):
        data = []

        for k, v in kw.items():
            if not isinstance(k, bytes):
                k = k.encode('utf8')

            if not isinstance(v, bytes):
                v = v.encode('utf8')

            data.append(pack_uint16(len(k)) + k)
            data.append(pack_uint16(len(v)) + v)

        data = b''.join(data)
        return pack_header(modifier1, len(data), modifier2) + data

    return pack


spoolpack = uwsgipacker(modifier1=17)
spoolprefix = 'uwsgi_spoolfile_on_' + platform.node() + '_'

SPOOL_OK     = -2
SPOOL_RETRY  = -1
SPOOL_IGNORE =  0

