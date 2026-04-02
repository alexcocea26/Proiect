from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


# =========================
# Identifiers
# =========================

class IdentifierBase(BaseModel):
    identifier_name: str
    description: Optional[str] = None
    identifier_type: Optional[str] = None


class IdentifierCreate(IdentifierBase):
    pass


class IdentifierUpdate(BaseModel):
    description: Optional[str] = None
    identifier_type: Optional[str] = None


class IdentifierResponse(IdentifierBase):
    class Config:
        from_attributes = True


# =========================
# Countries
# =========================

class CountryBase(BaseModel):
    name: str
    iso_code: Optional[str] = None
    short_code: Optional[str] = None


class CountryCreate(CountryBase):
    pass


class CountryUpdate(BaseModel):
    iso_code: Optional[str] = None
    short_code: Optional[str] = None


class CountryResponse(CountryBase):
    class Config:
        from_attributes = True


# =========================
# ConsumerUnits
# =========================

class ConsumerUnitBase(BaseModel):
    number_of_consumers: int
    country_name: str


class ConsumerUnitCreate(ConsumerUnitBase):
    pass


class ConsumerUnitUpdate(BaseModel):
    number_of_consumers: Optional[int] = None
    country_name: Optional[str] = None


class ConsumerUnitResponse(ConsumerUnitBase):
    class Config:
        from_attributes = True


# =========================
# Ownership
# =========================

class OwnershipBase(BaseModel):
    identifier_name: str
    originator_first_name: Optional[str] = None
    originator_last_name: Optional[str] = None
    user_id_tnumber: str
    user_id_intranet: Optional[str] = None
    email: Optional[str] = None
    owner_first_name: Optional[str] = None
    owner_last_name: Optional[str] = None


class OwnershipCreate(OwnershipBase):
    pass


class OwnershipUpdate(BaseModel):
    originator_first_name: Optional[str] = None
    originator_last_name: Optional[str] = None
    user_id_intranet: Optional[str] = None
    email: Optional[str] = None
    owner_first_name: Optional[str] = None
    owner_last_name: Optional[str] = None


class OwnershipResponse(OwnershipBase):
    class Config:
        from_attributes = True


# =========================
# Relationships
# =========================

class RelationshipBase(BaseModel):
    from_identifier_name: str
    to_identifier_name: str
    relationship_name: Optional[str] = None


class RelationshipCreate(RelationshipBase):
    pass


class RelationshipUpdate(BaseModel):
    relationship_name: Optional[str] = None


class RelationshipResponse(RelationshipBase):
    class Config:
        from_attributes = True


# =========================
# Characteristics
# =========================

class CharacteristicBase(BaseModel):
    master_name: str
    name: str
    specifics: Optional[str] = None
    action_required: Optional[str] = None
    report_type: Optional[str] = None
    data_type: Optional[str] = None
    lower_routine_release_limit: Optional[Decimal] = None
    lower_limit: Optional[Decimal] = None
    lower_target: Optional[Decimal] = None
    target: Optional[Decimal] = None
    upper_target: Optional[Decimal] = None
    upper_limit: Optional[Decimal] = None
    upper_routine_release_limit: Optional[Decimal] = None
    test_frequency: Optional[int] = None
    precision: Optional[int] = None
    engineering_unit: Optional[str] = None


class CharacteristicCreate(CharacteristicBase):
    pass


class CharacteristicUpdate(BaseModel):
    specifics: Optional[str] = None
    action_required: Optional[str] = None
    report_type: Optional[str] = None
    data_type: Optional[str] = None
    lower_routine_release_limit: Optional[Decimal] = None
    lower_limit: Optional[Decimal] = None
    lower_target: Optional[Decimal] = None
    target: Optional[Decimal] = None
    upper_target: Optional[Decimal] = None
    upper_limit: Optional[Decimal] = None
    upper_routine_release_limit: Optional[Decimal] = None
    test_frequency: Optional[int] = None
    precision: Optional[int] = None
    engineering_unit: Optional[str] = None


class CharacteristicResponse(CharacteristicBase):
    class Config:
        from_attributes = True


# =========================
# IdentifierCharacteristics
# =========================

class IdentifierCharacteristicBase(BaseModel):
    identifier_name: str
    master_name: str
    characteristic_name: str


class IdentifierCharacteristicCreate(IdentifierCharacteristicBase):
    pass


class IdentifierCharacteristicUpdate(BaseModel):
    pass


class IdentifierCharacteristicResponse(IdentifierCharacteristicBase):
    class Config:
        from_attributes = True