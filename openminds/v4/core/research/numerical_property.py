"""
Structured information about a property of some entity or process whose value is a number.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class NumericalProperty(EmbeddedMetadata):
    """
    Structured information about a property of some entity or process whose value is a number.
    """

    type_ = "https://openminds.om-i.org/types/NumericalProperty"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the numerical property.",
            instructions="Enter a descriptive name for this numerical property.",
        ),
        Property(
            "values",
            ["openminds.v4.core.QuantitativeValue", "openminds.v4.core.QuantitativeValueRange"],
            "value",
            multiple=True,
            unique_items=False,
            min_items=1,
            required=True,
            description="Entry for a property.",
            instructions="Enter all quantitative values that are described by this numerical property.",
        ),
    ]

    def __init__(self, name=None, values=None):
        return super().__init__(
            name=name,
            values=values,
        )
