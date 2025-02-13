"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Setup(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Setup"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the setup.",
            instructions="Enter a short text describing this setup.",
        ),
        Property(
            "has_parts",
            [
                "openminds.latest.core.Setup",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.ephys.Electrode",
                "openminds.latest.ephys.ElectrodeArray",
                "openminds.latest.ephys.Pipette",
                "openminds.latest.specimen_prep.SlicingDevice",
            ],
            "hasPart",
            multiple=True,
            unique_items=True,
            min_items=2,
            required=True,
            description="no description available",
            instructions="Add all components, including other setups, that are part of this setup. Note that a setup should not be only composed of software.",
        ),
        Property(
            "location",
            str,
            "location",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the geographic location of this setup. This may include room number, building, institution and/or city.",
        ),
        Property(
            "manufacturers",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "manufacturer",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the manufacturer (private or industrial) that constructed this setup.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the setup.",
            instructions="Enter a descriptive name for this setup.",
        ),
        Property(
            "types",
            "openminds.latest.controlled_terms.SetupType",
            "type",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add all types that describe this setup.",
        ),
    ]

    def __init__(
        self, id=None, description=None, has_parts=None, location=None, manufacturers=None, name=None, types=None
    ):
        return super().__init__(
            id=id,
            description=description,
            has_parts=has_parts,
            location=location,
            manufacturers=manufacturers,
            name=name,
            types=types,
        )
