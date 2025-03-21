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

    type_ = "https://openminds.om-i.org/types/DatasetVersion"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "accessibility",
            "openminds.v4.controlled_terms.ProductAccessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to the dataset version.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "authors",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this dataset version as authors. Note that these authors will overwrite the author list provided for the overarching dataset.",
        ),
        Property(
            "behavioral_protocols",
            "openminds.v4.core.BehavioralProtocol",
            "behavioralProtocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all behavioral protocols that were performed in this dataset version.",
        ),
        Property(
            "copyright",
            "openminds.v4.core.Copyright",
            "copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "custodians",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.",
        ),
        Property(
            "data_types",
            "openminds.v4.controlled_terms.SemanticDataType",
            "dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all semantic data types (raw, derived and/or simulated) provided in this dataset version.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the dataset version.",
            instructions="Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v4.core.DOI", "openminds.v4.core.IdentifiersDotOrgID"],
            "digitalIdentifier",
            required=True,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version.",
        ),
        Property(
            "ethics_assessment",
            "openminds.v4.controlled_terms.EthicsAssessment",
            "ethicsAssessment",
            required=True,
            description="Judgment about the applied principles of conduct governing an individual or a group.",
            instructions="Add the result of the ethics assessment of this dataset version.",
        ),
        Property(
            "experimental_approaches",
            "openminds.v4.controlled_terms.ExperimentalApproach",
            "experimentalApproach",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all experimental approaches which this dataset version has deployed.",
        ),
        Property(
            "full_documentation",
            [
                "openminds.v4.core.DOI",
                "openminds.v4.core.File",
                "openminds.v4.core.ISBN",
                "openminds.v4.core.WebResource",
            ],
            "fullDocumentation",
            required=True,
            description="Non-abridged instructions, comments, and information for using a particular product.",
            instructions="Add the publication or file that acts as the full documentation of this research product version.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            description="Whole, non-abbreviated name of the dataset version.",
            instructions="Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.",
        ),
        Property(
            "funding",
            "openminds.v4.core.Funding",
            "funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this research product version.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the dataset version.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "input_data",
            [
                "openminds.v4.core.DOI",
                "openminds.v4.core.File",
                "openminds.v4.core.FileBundle",
                "openminds.v4.core.WebResource",
                "openminds.v4.sands.BrainAtlas",
                "openminds.v4.sands.BrainAtlasVersion",
                "openminds.v4.sands.CommonCoordinateSpace",
                "openminds.v4.sands.CommonCoordinateSpaceVersion",
            ],
            "inputData",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Data that is put into a process or machine.",
            instructions="Add the data that was used as input for this dataset version.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.v4.core.DatasetVersion",
            "isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all dataset versions that can be used alternatively to this dataset version.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v4.core.DatasetVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the dataset version preceding this dataset version.",
        ),
        Property(
            "keywords",
            [
                "openminds.v4.controlled_terms.ActionStatusType",
                "openminds.v4.controlled_terms.AgeCategory",
                "openminds.v4.controlled_terms.AnalysisTechnique",
                "openminds.v4.controlled_terms.AnatomicalAxesOrientation",
                "openminds.v4.controlled_terms.AnatomicalIdentificationType",
                "openminds.v4.controlled_terms.AnatomicalPlane",
                "openminds.v4.controlled_terms.AnnotationCriteriaType",
                "openminds.v4.controlled_terms.AnnotationType",
                "openminds.v4.controlled_terms.AtlasType",
                "openminds.v4.controlled_terms.AuditoryStimulusType",
                "openminds.v4.controlled_terms.BiologicalOrder",
                "openminds.v4.controlled_terms.BiologicalProcess",
                "openminds.v4.controlled_terms.BiologicalSex",
                "openminds.v4.controlled_terms.BreedingType",
                "openminds.v4.controlled_terms.CellCultureType",
                "openminds.v4.controlled_terms.CellType",
                "openminds.v4.controlled_terms.ChemicalMixtureType",
                "openminds.v4.controlled_terms.Colormap",
                "openminds.v4.controlled_terms.ContributionType",
                "openminds.v4.controlled_terms.CranialWindowConstructionType",
                "openminds.v4.controlled_terms.CranialWindowReinforcementType",
                "openminds.v4.controlled_terms.CriteriaQualityType",
                "openminds.v4.controlled_terms.DataType",
                "openminds.v4.controlled_terms.DeviceType",
                "openminds.v4.controlled_terms.DifferenceMeasure",
                "openminds.v4.controlled_terms.Disease",
                "openminds.v4.controlled_terms.DiseaseModel",
                "openminds.v4.controlled_terms.EducationalLevel",
                "openminds.v4.controlled_terms.ElectricalStimulusType",
                "openminds.v4.controlled_terms.EthicsAssessment",
                "openminds.v4.controlled_terms.ExperimentalApproach",
                "openminds.v4.controlled_terms.FileBundleGrouping",
                "openminds.v4.controlled_terms.FileRepositoryType",
                "openminds.v4.controlled_terms.FileUsageRole",
                "openminds.v4.controlled_terms.GeneticStrainType",
                "openminds.v4.controlled_terms.GustatoryStimulusType",
                "openminds.v4.controlled_terms.Handedness",
                "openminds.v4.controlled_terms.Language",
                "openminds.v4.controlled_terms.Laterality",
                "openminds.v4.controlled_terms.LearningResourceType",
                "openminds.v4.controlled_terms.MRIPulseSequence",
                "openminds.v4.controlled_terms.MRIWeighting",
                "openminds.v4.controlled_terms.MeasuredQuantity",
                "openminds.v4.controlled_terms.MeasuredSignalType",
                "openminds.v4.controlled_terms.MetaDataModelType",
                "openminds.v4.controlled_terms.ModelAbstractionLevel",
                "openminds.v4.controlled_terms.ModelScope",
                "openminds.v4.controlled_terms.MolecularEntity",
                "openminds.v4.controlled_terms.OlfactoryStimulusType",
                "openminds.v4.controlled_terms.OperatingDevice",
                "openminds.v4.controlled_terms.OperatingSystem",
                "openminds.v4.controlled_terms.OpticalStimulusType",
                "openminds.v4.controlled_terms.Organ",
                "openminds.v4.controlled_terms.OrganismSubstance",
                "openminds.v4.controlled_terms.OrganismSystem",
                "openminds.v4.controlled_terms.PatchClampVariation",
                "openminds.v4.controlled_terms.PreparationType",
                "openminds.v4.controlled_terms.ProductAccessibility",
                "openminds.v4.controlled_terms.ProgrammingLanguage",
                "openminds.v4.controlled_terms.QualitativeOverlap",
                "openminds.v4.controlled_terms.SemanticDataType",
                "openminds.v4.controlled_terms.Service",
                "openminds.v4.controlled_terms.SetupType",
                "openminds.v4.controlled_terms.SoftwareApplicationCategory",
                "openminds.v4.controlled_terms.SoftwareFeature",
                "openminds.v4.controlled_terms.Species",
                "openminds.v4.controlled_terms.StimulationApproach",
                "openminds.v4.controlled_terms.StimulationTechnique",
                "openminds.v4.controlled_terms.SubcellularEntity",
                "openminds.v4.controlled_terms.SubjectAttribute",
                "openminds.v4.controlled_terms.TactileStimulusType",
                "openminds.v4.controlled_terms.Technique",
                "openminds.v4.controlled_terms.TermSuggestion",
                "openminds.v4.controlled_terms.Terminology",
                "openminds.v4.controlled_terms.TissueSampleAttribute",
                "openminds.v4.controlled_terms.TissueSampleType",
                "openminds.v4.controlled_terms.TypeOfUncertainty",
                "openminds.v4.controlled_terms.UBERONParcellation",
                "openminds.v4.controlled_terms.UnitOfMeasurement",
                "openminds.v4.controlled_terms.VisualStimulusType",
            ],
            "keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Significant word or concept that are representative of the dataset version.",
            instructions="Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.",
        ),
        Property(
            "license",
            ["openminds.v4.core.License", "openminds.v4.core.WebResource"],
            "license",
            required=True,
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license or an online available data usage agreement for this dataset version.",
        ),
        Property(
            "other_contributions",
            "openminds.v4.core.Contribution",
            "otherContribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
            instructions="Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.",
        ),
        Property(
            "preparation_designs",
            "openminds.v4.controlled_terms.PreparationType",
            "preparationDesign",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all preparation types used in this dataset version.",
        ),
        Property(
            "protocols",
            "openminds.v4.core.Protocol",
            "protocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Plan that describes the process of a scientific or medical experiment, treatment, or procedure.",
            instructions="Add all protocols that were performed in this dataset version (e.g., for data acquisition or processing).",
        ),
        Property(
            "related_publications",
            [
                "openminds.v4.core.DOI",
                "openminds.v4.core.HANDLE",
                "openminds.v4.core.ISBN",
                "openminds.v4.core.ISSN",
                "openminds.v4.publications.Book",
                "openminds.v4.publications.Chapter",
                "openminds.v4.publications.ScholarlyArticle",
            ],
            "relatedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to something that was made available for the general public to see or buy.",
            instructions="Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).",
        ),
        Property(
            "release_date",
            date,
            "releaseDate",
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.",
        ),
        Property(
            "repository",
            "openminds.v4.core.FileRepository",
            "repository",
            description="Place, room, or container where something is deposited or stored.",
            instructions="Add the file repository of this research product version.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the dataset version.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "studied_specimens",
            [
                "openminds.v4.core.Subject",
                "openminds.v4.core.SubjectGroup",
                "openminds.v4.core.TissueSample",
                "openminds.v4.core.TissueSampleCollection",
            ],
            "studiedSpecimen",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all specimens or sets of specimen that were studied in this dataset.",
        ),
        Property(
            "study_targets",
            [
                "openminds.v4.controlled_terms.AuditoryStimulusType",
                "openminds.v4.controlled_terms.BiologicalOrder",
                "openminds.v4.controlled_terms.BiologicalSex",
                "openminds.v4.controlled_terms.BreedingType",
                "openminds.v4.controlled_terms.CellCultureType",
                "openminds.v4.controlled_terms.CellType",
                "openminds.v4.controlled_terms.Disease",
                "openminds.v4.controlled_terms.DiseaseModel",
                "openminds.v4.controlled_terms.ElectricalStimulusType",
                "openminds.v4.controlled_terms.GeneticStrainType",
                "openminds.v4.controlled_terms.GustatoryStimulusType",
                "openminds.v4.controlled_terms.Handedness",
                "openminds.v4.controlled_terms.MolecularEntity",
                "openminds.v4.controlled_terms.OlfactoryStimulusType",
                "openminds.v4.controlled_terms.OpticalStimulusType",
                "openminds.v4.controlled_terms.Organ",
                "openminds.v4.controlled_terms.OrganismSubstance",
                "openminds.v4.controlled_terms.OrganismSystem",
                "openminds.v4.controlled_terms.Species",
                "openminds.v4.controlled_terms.SubcellularEntity",
                "openminds.v4.controlled_terms.TactileStimulusType",
                "openminds.v4.controlled_terms.TermSuggestion",
                "openminds.v4.controlled_terms.TissueSampleType",
                "openminds.v4.controlled_terms.UBERONParcellation",
                "openminds.v4.controlled_terms.VisualStimulusType",
                "openminds.v4.sands.CustomAnatomicalEntity",
                "openminds.v4.sands.ParcellationEntity",
                "openminds.v4.sands.ParcellationEntityVersion",
            ],
            "studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this dataset version.",
        ),
        Property(
            "support_channels",
            str,
            "supportChannel",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Way of communication used to interact with users or customers.",
            instructions="Enter all channels through which a user can receive support for handling this research product version.",
        ),
        Property(
            "techniques",
            [
                "openminds.v4.controlled_terms.AnalysisTechnique",
                "openminds.v4.controlled_terms.MRIPulseSequence",
                "openminds.v4.controlled_terms.MRIWeighting",
                "openminds.v4.controlled_terms.StimulationApproach",
                "openminds.v4.controlled_terms.StimulationTechnique",
                "openminds.v4.controlled_terms.Technique",
            ],
            "technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Method of accomplishing a desired aim.",
            instructions="Add all techniques that were used in this dataset version.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this research product version.",
        ),
        Property(
            "version_innovation",
            str,
            "versionInnovation",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.",
        ),
    ]

    def __init__(
        self,
        id=None,
        accessibility=None,
        authors=None,
        behavioral_protocols=None,
        copyright=None,
        custodians=None,
        data_types=None,
        description=None,
        digital_identifier=None,
        ethics_assessment=None,
        experimental_approaches=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        input_data=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        keywords=None,
        license=None,
        other_contributions=None,
        preparation_designs=None,
        protocols=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        studied_specimens=None,
        study_targets=None,
        support_channels=None,
        techniques=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            accessibility=accessibility,
            authors=authors,
            behavioral_protocols=behavioral_protocols,
            copyright=copyright,
            custodians=custodians,
            data_types=data_types,
            description=description,
            digital_identifier=digital_identifier,
            ethics_assessment=ethics_assessment,
            experimental_approaches=experimental_approaches,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            input_data=input_data,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            keywords=keywords,
            license=license,
            other_contributions=other_contributions,
            preparation_designs=preparation_designs,
            protocols=protocols,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            studied_specimens=studied_specimens,
            study_targets=study_targets,
            support_channels=support_channels,
            techniques=techniques,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
