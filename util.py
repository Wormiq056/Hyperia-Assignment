import dataclasses
import json


def write_to_json(job_dataclasses: list):
    """
    function that writes given JobData objects into a JSON file
    :param job_dataclasses: list of JobData objects
    """
    with open("json_data.json", "w", encoding='utf-8') as file:
        dict_list = []
        for job_dataclass in job_dataclasses:
            dict_list.append(dataclasses.asdict(job_dataclass))
        file.write(json.dumps(dict_list, indent=5, ensure_ascii=False))
