from setuptools import setup

setup(
    name="ohnoyoudidnt",
    version="0.1",
    packages=["ohnoyoudidnt"],

    entry_points={
        "doc8.extension.check": [
            "one = ohnoyoudidnt.one:Formatter"
        ]
    }

)