from os.path import join, dirname, abspath

from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(name="robotframework-seleniumheallocator",
      packages=find_packages(include=['SeleniumHealLocator.keywords',
                                      'SeleniumHealLocator.utilities',
                                      'SeleniumHealLocator']),
      version='1.0.0',
      description='RF Selenium Auto Heal',
      author='Me',
      license='Me',
      install_requires=REQUIREMENTS
      )
