"""
Structured information on data originating from human/animal studies or simulations (version level).
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class DatasetVersion(LinkedMetadata):
    """
    Structured information on data originating from human/animal studies or simulations (version level).
    """
    type_ = ["https://openminds.ebrains.eu/core/DatasetVersion"]
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
            "author",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:author",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this dataset version as authors. Note that these authors will overwrite the author list provided for the overarching dataset."
        ),
        Property(
            "behavioral_protocol",
            "openminds.latest.core.BehavioralProtocol",
            "vocab:behavioralProtocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all behavioral protocols that were performed in this dataset version."
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
            "data_type",
            "openminds.latest.controlled_terms.SemanticDataType",
            "vocab:dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="no description available",
            instructions="Add all semantic data types (raw, derived and/or simulated) provided in this dataset version."
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
            "digital_identifier",
            ['openminds.latest.core.DOI', 'openminds.latest.core.IdentifiersDotOrgID'],
            "vocab:digitalIdentifier",required=True,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version."
        ),
        Property(
            "ethics_assessment",
            "openminds.latest.controlled_terms.EthicsAssessment",
            "vocab:ethicsAssessment",required=True,
            description="Judgment about the applied principles of conduct governing an individual or a group.",
            instructions="Add the result of the ethics assessment of this dataset version."
        ),
        Property(
            "experimental_approach",
            "openminds.latest.controlled_terms.ExperimentalApproach",
            "vocab:experimentalApproach",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="no description available",
            instructions="Add all experimental approaches which this dataset version has deployed."
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
            "input_data",
            ['openminds.latest.core.DOI', 'openminds.latest.core.File', 'openminds.latest.core.FileBundle', 'openminds.latest.core.WebResource', 'openminds.latest.sands.BrainAtlas', 'openminds.latest.sands.BrainAtlasVersion', 'openminds.latest.sands.CommonCoordinateSpace', 'openminds.latest.sands.CommonCoordinateSpaceVersion'],
            "vocab:inputData",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Data that is put into a process or machine.",
            instructions="Add the data that was used as input for this dataset version."
        ),
        Property(
            "is_alternative_version_of",
            "openminds.latest.core.DatasetVersion",
            "vocab:isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all dataset versions that can be used alternatively to this dataset version."
        ),
        Property(
            "is_new_version_of",
            "openminds.latest.core.DatasetVersion",
            "vocab:isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the dataset version preceding this dataset version."
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
            "license",
            ['openminds.latest.core.License', 'openminds.latest.core.WebResource'],
            "vocab:license",required=True,
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license or an online available data usage agreement for this dataset version."
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
            "preparation_design",
            "openminds.latest.controlled_terms.PreparationType",
            "vocab:preparationDesign",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all preparation types used in this dataset version."
        ),
        Property(
            "protocol",
            "openminds.latest.core.Protocol",
            "vocab:protocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Plan that describes the process of a scientific or medical experiment, treatment, or procedure.",
            instructions="Add all protocols that were performed in this dataset version (e.g., for data acquisition or processing)."
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
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name)."
        ),
        Property(
            "studied_specimen",
            ['openminds.latest.core.Subject', 'openminds.latest.core.SubjectGroup', 'openminds.latest.core.TissueSample', 'openminds.latest.core.TissueSampleCollection'],
            "vocab:studiedSpecimen",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all specimens or sets of specimen that were studied in this dataset."
        ),
        Property(
            "study_target",
            ['openminds.latest.controlled_terms.AuditoryStimulusType', 'openminds.latest.controlled_terms.BiologicalOrder', 'openminds.latest.controlled_terms.BiologicalSex', 'openminds.latest.controlled_terms.BreedingType', 'openminds.latest.controlled_terms.CellCultureType', 'openminds.latest.controlled_terms.CellType', 'openminds.latest.controlled_terms.Disease', 'openminds.latest.controlled_terms.DiseaseModel', 'openminds.latest.controlled_terms.ElectricalStimulusType', 'openminds.latest.controlled_terms.GeneticStrainType', 'openminds.latest.controlled_terms.GustatoryStimulusType', 'openminds.latest.controlled_terms.Handedness', 'openminds.latest.controlled_terms.MolecularEntity', 'openminds.latest.controlled_terms.OlfactoryStimulusType', 'openminds.latest.controlled_terms.OpticalStimulusType', 'openminds.latest.controlled_terms.Organ', 'openminds.latest.controlled_terms.OrganismSubstance', 'openminds.latest.controlled_terms.OrganismSystem', 'openminds.latest.controlled_terms.Species', 'openminds.latest.controlled_terms.SubcellularEntity', 'openminds.latest.controlled_terms.TactileStimulusType', 'openminds.latest.controlled_terms.TermSuggestion', 'openminds.latest.controlled_terms.UBERONParcellation', 'openminds.latest.controlled_terms.VisualStimulusType', 'openminds.latest.sands.CustomAnatomicalEntity', 'openminds.latest.sands.ParcellationEntity', 'openminds.latest.sands.ParcellationEntityVersion'],
            "vocab:studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this dataset version."
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
            "technique",
            ['openminds.latest.controlled_terms.AnalysisTechnique', 'openminds.latest.controlled_terms.StimulationApproach', 'openminds.latest.controlled_terms.StimulationTechnique', 'openminds.latest.controlled_terms.Technique'],
            "vocab:technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Method of accomplishing a desired aim.",
            instructions="Add all techniques that were used in this dataset version."
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

    def __init__(self, id=None, accessibility=None, author=None, behavioral_protocol=None, copyright=None, custodian=None, data_type=None, description=None, digital_identifier=None, ethics_assessment=None, experimental_approach=None, full_documentation=None, full_name=None, funding=None, homepage=None, how_to_cite=None, input_data=None, is_alternative_version_of=None, is_new_version_of=None, keyword=None, license=None, other_contribution=None, preparation_design=None, protocol=None, related_publication=None, release_date=None, repository=None, short_name=None, studied_specimen=None, study_target=None, support_channel=None, technique=None, version_identifier=None, version_innovation=None):
        return super().__init__(id=id,accessibility=accessibility,author=author,behavioral_protocol=behavioral_protocol,copyright=copyright,custodian=custodian,data_type=data_type,description=description,digital_identifier=digital_identifier,ethics_assessment=ethics_assessment,experimental_approach=experimental_approach,full_documentation=full_documentation,full_name=full_name,funding=funding,homepage=homepage,how_to_cite=how_to_cite,input_data=input_data,is_alternative_version_of=is_alternative_version_of,is_new_version_of=is_new_version_of,keyword=keyword,license=license,other_contribution=other_contribution,preparation_design=preparation_design,protocol=protocol,related_publication=related_publication,release_date=release_date,repository=repository,short_name=short_name,studied_specimen=studied_specimen,study_target=study_target,support_channel=support_channel,technique=technique,version_identifier=version_identifier,version_innovation=version_innovation,)
