from setuptools import setup, find_packages

setup(
    name='pypdl',
    version='0.0.1',
    description='People Data Labs Python Library',
    url='https://github.com/bakhtikyan/peopledatalabs-py',
    packages=find_packages(),
    install_requires=[
                        'pytest',
                        'requests',
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
    ],
)
