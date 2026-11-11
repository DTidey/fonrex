"""The ISIN field of a Yahoo answer, read once for the enrichment and the profile write.

Yahoo writes a placeholder (``-``, ``N/A``…) in the ISIN field of an instrument
it has no ISIN for. Taken as an ISIN, it would differ from the ISIN of the asset
and refuse the profile of the right instrument. No dependency: imported by the
enrichment (``financials/enrichment/yfinance_enricher.py``), the import
(``import_assets.py``) and the profile write (``database/assets.py``).
"""

# What Yahoo writes in an ISIN field when it has none.
_NO_ISIN = ("-", "N/A", "NA", "NONE", "NULL")


def clean_yahoo_isin(value) -> str | None:
    """An ISIN given by Yahoo, upper case; ``None`` for an empty field or a placeholder."""
    if not isinstance(value, str):
        return None
    normalized = value.strip().upper()
    return normalized if normalized and normalized not in _NO_ISIN else None
