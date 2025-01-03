# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.0"
def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "bitlaunch Pulumi Package - Development Version"


setup(name='pulumi_bitlaunch',
      python_requires='>=3.8',
      version=VERSION,
      description="A Pulumi package for creating and managing bitlaunch cloud resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords='webwarrior-ws bitlaunch category/cloud',
      url='https://www.pulumi.com',
      project_urls={
          'Repository': 'https://github.com/webwarrior-ws/pulumi-bitlaunch'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'pulumi_bitlaunch': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
