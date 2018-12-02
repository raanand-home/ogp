import redis
from rom import util
import datetime

util.set_connection_settings(host='redis', db=7)

import rom

# All models to be handled by rom must derived from rom.Model
class Stories(rom.Model):
    url = rom.String(required=True, unique=True, suffix=True,keygen=rom.FULL_TEXT)
    data = rom.Json()
    status = rom.String(default='pending')
    updated_time = rom.DateTime(default=datetime.datetime.utcnow())
    id = rom.PrimaryKey(index = True)




