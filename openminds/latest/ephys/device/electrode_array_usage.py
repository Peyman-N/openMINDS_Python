"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeArrayUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ElectrodeArrayUsage"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "anatomical_locations_of_arrays",
            [
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.sands.CustomAnatomicalEntity",
                "openminds.latest.sands.ParcellationEntity",
                "openminds.latest.sands.ParcellationEntityVersion",
            ],
            "anatomicalLocationOfArray",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all anatomical entities that semantically best describe the overall anatomical location of the electrode array.",
        ),
        Property(
            "anatomical_locations_of_electrodes",
            [
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.sands.CustomAnatomicalEntity",
                "openminds.latest.sands.ParcellationEntity",
                "openminds.latest.sands.ParcellationEntityVersion",
            ],
            "anatomicalLocationOfElectrodes",
            multiple=True,
            unique_items=True,
            min_items=2,
            description="no description available",
            instructions="Add all anatomical entities that semantically best describe the anatomical location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.",
        ),
        Property(
            "contact_resistances",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "contactResistances",
            multiple=True,
            unique_items=True,
            min_items=2,
            description="no description available",
            instructions="Enter the contact resistance for each electrode of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.",
        ),
        Property(
            "device",
            "openminds.latest.ephys.ElectrodeArray",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the electrode array used.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device usage that may help you to find this instance more easily.",
        ),
        Property(
            "metadata_locations",
            ["openminds.latest.core.File", "openminds.latest.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "spatial_locations_of_electrodes",
            "openminds.latest.sands.CoordinatePoint",
            "spatialLocationOfElectrodes",
            multiple=True,
            unique_items=True,
            min_items=2,
            description="no description available",
            instructions="Add all coordinate points that best describe the spatial location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.",
        ),
        Property(
            "used_electrodes",
            str,
            "usedElectrode",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter the identifiers of all electrodes that are actually in use for this array.",
        ),
        Property(
            "used_specimen",
            ["openminds.latest.core.SubjectState", "openminds.latest.core.TissueSampleState"],
            "usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_locations_of_arrays=None,
        anatomical_locations_of_electrodes=None,
        contact_resistances=None,
        device=None,
        lookup_label=None,
        metadata_locations=None,
        spatial_locations_of_electrodes=None,
        used_electrodes=None,
        used_specimen=None,
    ):
        return super().__init__(
            id=id,
            anatomical_locations_of_arrays=anatomical_locations_of_arrays,
            anatomical_locations_of_electrodes=anatomical_locations_of_electrodes,
            contact_resistances=contact_resistances,
            device=device,
            lookup_label=lookup_label,
            metadata_locations=metadata_locations,
            spatial_locations_of_electrodes=spatial_locations_of_electrodes,
            used_electrodes=used_electrodes,
            used_specimen=used_specimen,
        )
