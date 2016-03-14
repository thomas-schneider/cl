from setuptools import setup

setup(
I   name='my_test_plugin',
    version='1.0',
    author='victor',
    packages=['test_plugin_package'],
    license='LICENSE',
    zip_safe=False,
    install_requires=['cloudify-plugins-common>=3.3'],
    test_requires=[
        "cloudify-dsl-parser>=3.4a3"
        "nose"
    ]
)
 