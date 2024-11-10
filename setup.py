import io
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='algorithms',
      version='0.0.1',
      description='Pythonic Data Structures and Algorithms',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/wlg-and-yang/algorithms',
      author='Algorithms Team & Contributors',
      author_email="598602465@qq.com",
      license='Apache-2.0',
      packages=find_packages(exclude=('tests', 'tests.*', 'tests_ut')),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.10',
          ],
      zip_safe=False)
