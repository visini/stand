from setuptools import setup

APP = ["stand.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "icon.icns",
    "plist": {"CFBundleShortVersionString": "0.2.0", "LSUIElement": True},
    "packages": ["rumps", "paramiko", "cffi"],
}

setup(
    app=APP,
    name="Stand",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=["rumps", "paramiko", "cffi"],
)
