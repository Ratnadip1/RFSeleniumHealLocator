from os.path import join, dirname, abspath

from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(name="robotframework-seleniumheallocator",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      version='1.0.0',
      description='RF Selenium Auto Heal',
      author='Ratnadip Chaudhuri',
      author_email='ratnadip.chaudhuri@gmail.com',
      license='Open',

      install_requires=REQUIREMENTS
      )
