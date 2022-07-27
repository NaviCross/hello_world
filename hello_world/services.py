from typing import Optional


def get_hello_world_data() -> Optional[dict]:
    emulated_db_data = dict(
        hello="world"
    )
    hello_world_data = emulated_db_data or None
    return hello_world_data
