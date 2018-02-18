from setuptools import setup,find_packages

setup(name='derivatives_pricing',
      version='0',
      description='asset pricing',
      url='https://github.com/RobinsoGarcia/PortfolioOptimization',
      author='Robinson Garcia',
      author_email='rlsg.mec@hotmail.com',
      license='MIT',
      include_package_data=True,
      packages=['derivatives_pricing'],
      zip_safe=False,
      install_requires=[
          'Quandl>=3.3.0',
          'numpy>=1.14.0',
          'pandas>-0.22.0'
          'matplotlib>=2.1.2',
          'pandas_datareader>=0.5.0',
          'beautifulsoup4>=4.6.0'
      ]
      )
