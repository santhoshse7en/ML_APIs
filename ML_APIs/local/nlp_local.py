from ML_APIs.utils import *


class nlp_classifier_local:

    def __init__(self, text_content, model, credentials):

        self.text_content = text_content
        self.model = model
        self.credentials = credentials

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{self.credentials}"

        client = language_v1.LanguageServiceClient()

        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.enums.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": re.sub(
            r'\W+', ' ', self.text_content), "type": type_, "language": language}

        if self.model == 'entity':

            # Available values: NONE, UTF8, UTF16, UTF32
            encoding_type = language_v1.enums.EncodingType.UTF8
            response = client.analyze_entities(
                document, encoding_type=encoding_type)
            entities = response.entities

            df = pd.DataFrame(columns=[
                              "content", "entity_name", "entity_type", "entity_type_source_url", "mention", "mention_type"])

            for entity in entities:
                df = df.append(
                    dict(content=self.text_content,
                         entity_name=entity.name,
                         entity_type=language_v1.enums.Entity.Type(
                             entity.type).name,
                         entity_type_source_url=entity.metadata['wikipedia_url'],
                         mention=entity.mentions[0].text.content,
                         mention_type=language_v1.enums.EntityMention.Type(
                             entity.mentions[0].type).name
                         ), ignore_index=True
                )

            self.analyze_entities = df

        else:
            print(
                "Couldn't find the model. Are you sure it's in the below following" + "\n\n" +
                "1. entity"
            )
