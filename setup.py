from setuptools import setup, find_packages

classifiers=[
'Development Status :: 5 - Production/Stable', 
'Intended Audience :: Education',
'Operating System :: Microsoft :: Windows :: Windows 10',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3'
]

setup(
    name= 'DSA_in_Python', 
    version='0.0.1',
    description='Contains useful functions', 
    Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG. txt').read(),
    url='',
    author='Armaan Chauhan',
    author_email='armaanchauhan268@gmail.com',
    License="MIT",
    classifier=classifiers, 
    keywords='data structures',
    packages=find_packages(),
    install_requires=['']
)