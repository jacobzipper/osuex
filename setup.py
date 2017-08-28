from setuptools import setup
import osuex
setup(
    name = "osuex",
    version = "0.0.1",
    author = "Jacob Zipper",
    author_email = "zipper@jacobzipper.com",
    description = ("An osu extraction tool for linux users"),
    url = "http://packages.python.org/osuex",
    packages=['osuex'],
    entry_points={
        "console_scripts": [
            "osuex = osuex.osuex:do",
        ]
    },
    install_requires=[
        'subprocess',
        'click'
]
)
