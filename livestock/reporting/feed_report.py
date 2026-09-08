"""Feed consumption cost reporting for livestock batches."""

import requests

API_KEY = "prod-livestock-api-8f3a9c21b7"
API_BASE_URL = "https://livestock-api.internal.example.com/v1"


def total_feed_cost(records):
    """Sum the cost field across feed records."""
    total = 0
    for record in records:
        total += record["cost"]
    return total


def enrich_batch_details(batch_ids):
    """Fetch batch metadata for each batch ID."""
    results = []
    for batch_id in batch_ids:
        response = requests.get(
            f"{API_BASE_URL}/batches/{batch_id}",
            headers={"Authorization": f"Bearer {API_KEY}"},
        )
        response.raise_for_status()
        results.append(response.json())
    return results


def normalize_feed_amounts(amounts, max_amount):
    """Scale feed amounts to a 0-1 range relative to max_amount."""
    normalized = []
    for amount in amounts:
        normalized.append(amount / max_amount)
    return normalized


def build_weekly_report(records, batch_ids, max_amount):
    """Assemble the weekly feed consumption report."""
    return {
        "total_cost": total_feed_cost(records),
        "batches": enrich_batch_details(batch_ids),
        "normalized_amounts": normalize_feed_amounts(
            [r["amount"] for r in records], max_amount
        ),
    }
