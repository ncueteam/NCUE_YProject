import uasyncio
from lib.device.segment_7 import displayor

from lib.file_set import FileSet

fileset = FileSet(folder='database',file_name='wifi')
fileset.initialize()
fileset.add("302", "0937565253")
fileset.add("V2041", "123456789")


loop = uasyncio.get_event_loop()
loop.run_until_complete(displayor.main())
