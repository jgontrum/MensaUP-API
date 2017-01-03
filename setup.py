from setuptools import setup

setup(
    name='mensaup_api',
    version='0.1',
    description='API for the Uni Potsdam Mensa',
    author='Johannes Gontrum',
    author_email='gontrum@me.com',
    include_package_data=True,
    license='MIT license',
    entry_points={
          'console_scripts': [
              'start = mensaup_api.scripts.start:run',
              'start_debug = mensaup_api.scripts.start:run_debug'
          ]
      }
)
