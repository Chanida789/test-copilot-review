"""Per-species alert thresholds for water quality monitoring."""

_THRESHOLDS = {
    "tilapia": {
        "dissolved_oxygen": 3.5,
    },
    "shrimp": {
        "salinity": 15.0,
    },
}


def get_alert_threshold(species, param):
    """Return the configured alert threshold for a species/parameter pair.

    Falls back to 0.0 when no threshold is configured for the given
    species or parameter.
    """
    return _THRESHOLDS.get(species, {}).get(param, 0.0)
