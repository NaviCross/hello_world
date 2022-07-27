import json
from typing import Optional


def data_serializer(data: Optional[dict]) -> str:
    """In the Fact it will not work safe and predictable.
        We can't guarantee all entities are serializable
    """
    if data is None:
        data = {}
    # TODO: create more complex serialization obj
    return json.dumps(data)
