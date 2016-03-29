from setuptools import setup

setup(
    
    name = 'simple-plugin',
    version = '1.0',
    author = 'victor',
    packages = ['plugin'],
    license = 'LICENSE',
    zip_safe = False,
    install_requires = ['cloudify-plugins-common>=3.3']
)
 