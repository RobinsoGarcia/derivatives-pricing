from setuptools import setup,find_packages
from setuptools.command.install import install

setup(name='derivatives_pricing',
      version='0',
      description='script to evaluate the price of different derivatives',
      url='https://github.com/RobinsoGarcia/PortfolioOptimization',
      author='Robinson Garcia',
      author_email='rlsg.mec@hotmail.com',
      license='MIT',
      entry_points={'console_scripts':['optvalue = derivatives_pricing.get_values:main']},
      scripts=['derivatives_pricing/scripts/options_pricing.py']
      include_package_data=True,
      packages=find_packages(),
      '''['derivatives_pricing','derivatives_pricing.sim','derivatives_pricing.load_data',
      'derivatives_pricing.securities']'''
      zip_safe=False,
      cmdclass={'install':adjustments},
      install_requires=[
          'Quandl>=3.3.0',
          'numpy>=1.14.0',
          'pandas>-0.22.0',
          'matplotlib',
          'pandas_datareader>=0.5.0',
          'beautifulsoup4>=4.6.0',
          'yahoo-finance>=1.4.0',
          'scipy>=1.0.0'
      ]
      )
