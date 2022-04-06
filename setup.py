from setuptools import setup, find_packages

setup(
    name='pyqt-tooltip-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QWidget as a tooltip',
    url='https://github.com/yjg30737/pyqt-tooltip-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)