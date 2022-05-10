from dataclasses import dataclass


@dataclass
class Result:
    """
    Result returned from RestAdapter
    :param status_code: Status code of the response
    :param message: Human readable message of the response
    :param total: The total number of results.
    :param offset: The offset for the results.
    :param limit: The maximum number of results to be returned.
    :paran data: List of dict or single dict
    """
    status_code: int
    message: str = None
    total: int = None
    offset: int = None
    limit: int = None
    results: list[dict] | dict = None


@dataclass
class NamedResourceReference:
    id: str
    resourceType: str
    name: str


@dataclass
class Domain(NamedResourceReference):
    pass


@dataclass
class Type(NamedResourceReference):
    pass


@dataclass
class Status(NamedResourceReference):
    pass


@dataclass
class Parent(NamedResourceReference):
    pass


@dataclass
class SymbolData:
    color: str
    symbolType: str
    acronymCode: str = None
    iconCode: str = None


@dataclass
class Asset:
    id: str
    createdBy: str
    createdOn: int
    lastModifiedBy: str
    lastModifiedOn: int
    system: bool
    resourceType: str
    name: str
    displayName: str
    excludedFromAutoHyperlinking: bool
    domain: Domain | dict
    type: Type | dict
    status: Status | dict
    avgRating: float
    ratingsCount: int
    articulationScore: float = 0.0

    def __post_init__(self):
        self.domain = Domain(**self.domain) or self.domain
        self.type = Type(**self.type) or self.type
        self.status = Status(**self.status) or self.status


@dataclass
class AssetType:
    id: str
    createdBy: str
    createdOn: int
    lastModifiedBy: str
    lastModifiedOn: int
    system: bool
    resourceType: str
    name: str
    description: str
    parent: Parent | dict
    symbolData: SymbolData | dict
    displayNameEnabled: bool
    ratingEnabled: bool

    def __post_init__(self):
        self.parent = Parent(**self.parent) or self.parent
        self.symbolData = SymbolData(**self.symbolData) or self.symbolData
