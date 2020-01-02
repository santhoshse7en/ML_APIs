from ML_APIs.utils import *


class vision_classifier_cloud:

    def __init__(self, uri, model, credentials):
        self.uri = uri
        self.model = model
        self.credentials = credentials

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{self.credentials}"

        client = vision.ImageAnnotatorClient()

        self.image = vision.types.Image()
        self.image.source.image_uri = self.uri

        if self.model == 'labels':

            """Detects labels in the file."""
            response = client.label_detection(image=self.image)
            labels = response.label_annotations

            df = pd.DataFrame(
                columns=["media", "media_type", "description", "score", "topicality"])

            for label in labels:
                df = df.append(
                    dict(
                        media=self.uri,
                        media_type='photo',
                        description=label.description,
                        score=label.score,
                        topicality=label.topicality
                    ), ignore_index=True
                )
            self.labels = df

        elif self.model == 'logos':
            """Detects logos in the file."""
            response = client.logo_detection(image=self.image)
            logos = response.logo_annotations

            df = pd.DataFrame(
                columns=["media", "media_type", "description", "score", "bounding_poly"])

            for logo in logos:
                df = df.append(
                    dict(
                        media=self.uri,
                        media_type='photo',
                        file=self.uri,
                        description=logo.description,
                        score=logo.score,
                        bounding_poly=logo.bounding_poly
                    ), ignore_index=True
                )

            self.logos = df

        elif self.model == 'objects':
            """Detects logos in the file."""
            response = client.logo_detection(image=self.image)
            logos = response.logo_annotations

            df = pd.DataFrame(
                columns=["media", "media_type", "description", "score", "bounding_poly"])

            for logo in logos:
                df = df.append(
                    dict(
                        media=self.uri,
                        media_type='photo',
                        description=logo.description,
                        score=logo.score,
                        bounding_poly=logo.bounding_poly
                    ), ignore_index=True
                )

            self.localize_objects = df

        elif self.model == 'landmarks':

            """Detects landmarks in the file."""

            response = client.landmark_detection(image=self.image)
            landmarks = response.landmark_annotations

            df = pd.DataFrame(
                columns=["media", "media_type", "description", "score", "bounding_poly", "locations"])

            for landmark in landmarks:
                df = df.append(
                    dict(
                        media=self.uri,
                        media_type='photo',
                        description=landmark.description,
                        score=landmark.score,
                        bounding_poly=landmark.bounding_poly,
                        locations=landmark.locations
                    ), ignore_index=True
                )

            self.landmarks = df

        elif self.model == 'faces':

            """Detects faces in an image."""

            response = client.face_detection(image=self.image)
            faces = response.face_annotations

            # Names of likelihood from google.cloud.vision.enums
            likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                               'LIKELY', 'VERY_LIKELY')

            df = pd.DataFrame(columns=["media", "media_type", "bounding_poly", "joy", "sorrow",
                                       "anger", "surprise", "under_exposed", "blurred", "headwear"])

            for face in faces:
                df = df.append(
                    dict(
                        media=self.uri,
                        media_type='photo',
                        bounding_poly=face.bounding_poly,
                        joy=likelihood_name[face.joy_likelihood],
                        sorrow=likelihood_name[face.sorrow_likelihood],
                        anger=likelihood_name[face.anger_likelihood],
                        surprise=likelihood_name[face.surprise_likelihood],
                        under_exposed=likelihood_name[face.under_exposed_likelihood],
                        blurred=likelihood_name[face.blurred_likelihood],
                        headwear=likelihood_name[face.headwear_likelihood]
                    ), ignore_index=True
                )

            self.faces = df
        else:
            print(
                "Couldn't find the model. Are you sure it's in the below following" + "\n\n" +
                "1. labels" + "\n" +
                "2. logos" + "\n" +
                "3. objects" + "\n" +
                "4. landmarks" + "\n" +
                "5. faces"
            )
