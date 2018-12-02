import connexion

app = connexion.App(__name__, specification_dir='swagger/')

import redis
from rom import util

util.set_connection_settings(host='redis', db=7)

if __name__ == '__main__':
	app.add_api('api.yaml')
	app.run(port=5001)