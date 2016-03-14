from cloudify import ctx
from cloudify.decorators import operation

@operation
def set_hello(some_property, **kwargs):
    # setting node instance runtime property
    ctx.instance.runtime_properties['hello'] = 'world'