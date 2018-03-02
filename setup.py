from setuptools import setup,find_packages
from setuptools.command.install import install

class adjustments(install):
    def run(self):
        install.run(self)
        import derivatives_pricing
        import sys
        import os
        #path_port = os.path.abspath(os.path.dirname(sys.argv[0]))
        path_port = 'usr/local/lib/python3.6/dist-packages/derivatives_pricing*'
        os.system('chmod -R 777 /' + path_port)
        os.system('chmod -R 777 /usr/local/bin/optvalue.py')
        print('done adjustments')

setup(name='derivatives_pricing',
      version='0',
      description='script to evaluate the price of different derivatives',
      url='https://github.com/RobinsoGarcia/PortfolioOptimization',
      author='Robinson Garcia',
      author_email='rlsg.mec@hotmail.com',
      license='MIT',
      entry_points={'console_scripts':['optvalue = derivatives_pricing.get_values:main']},
      include_package_data=True,
      packages=['derivatives_pricing','derivatives_pricing.sim','derivatives_pricing.load_data',
      'derivatives_pricing.securities'],

      zip_safe=False,
      cmdclass={'install':adjustments},
      install_requires=[
          'Quandl>=3.3.0',
          'numpy>=1.14.0',
          'pandas>-0.22.0',
          'matplotlib>=2.1.2',
          'pandas_datareader>=0.5.0',
          'beautifulsoup4>=4.6.0',
          'yahoo-finance>=1.4.0',
          'scipy>=1.0.0'
      ]
      )
