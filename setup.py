from setuptools import setup, find_packages

setup(
    name='pyqt-music-sheet-graphics-view',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt music sheet graphics view (only music sheet lines exist currently)',
    url='https://github.com/yjg30737/pyqt-music-sheet-graphics-view.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)