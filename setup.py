# coding=utf-8
# !/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    print 'No setuptools installed, use distutils'
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='wunderbear',
    packages=[
        'wunderbear',
        'wunderbear.tools',
        'wunderbear.tests'
    ],
    package_dir={
        'wunderbear': 'src/wunderbear',
        'wunderbear.tools': 'src/wunderbear/tools',
        'wunderbear.tests': 'src/wunderbear/tests'
    },
    package_data={'': [
        'src/wunderbear/main.ini'
    ]},
    data_files=[
        ('', [
            'src/wunderbear/main.ini'
        ]),
    ],
    test_suite="wunderbear.tests",
    include_package_data=True,
    install_requires=required,
    version='1.0',
    description='python project skeleton',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='http://github.com/paoolo/python-project-skeleton',
    download_url='http://github.com/paoolo/python-project-skeleton',
    keywords=[
        'skeleton'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description='''\
'''
)
