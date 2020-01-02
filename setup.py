"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://santhoshse7en.github.io/ML_APIs/
https://santhoshse7en.github.io/ML_APIs/docs/
"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['Google', 'ML APIs', 'Cloud', 'ML_APIs', 'machine_learning']

setuptools.setup(
    name='ML_APIs',
    version='0.0.1',
    author='M Santhosh Kumar',
    author_email='santhoshse7en@gmail.com',
    description='A package for google ML_APIs.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://santhoshse7en.github.io/ML_APIs',
    package_dir={'ML_APIs': 'ML_APIs'},
    packages=setuptools.find_packages(),
    install_requires=['pandas==0.25.3', 'google-api-python-client==1.7.11', 'google-api-core==1.15.0',
                      'google-auth==1.10.0', 'google-auth-httplib2==0.0.3', 'google-cloud-core==1.1.0',
                      'google-cloud-datastore==1.10.0', 'google-cloud-language==1.3.0', 'google-cloud-storage==1.23.0',
                      'google-cloud-videointelligence==1.12.1', 'google-cloud-vision==0.41.0', 'google-resumable-media==0.5.0',
                      'googleapis-common-protos==1.6.0', 'oauth2client==4.1.3', 'psycopg2==2.8.4'],
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
    include_package_data=True
)
