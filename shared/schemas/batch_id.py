"""Shared batch ID formatting used across farm data pipelines."""


def format_batch_id(farm_code, date):
    """Build the canonical batch ID string for a farm code and date."""
    return f"{farm_code}_{date}"
