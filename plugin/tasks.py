from cloudify import ctx
from cloudify.decorators import operation
import os


@operation
def set_hello(**kwargs):
    # setting node instance runtime property
    ctx.instance.runtime_properties['hello'] = 'world'

@operation
def kkill(**kwargs):
	try:
		with open('/tmp/node.pid', 'r') as file:
			pid = f.read().strip()
		ctx.logger.info('stopping node server [pid={0}]'.format(pid))
		os.system('kill -9 {0}'.format(pid))
	except IOError:
		ctx.logger.info('node server is not running!')

@operation
def print_hosts(**kwargs):
	Path = os.getenv("HOME")
	with open(os.path.join(Path, 'test.file'),'w') as f:
		f.write('This is Test Plugin')
