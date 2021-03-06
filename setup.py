from setuptools import setup

setup(
    name='smpa-murphy',
    packages=['murphy'],
    version='1.0.0-alpha.1',
    license='MIT',
    description='Murpheus is a powerful processor that is used to analyze a ton of twitter data from the internet archive.',
    long_description="""# Murpheus\n\n* Murpheus is a powerful processor that is used to analyze a ton of twitter data from the internet archive""",
    long_description_content_type="text/markdown",
    author='Ali Abbas',
    author_email='v2thegreat@gmail.com',
    url='https://github.com/Social-Media-Public-Analysis/murpheus',
    download_url='https://github.com/Social-Media-Public-Analysis/murpheus/archive/v1.0.0-alpha.1.tar.gz',
    keywords=['DASK', 'BIG DATA', 'MACHINE LEARNING'],
    install_requires=[
        'tqdm',
        'numpy',
        'pandas',
        'dask[complete]',
        'nltk',
        'pytest',
        'pyfiglet',
        'emoji'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
