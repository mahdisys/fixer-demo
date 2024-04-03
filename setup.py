from setuptools import setup


setup(name='fixer-demo',
      version='0.2',
      description='Fixer service demo package',
      url='https://github.com/mahdisys/fixer-demo.git',
      author='Hosein',
      author_email='mahdikhorshidio@gmail.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)
