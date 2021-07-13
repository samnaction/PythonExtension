from setuptools import setup
import distutils
import sys

from setuptools.dist import Distribution

from distutils.sysconfig import get_python_lib
relative_site_packages = get_python_lib().split(sys.prefix+os.sep)[1]
date_files_relative_path = os.path.join(relative_site_packages, "CppProject")

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True


setup(
    name='CppProject',
    version='1.0',
    description='CppProject Library',
    packages=['CppProject'],
    package_data={
        'CppProject': ['CppProject.pyd'],
    },
    data_files = [(date_files_relative_path, ["CppExport.dll"])],
    distclass=BinaryDistribution
)