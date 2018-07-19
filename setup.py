from setuptools import setup,find_packages
from setuptools.command.install import install

setup(name='derivatives_pricing',
      version='1.0',
      description='script to evaluate the price of different derivatives',
      url='https://github.com/RobinsoGarcia/derivatives-pricing',
      author='Robinson Garcia',
      author_email='rlsg.mec@hotmail.com',
      license='MIT',
      scripts=['derivatives_pricing/scripts/options_pricing.py',
      'derivatives_pricing/scripts/build_dataset_quandl.py'],
      include_package_data=True,
      packages=find_packages(),
      package_data={'derivatives_pricing':['scripts/*','jupyter-notebook/*']},
      zip_safe=False,
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
