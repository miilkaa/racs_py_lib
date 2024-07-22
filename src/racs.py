import requests
import json


class Racs:
    def __init__(
            self,
            resource: str | None = None,
            dataset: str | None = None
    ):
        self.resource = resource
        self.dataset = dataset
        self.headers = {'Content-Type': 'application/json'}
        self.base_url = "https://racs.rest/v3"

        if not self.resource:
            raise ValueError("resource can't be None")

        if not self.dataset:
            raise ValueError("dataset can't be None")

    def create_post(
            self,
            data: dict | None = None
    ):
        if not data:
            raise ValueError('Argument "data" is required')
        url: str = f"{self.base_url}?resource={self.resource}&dataset={self.dataset}"
        payload = json.dumps(data)

        return requests.post(url, headers=self.headers, data=payload).json()

    def create_file(
            self,
            file_path: str | None = None
    ):
        if not file_path:
            raise ValueError('Argument "file_path" is required')

        url: str = f"{self.base_url}?resource={self.resource}&dataset={self.dataset}"
        headers = {"Content-Type": "application/json"}

        with open(file_path, 'rb') as file:
            files = {'file': file}
            req = requests.post(url, files=files, headers=headers)

        return req.json()

    def read_post_by_id(
            self,
            post_id: str | None = None
    ):
        if not post_id:
            raise ValueError('Argument "post_id" is required')

        url: str = f"{self.base_url}/{post_id}"

        return requests.get(url=url, headers=self.headers).json()

    def read_post_by_filter(
            self,
            filter_data: dict | None = None,
            sort: int | None = -1,
            limit: int | None = 1
    ):

        if not filter_data:
            raise ValueError('Argument "data" is required')

        url: str = f"{self.base_url}/get?resource={self.resource}&dataset={self.dataset}"
        payload = json.dumps({
            "filter": filter_data,
            "sort": sort,
            "limit": limit
        })

        return requests.post(url=url, headers=self.headers, data=payload)

    def read_file_by_id(
            self,
            post_id: str | None = None
    ):
        if not post_id:
            raise ValueError('Argument "post_id" is required')

        url: str = f"{self.base_url}/file/{post_id}"

        headers = {"Accept": "application/octet-stream"}

        return requests.get(url, headers).json()
