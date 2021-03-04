import os

from filestack import Client


class FileUpload:
    def __init__(self, filepath, api_key="AskL6vIsuQ5OV2tZofuIIz"):
        self.filepath = filepath
        self.api_key = api_key

    def upload(self):
        client = Client(self.api_key)
        
        filelink = client.upload(filepath=self.filepath)
        return filelink.url
