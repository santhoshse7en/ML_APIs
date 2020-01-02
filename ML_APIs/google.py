from .utils import *

# Prediction on Local file
from ML_APIs.local.vision_local import vision_classifier_local
from ML_APIs.local.video_local import video_classifier_local
from ML_APIs.local.nlp_local import nlp_classifier_local


# Prediction on Cloud Storage
from ML_APIs.cloud.vision_cloud import vision_classifier_cloud
from ML_APIs.cloud.video_cloud import video_classifier_cloud
from ML_APIs.cloud.nlp_cloud import nlp_classifier_cloud

# main class which passes the path, model, credentials to each individual class
class vision_ai_local:
    def __init__(self, path, model, credentials):
        vision_classifier_local.__init__(self, path, model, credentials)

class video_ai_local:
    def __init__(self, path, model, credentials):
        video_classifier_local.__init__(self, path, model, credentials)

# main class which passes the text_content, model, credentials to each individual class
class nlp_ai_local:
    def __init__(self, text_content, model, credentials):
        nlp_classifier_local.__init__(self, text_content, model, credentials)


# main class which passes the uri, model, credentials to each individual class
class vision_ai_cloud:
    def __init__(self, uri, model, credentials):
        vision_classifier_cloud.__init__(self, uri, model, credentials)

class video_ai_cloud:
    def __init__(self, uri, model, credentials):
        video_classifier_cloud.__init__(self, uri, model, credentials)

# main class which passes the text_content_uri, model, credentials to each individual class
class nlp_ai_cloud:
    def __init__(self, text_content_uri, model, credentials):
        nlp_classifier_cloud.__init__(self, text_content_uri, model, credentials)