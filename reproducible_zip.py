#!/usr/bin/env python2
import os, sys, mmap
from zipfile import ZipFile, ZipInfo

with ZipFile(sys.argv[1], "w") as z:
    for filename in sys.argv[2:]:
        with open(filename, "r+b") as f:
            mm = mmap.mmap(f.fileno(), 0)
            try:
                info = ZipInfo(os.path.basename(filename), (1980, 1, 1, 0, 0, 0))
                info.create_system = 3 # Unix
                info.external_attr = 0644 << 16L # rw-r--r--
                z.writestr(info, mm)
            finally:
                mm.close()
