from setuptools import setup

APP = ['cpu_temp.py']
DATA_FILES = ['osx-cpu-temp']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'tmp.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='MacOS CPU Temperature',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)