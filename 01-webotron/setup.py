from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Christoph Heinig',
    author_email='christoph+test@heinig.xyz',
    description='Webotron 80 is a tool to deploy static websites',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/cheinig/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)