from ML_APIs.utils import *


class video_classifier_local:

    def __init__(self, path, model, credentials):
        self.path = path
        self.model = model
        self.credentials = credentials

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{self.credentials}"

        with io.open(self.path, 'rb') as movie:
            input_content = movie.read()

        label_client = videointelligence.VideoIntelligenceServiceClient()
        logo_client = videointelligence_v1p3beta1.VideoIntelligenceServiceClient()

        if self.model == 'labels':

            """ Detects labels given a context. """

            features = [videointelligence.enums.Feature.LABEL_DETECTION]

            operation = label_client.annotate_video(
                features=features, input_content=input_content)
            print('\nProcessing video for label annotations:')

            result = operation.result(timeout=90)
            print('\nFinished processing.')

            # Process video/segment level label annotations
            segment_labels = result.annotation_results[0].segment_label_annotations

            # Process shot level label annotations
            shot_labels = result.annotation_results[0].shot_label_annotations

            # Process frame level label annotations
            frame_labels = result.annotation_results[0].frame_label_annotations

            segment_labels_df = pd.DataFrame(
                columns=["media", "media_type", "description", "category", "start_time", "end_time", "confidence"])

            for label in segment_labels:
                segment_labels_df = segment_labels_df.append(
                    dict(
                        media=self.path,
                        media_type='video',
                        description=label.entity.description,
                        category=[
                            cat.description for cat in label.category_entities],
                        start_time=[(seg.segment.start_time_offset.seconds +
                                     seg.segment.start_time_offset.nanos / 1e9) for seg in label.segments],
                        end_time=[(seg.segment.end_time_offset.seconds +
                                   seg.segment.end_time_offset.nanos / 1e9) for seg in label.segments],
                        confidence=[con.confidence for con in label.segments]
                    ), ignore_index=True
                )

            self.analyze_segment_labels = segment_labels_df

            shot_labels_df = pd.DataFrame(
                columns=["media", "media_type", "description", "category", "start_time", "end_time", "confidence"])

            for label in shot_labels:
                shot_labels_df = shot_labels_df.append(
                    dict(
                        media=self.path,
                        media_type='video',
                        description=label.entity.description,
                        category=[
                            cat.description for cat in label.category_entities],
                        start_time=[(seg.segment.start_time_offset.seconds +
                                     seg.segment.start_time_offset.nanos / 1e9) for seg in label.segments],
                        end_time=[(seg.segment.end_time_offset.seconds +
                                   seg.segment.end_time_offset.nanos / 1e9) for seg in label.segments],
                        confidence=[con.confidence for con in label.segments]
                    ), ignore_index=True
                )

            self.analyze_shot_labels = shot_labels_df

            # Each frame_label_annotation has many frames, SO NOT added

        elif self.model == 'logos':
            """ Detects logo given a GCS uri. """

            features = [
                videointelligence_v1p3beta1.enums.Feature.LOGO_RECOGNITION]

            operation = logo_client.annotate_video(
                input_content=input_content, features=features)
            print('\nProcessing video for logo recognition:')

            print(u'Waiting for operation to complete...')
            response = operation.result()

            # Get the first response, since we sent only one video.
            annotation_result = response.annotation_results[0]

            logos_df = pd.DataFrame(columns=[
                                    "media", "media_type", "description", "start_time", "end_time", "confidence", "left", "right", "top", "bottom"])

            for logo_recognition_annotation in annotation_result.logo_recognition_annotations:
                logos_df = logos_df.append(
                    dict(
                        media=self.path,
                        media_type='video',
                        description=logo_recognition_annotation.entity.description,
                        start_time=[(track.segment.start_time_offset.seconds +
                                     track.segment.start_time_offset.nanos / 1e9) for track in logo_recognition_annotation.tracks],
                        end_time=[(track.segment.end_time_offset.seconds +
                                   track.segment.end_time_offset.nanos / 1e9) for track in logo_recognition_annotation.tracks],
                        confidence=[
                            track.confidence for track in logo_recognition_annotation.tracks],
                        left=[
                            timestamped_object.normalized_bounding_box.left for track in logo_recognition_annotation.tracks for timestamped_object in track.timestamped_objects],
                        top=[timestamped_object.normalized_bounding_box.top for track in logo_recognition_annotation.tracks for timestamped_object in track.timestamped_objects],
                        right=[
                            timestamped_object.normalized_bounding_box.right for track in logo_recognition_annotation.tracks for timestamped_object in track.timestamped_objects],
                        bottom=[
                            timestamped_object.normalized_bounding_box.bottom for track in logo_recognition_annotation.tracks for timestamped_object in track.timestamped_objects]
                    ), ignore_index=True
                )

            self.logos = logos_df

        else:
            print(
                "Couldn't find the model. Are you sure it's in the below following" + "\n\n" +
                "1. labels" + "\n" +
                "2. logos"
            )
