from setuptools import setup, find_packages

setup(
    name='Filipino Native Language Identifier',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    url='',
    license='',
    author='Red Periabras',
    author_email='redperiabras@gmail.com',
    description='Porject in Natural Language Processing',
    install_requires=[
        'nltk'
    ],
    package_data={
        'phidentifier': ['data/**/*', 'data/*'],  # Include all files in the data folder
    },
)
