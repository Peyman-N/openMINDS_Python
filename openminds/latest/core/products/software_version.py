"""
<description not available>
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SoftwareVersion(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/core/SoftwareVersion"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "accessibility",
            "openminds.latest.controlled_terms.ProductAccessibility",
            "vocab:accessibility",required=True,
            description="Level to which something is accessible to someone or something.",
            instructions="Add the accessibility of the data for this research product version."
        ),
        Property(
            "application_category",
            "openminds.latest.controlled_terms.SoftwareApplicationCategory",
            "vocab:applicationCategory",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Distinct class that groups software programs which perform a similar task or set of tasks.",
            instructions="Add all categories to which this software version belongs."
        ),
        Property(
            "copyright",
            "openminds.latest.core.Copyright",
            "vocab:copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version."
        ),
        Property(
            "custodian",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version."
        ),
        Property(
            "description",
            str,
            "vocab:description",formatting="text/markdown",
            multiline=True,
            
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset."
        ),
        Property(
            "developer",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add all parties that developed this software version. Note that these developers will overwrite the developer list provided for the overarching software."
        ),
        Property(
            "device",
            "openminds.latest.controlled_terms.OperatingDevice",
            "vocab:device",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add all operating devices compatible with this software version."
        ),
        Property(
            "digital_identifier",
            ['openminds.latest.core.DOI', 'openminds.latest.core.SWHID', 'openminds.latest.core.RRID'],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version."
        ),
        Property(
            "feature",
            "openminds.latest.controlled_terms.SoftwareFeature",
            "vocab:feature",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Structure, form, or appearance that characterizes something or someone.",
            instructions="Add all distinguishing characteristics of this software version (e.g., performance, portability or functionality)."
        ),
        Property(
            "full_documentation",
            ['openminds.latest.core.DOI', 'openminds.latest.core.File', 'openminds.latest.core.WebResource'],
            "vocab:fullDocumentation",required=True,
            description="Non-abridged instructions, comments, and information for using a particular product.",
            instructions="Add the publication or file that acts as the full documentation of this research product version."
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",formatting="text/plain",
            
            
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset."
        ),
        Property(
            "funding",
            "openminds.latest.core.Funding",
            "vocab:funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this research product version."
        ),
        Property(
            "has_part",
            "openminds.latest.core.SoftwareVersion",
            "vocab:hasPart",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all software versions that supplement this software version."
        ),
        Property(
            "homepage",
            IRI,
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version."
        ),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",formatting="text/markdown",
            multiline=True,
            
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier."
        ),
        Property(
            "input_format",
            "openminds.latest.core.ContentType",
            "vocab:inputFormat",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Format of data that is put into a process or machine.",
            instructions="Add all content types that can be used as input by this software version."
        ),
        Property(
            "is_alternative_version_of",
            "openminds.latest.core.SoftwareVersion",
            "vocab:isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all software versions that can be used alternatively to this software version."
        ),
        Property(
            "is_new_version_of",
            "openminds.latest.core.SoftwareVersion",
            "vocab:isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the software version preceding this software version."
        ),
        Property(
            "keyword",
            ['openminds.latest.controlled_terms.ActionStatusType', 'openminds.latest.controlled_terms.AgeCategory', 'openminds.latest.controlled_terms.AnalysisTechnique', 'openminds.latest.controlled_terms.AnatomicalAxesOrientation', 'openminds.latest.controlled_terms.AnatomicalIdentificationType', 'openminds.latest.controlled_terms.AnatomicalPlane', 'openminds.latest.controlled_terms.AnnotationCriteriaType', 'openminds.latest.controlled_terms.AnnotationType', 'openminds.latest.controlled_terms.AtlasType', 'openminds.latest.controlled_terms.AuditoryStimulusType', 'openminds.latest.controlled_terms.BiologicalOrder', 'openminds.latest.controlled_terms.BiologicalProcess', 'openminds.latest.controlled_terms.BiologicalSex', 'openminds.latest.controlled_terms.BreedingType', 'openminds.latest.controlled_terms.CellCultureType', 'openminds.latest.controlled_terms.CellType', 'openminds.latest.controlled_terms.ChemicalMixtureType', 'openminds.latest.controlled_terms.Colormap', 'openminds.latest.controlled_terms.ContributionType', 'openminds.latest.controlled_terms.CranialWindowConstructionType', 'openminds.latest.controlled_terms.CranialWindowReinforcementType', 'openminds.latest.controlled_terms.CriteriaQualityType', 'openminds.latest.controlled_terms.DataType', 'openminds.latest.controlled_terms.DeviceType', 'openminds.latest.controlled_terms.DifferenceMeasure', 'openminds.latest.controlled_terms.Disease', 'openminds.latest.controlled_terms.DiseaseModel', 'openminds.latest.controlled_terms.EducationalLevel', 'openminds.latest.controlled_terms.ElectricalStimulusType', 'openminds.latest.controlled_terms.EthicsAssessment', 'openminds.latest.controlled_terms.ExperimentalApproach', 'openminds.latest.controlled_terms.FileBundleGrouping', 'openminds.latest.controlled_terms.FileRepositoryType', 'openminds.latest.controlled_terms.FileUsageRole', 'openminds.latest.controlled_terms.GeneticStrainType', 'openminds.latest.controlled_terms.GustatoryStimulusType', 'openminds.latest.controlled_terms.Handedness', 'openminds.latest.controlled_terms.Language', 'openminds.latest.controlled_terms.Laterality', 'openminds.latest.controlled_terms.LearningResourceType', 'openminds.latest.controlled_terms.MeasuredQuantity', 'openminds.latest.controlled_terms.MeasuredSignalType', 'openminds.latest.controlled_terms.MetaDataModelType', 'openminds.latest.controlled_terms.ModelAbstractionLevel', 'openminds.latest.controlled_terms.ModelScope', 'openminds.latest.controlled_terms.MolecularEntity', 'openminds.latest.controlled_terms.OlfactoryStimulusType', 'openminds.latest.controlled_terms.OperatingDevice', 'openminds.latest.controlled_terms.OperatingSystem', 'openminds.latest.controlled_terms.OpticalStimulusType', 'openminds.latest.controlled_terms.Organ', 'openminds.latest.controlled_terms.OrganismSubstance', 'openminds.latest.controlled_terms.OrganismSystem', 'openminds.latest.controlled_terms.PatchClampVariation', 'openminds.latest.controlled_terms.PreparationType', 'openminds.latest.controlled_terms.ProductAccessibility', 'openminds.latest.controlled_terms.ProgrammingLanguage', 'openminds.latest.controlled_terms.QualitativeOverlap', 'openminds.latest.controlled_terms.SemanticDataType', 'openminds.latest.controlled_terms.Service', 'openminds.latest.controlled_terms.SetupType', 'openminds.latest.controlled_terms.SoftwareApplicationCategory', 'openminds.latest.controlled_terms.SoftwareFeature', 'openminds.latest.controlled_terms.Species', 'openminds.latest.controlled_terms.StimulationApproach', 'openminds.latest.controlled_terms.StimulationTechnique', 'openminds.latest.controlled_terms.SubcellularEntity', 'openminds.latest.controlled_terms.SubjectAttribute', 'openminds.latest.controlled_terms.TactileStimulusType', 'openminds.latest.controlled_terms.Technique', 'openminds.latest.controlled_terms.TermSuggestion', 'openminds.latest.controlled_terms.Terminology', 'openminds.latest.controlled_terms.TissueSampleAttribute', 'openminds.latest.controlled_terms.TissueSampleType', 'openminds.latest.controlled_terms.TypeOfUncertainty', 'openminds.latest.controlled_terms.UBERONParcellation', 'openminds.latest.controlled_terms.UnitOfMeasurement', 'openminds.latest.controlled_terms.VisualStimulusType'],
            "vocab:keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Significant word or concept that are representative of something or someone.",
            instructions="Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms."
        ),
        Property(
            "language",
            "openminds.latest.controlled_terms.Language",
            "vocab:language",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="System of communication (words, their pronunciation, and the methods of combining them) used and understood by a particular community.",
            instructions="Add all languages supported by this software version."
        ),
        Property(
            "license",
            "openminds.latest.core.License",
            "vocab:license",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add all licenses of this software version."
        ),
        Property(
            "operating_system",
            "openminds.latest.controlled_terms.OperatingSystem",
            "vocab:operatingSystem",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Software that controls the operation of a computer and directs the processing of programs.",
            instructions="Add all operating systems supported by this software version."
        ),
        Property(
            "other_contribution",
            "openminds.latest.core.Contribution",
            "vocab:otherContribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
            instructions="Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'."
        ),
        Property(
            "output_format",
            "openminds.latest.core.ContentType",
            "vocab:outputFormat",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Format of data that comes out of, is delivered or produced by a process or machine.",
            instructions="Add all content types that can be generated as output by this software version."
        ),
        Property(
            "programming_language",
            "openminds.latest.controlled_terms.ProgrammingLanguage",
            "vocab:programmingLanguage",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Distinct set of instructions for computer programs in order to produce various kinds of output.",
            instructions="Add all programming languages used to develop this software version."
        ),
        Property(
            "related_publication",
            ['openminds.latest.core.DOI', 'openminds.latest.core.HANDLE', 'openminds.latest.core.ISBN', 'openminds.latest.core.ISSN', 'openminds.latest.publications.Book', 'openminds.latest.publications.Chapter', 'openminds.latest.publications.ScholarlyArticle'],
            "vocab:relatedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Reference to something that was made available for the general public to see or buy.",
            instructions="Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version)."
        ),
        Property(
            "release_date",
            date,
            "vocab:releaseDate",required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'."
        ),
        Property(
            "repository",
            "openminds.latest.core.FileRepository",
            "vocab:repository",
            description="Place, room, or container where something is deposited or stored.",
            instructions="Add the file repository of this research product version."
        ),
        Property(
            "requirement",
            str,
            "vocab:requirement",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            formatting="text/plain",
            
            
            description="Something essential to the existence, occurrence or function of something else.",
            instructions="Enter all requirements of this software version."
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name)."
        ),
        Property(
            "support_channel",
            str,
            "vocab:supportChannel",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            formatting="text/plain",
            
            
            description="Way of communication used to interact with users or customers.",
            instructions="Enter all channels through which a user can receive support for handling this research product version."
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",formatting="text/plain",
            
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this research product version."
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'."
        ),
        
    ]

    def __init__(self, id=None, accessibility=None, application_category=None, copyright=None, custodian=None, description=None, developer=None, device=None, digital_identifier=None, feature=None, full_documentation=None, full_name=None, funding=None, has_part=None, homepage=None, how_to_cite=None, input_format=None, is_alternative_version_of=None, is_new_version_of=None, keyword=None, language=None, license=None, operating_system=None, other_contribution=None, output_format=None, programming_language=None, related_publication=None, release_date=None, repository=None, requirement=None, short_name=None, support_channel=None, version_identifier=None, version_innovation=None):
        return super().__init__(id=id,accessibility=accessibility,application_category=application_category,copyright=copyright,custodian=custodian,description=description,developer=developer,device=device,digital_identifier=digital_identifier,feature=feature,full_documentation=full_documentation,full_name=full_name,funding=funding,has_part=has_part,homepage=homepage,how_to_cite=how_to_cite,input_format=input_format,is_alternative_version_of=is_alternative_version_of,is_new_version_of=is_new_version_of,keyword=keyword,language=language,license=license,operating_system=operating_system,other_contribution=other_contribution,output_format=output_format,programming_language=programming_language,related_publication=related_publication,release_date=release_date,repository=repository,requirement=requirement,short_name=short_name,support_channel=support_channel,version_identifier=version_identifier,version_innovation=version_innovation,)
