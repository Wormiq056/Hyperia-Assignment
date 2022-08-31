import dataclasses
import json


class JsonWriter:
    def __init__(self, job_dataclasses):
        with open("json_data.json", "w", encoding='utf-8') as file:
            dict_list = []
            for job_dataclass in job_dataclasses:
                dict_list.append(dataclasses.asdict(job_dataclass))
            file.write(json.dumps(dict_list, indent=5, ensure_ascii=False))
