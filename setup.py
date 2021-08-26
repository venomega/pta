from distutils.core import setup

setup(
    name='pta',
    author="venomega",
    author_email="0x7976ef12c28610a2f10bf786960f18f3098d8715@ethmail.cc",
    version='0.1',
    packages=['pta', ],
    requires=['ipaddr' ],
    licence='GPL-3',
    url="https://github.com/venomega/pta",
    download_url="",
    description="Application for sharing files with peers on same LAN",
    long_description=open("README.md").read(),

)
