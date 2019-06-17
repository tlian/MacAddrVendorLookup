from setuptools import (
    setup,
    find_packages
)
from macaddress_lookup import (
    __author__,
    __version__,
    __license__,
    __email__
)
# from macaddress_lookup.macaddr_lookup import mytest

setup(
    name='macaddress_lookup',
    version=__version__,
    description='Look up vendor information of a given MAC Address',
    author=__author__,
    author_email=__email__,
    license=__license__,
    entry_points={
        'console_scripts': [
            'mac-vendor-lookup = macaddress_lookup.cli.vendor_lookup:main'
        ]
    },
    packages=find_packages(),
    install_requires=[
        'requests>=2.13.0,<3'
    ],
)
