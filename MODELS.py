from sqlalchemy import Column, String, Integer, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Identifier(Base):
    _tablename_ = 'Identifiers'
    
    identifier_name = Column(String(255), primary_key=True)
    description = Column(Text)
    identifier_type = Column(String(255))

class Country(Base):
    _tablename_ = 'Countries'
    
    name = Column(String(255), primary_key=True)
    iso_code = Column(String(255))
    short_code = Column(String(255))

class ConsumerUnit(Base):
    _tablename_ = 'ConsumerUnits'
    
    number_of_consumers = Column(Integer, primary_key=True)
    country_name = Column(String(255), ForeignKey('Countries.name'), primary_key=True)
    country = relationship('Country', back_populates='consumer_units')

Country.consumer_units = relationship('ConsumerUnit', order_by=ConsumerUnit.number_of_consumers, back_populates='country')

class Ownership(Base):
    _tablename_ = 'Ownership'
    
    identifier_name = Column(String(255), ForeignKey('Identifiers.identifier_name'), primary_key=True)
    originator_first_name = Column(String(255))
    originator_last_name = Column(String(255))
    user_id_tnumber = Column(String(255), primary_key=True)
    user_id_intranet = Column(String(255))
    email = Column(String(255))
    owner_first_name = Column(String(255))
    owner_last_name = Column(String(255))
    identifier = relationship('Identifier')

class Relationship(Base):
    _tablename_ = 'Relationships'
    
    from_identifier_name = Column(String(255), ForeignKey('Identifiers.identifier_name'), primary_key=True)
    to_identifier_name = Column(String(255), ForeignKey('Identifiers.identifier_name'), primary_key=True)
    relationship_name = Column(String(255))
    from_identifier = relationship('Identifier', foreign_keys=[from_identifier_name])
    to_identifier = relationship('Identifier', foreign_keys=[to_identifier_name])

class Characteristic(Base):
    _tablename_ = 'Characteristics'
    
    master_name = Column(String(255), primary_key=True)
    name = Column(String(255), primary_key=True)
    specifics = Column(String(255))
    action_required = Column(String(255))
    report_type = Column(String(255))
    data_type = Column(String(255))
    lower_routine_release_limit = Column(DECIMAL(10, 2))
    lower_limit = Column(DECIMAL(10, 2))
    lower_target = Column(DECIMAL(10, 2))
    target = Column(DECIMAL(10, 2))
    upper_target = Column(DECIMAL(10, 2))
    upper_limit = Column(DECIMAL(10, 2))
    upper_routine_release_limit = Column(DECIMAL(10, 2))
    test_frequency = Column(Integer)
    precision = Column(Integer)
    engineering_unit = Column(String(255))


class IdentifierCharacteristic(Base):
    _tablename_ = 'IdentifierCharacteristics'

    identifier_name = Column(String(255), ForeignKey('Identifiers.identifier_name'), primary_key=True)
    master_name = Column(String(255), primary_key=True)
    characteristic_name = Column(String(255), primary_key=True)

    _table_args_ = (
        ForeignKeyConstraint(
            ['master_name', 'characteristic_name'],
            ['Characteristics.master_name', 'Characteristics.name']
        ),
    )

    identifier = relationship('Identifier')
    characteristic = relationship('Characteristic')