"""
Structured information about the source of a chemical substance or mixture.
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class ProductSource(LinkedMetadata):
    """
    Structured information about the source of a chemical substance or mixture.
    """
    type_ = ["https://openminds.ebrains.eu/chemicals/ProductSource"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "digital_identifier",
            "openminds.latest.core.RRID",
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this product."
        ),
        Property(
            "identifier",
            str,
            "vocab:identifier",formatting="text/plain",
            
            
            description="Term or code used to identify something or someone.",
            instructions="Enter the identifier for this product, excluding its RRID (e.g., a catalog number)."
        ),
        Property(
            "product_name",
            str,
            "vocab:productName",formatting="text/plain",
            
            required=True,
            description="no description available",
            instructions="Enter the name of this product as stated by the 'provider'."
        ),
        Property(
            "provider",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:provider",required=True,
            description="no description available",
            instructions="Add the party (private, commercial or industrial) that provided this product."
        ),
        Property(
            "purity",
            ['openminds.latest.core.QuantitativeValue', 'openminds.latest.core.QuantitativeValueRange'],
            "vocab:purity",
            description="no description available",
            instructions="Enter the purity of the product as stated by the 'provider'."
        ),
        
    ]

    def __init__(self, id=None, digital_identifier=None, identifier=None, product_name=None, provider=None, purity=None):
        return super().__init__(id=id,digital_identifier=digital_identifier,identifier=identifier,product_name=product_name,provider=provider,purity=purity,)
