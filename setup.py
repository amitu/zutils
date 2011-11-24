from setuptools import setup

setup(
    name = "amitu-zutils",
    version = "0.1.0",
    url = 'http://packages.python.org/amitu-zutils/',
    license = 'BSD',
    description = "Generic Utilities for ZMQ based services",
    author = 'Amit Upadhyay',
    author_email = "upadhyay@gmail.com",
    py_modules = ["amitu.zutils"],
    namespace_packages = ["amitu"],
)
