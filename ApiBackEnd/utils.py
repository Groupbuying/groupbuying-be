import json
from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Union

from django.http import JsonResponse


def serialize_json_fallback(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')


@dataclass
class Envelope:
    status: int
    data: Union[dict, list, None]
    msg: Union[str, None]

    def to_res(self):
        if self.data:
            # this is for as_dict serialization
            # removes redundant serializer instance from drf ordered dict
            # might have perf issue, but it's okay for now
            self.data = json.loads(json.dumps(self.data, default=serialize_json_fallback))
        # TODO(gogo): auto extract valid status for custom codes
        status = self.status if 100 <= self.status < 600 else 200
        return JsonResponse(asdict(self), status=status)
