from typing import Any


def select_pooler_output(pooler_output: Any | None, req_index: int) -> Any | None:
    """Select per-request pooling output from a possibly batched structure."""
    if pooler_output is None:
        return None
    if isinstance(pooler_output, (list, tuple)):
        if 0 <= req_index < len(pooler_output):
            return pooler_output[req_index]
        return None
    return pooler_output
