from setuptools import setup,find_packages

setup(name='my_quandl',
      version='0',
      description='acess my quandl account',
      url='',
      author='Robinson Garcia',
      author_email='rlsg.mec@hotmail.com',
      license='MIT',
      include_package_data=True,
      packages=['my_quandl'],
      zip_safe=False,
      install_requires=['Quandl>=3.3.0']
      )
