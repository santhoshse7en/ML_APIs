import setuptools

setuptools.setup(
    name='ML_APIs',
    version='0.1.dev0',
    author='M Santhosh Kumar',
    author_email=' ',
    description='A package for google ML_APIs.',
    url='https:gitlab.com/Fanlytiks/twitter-essentials',
    package_dir={'ML_APIs': 'ML_APIs'},
    packages=setuptools.find_packages(),
    install_requires=['pandas==0.25.3', 'google-api-python-client==1.7.11', 'google-api-core==1.15.0',
                      'google-auth==1.10.0', 'google-auth-httplib2==0.0.3', 'google-cloud-core==1.1.0',
                      'google-cloud-datastore==1.10.0', 'google-cloud-language==1.3.0', 'google-cloud-storage==1.23.0',
                      'google-cloud-videointelligence==1.12.1', 'google-cloud-vision==0.41.0', 'google-resumable-media==0.5.0',
                      'googleapis-common-protos==1.6.0', 'oauth2client==4.1.3', 'psycopg2==2.8.4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Ubuntu"
    ],
    include_package_data=True
)
