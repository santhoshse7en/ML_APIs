### ML_APIs
A simple python package to get ease use of Google ML APIs

### Quick Start
**In order to use this library, you first need to go through the following steps:**

1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)
2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
3. [Enable the Google Cloud Vision API.](https://cloud.google.com/vision)
4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)

## Installation
Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

### Supported Python Versions
Python >= 3.5

### Deprecated Python Versions
Python == 2.7. Python 2.7 support will be removed on January 1, 2020.

#### Windows 
```console
se7en@bar:~$ pip install virtualenv
se7en@bar:~$ virtualenv <your-env>
se7en@bar:~$ <your-env>\Scripts\activate
(<your-env>)se7en@bar:~$ 
```

The easiest way to install the latest stable version of Airflow is with pip:
```console
(<your-env>)se7en@bar:~$ pip install ML_APIs
```
### Example Usage Google Vision A.I. on local media file
```python3
  from ML_APIs.google import vision_ai_local
  
  path = <your-image>
  model = 'logos'
  credentials = <your-credentials.json>
  
  image_classification = vision_ai_local(path, model, credentials)
  image_classification.logos
```
### Next Steps
Read the Product documentation to learn more about the product and see How-to Guides.
