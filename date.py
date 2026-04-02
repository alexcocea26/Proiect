from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from proiect import (
    Identifier,
    Country,
    ConsumerUnit,
    Ownership,
    Relationship,
    Characteristic,
    IdentifierCharacteristic
)

DATABASE_URL = "mssql+pyodbc://COCEA\\SQLEXPRESS/proiect?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

try:
    # 1. Identifiers
    identifiers = [
        Identifier(identifier_name='88823141', description='Shampoo Product', identifier_type='Finished Product Part'),
        Identifier(identifier_name='88823142', description='Packaging Carton', identifier_type='Packaging Material Part'),
        Identifier(identifier_name='88823143', description='Packaging Box', identifier_type='Packaging Material Part'),
        Identifier(identifier_name='88823144', description='Chemical Substance', identifier_type='Assembled Product Part'),
        Identifier(identifier_name='88823145', description='Water', identifier_type='Assembled Product Part'),
        Identifier(identifier_name='88823146', description='Shampoo Bottle', identifier_type='Material Part'),
    ]
    session.add_all(identifiers)
    session.commit()

    # 2. Countries
    countries = [
        Country(name='Luxembourg', iso_code='LU', short_code='442'),
        Country(name='France', iso_code='FR', short_code='250'),
        Country(name='Germany', iso_code='DE', short_code='276'),
        Country(name='Belgium', iso_code='BE', short_code='056'),
        Country(name='Netherlands', iso_code='NL', short_code='528'),
        Country(name='Sweden', iso_code='SE', short_code='752'),
        Country(name='Norway', iso_code='NO', short_code='578'),
    ]
    session.add_all(countries)
    session.commit()

    # 3. ConsumerUnits
    consumer_units = [
        ConsumerUnit(number_of_consumers=150, country_name='Luxembourg'),
        ConsumerUnit(number_of_consumers=200, country_name='France'),
        ConsumerUnit(number_of_consumers=100, country_name='Germany'),
        ConsumerUnit(number_of_consumers=120, country_name='Belgium'),
        ConsumerUnit(number_of_consumers=80, country_name='Netherlands'),
        ConsumerUnit(number_of_consumers=60, country_name='Sweden'),
        ConsumerUnit(number_of_consumers=90, country_name='Norway'),
    ]
    session.add_all(consumer_units)
    session.commit()

    # 4. Ownership
    ownerships = [
        Ownership(identifier_name='88823141', originator_first_name='Andrea', originator_last_name='Meier', user_id_tnumber='AP5065', user_id_intranet='meier.a.1', email='andrea@example.com', owner_first_name='Andrea', owner_last_name='Meier'),
        Ownership(identifier_name='88823142', originator_first_name='John', originator_last_name='Doe', user_id_tnumber='JD1234', user_id_intranet='doe.j.1', email='john@example.com', owner_first_name='John', owner_last_name='Doe'),
        Ownership(identifier_name='88823143', originator_first_name='Jane', originator_last_name='Smith', user_id_tnumber='JS5678', user_id_intranet='smith.j.2', email='jane@example.com', owner_first_name='Jane', owner_last_name='Smith'),
        Ownership(identifier_name='88823144', originator_first_name='Michael', originator_last_name='Brown', user_id_tnumber='MB9101', user_id_intranet='brown.m.3', email='michael@example.com', owner_first_name='Michael', owner_last_name='Brown'),
        Ownership(identifier_name='88823145', originator_first_name='Emily', originator_last_name='Davis', user_id_tnumber='ED1123', user_id_intranet='davis.e.4', email='emily@example.com', owner_first_name='Emily', owner_last_name='Davis'),
        Ownership(identifier_name='88823146', originator_first_name='David', originator_last_name='Wilson', user_id_tnumber='DW1456', user_id_intranet='wilson.d.5', email='david@example.com', owner_first_name='David', owner_last_name='Wilson'),
    ]
    session.add_all(ownerships)
    session.commit()

    # 5. Relationships
    relationships = [
        Relationship(from_identifier_name='88823141', to_identifier_name='88823142', relationship_name='Contains'),
        Relationship(from_identifier_name='88823141', to_identifier_name='88823143', relationship_name='Contains'),
        Relationship(from_identifier_name='88823141', to_identifier_name='88823144', relationship_name='Contains'),
        Relationship(from_identifier_name='88823141', to_identifier_name='88823145', relationship_name='Contains'),
        Relationship(from_identifier_name='88823141', to_identifier_name='88823146', relationship_name='Contains'),
    ]
    session.add_all(relationships)
    session.commit()

    # 6. Characteristics
    characteristics = [
        Characteristic(master_name='CM-10001', name='Volume', specifics='Shampoo Bottle Volume', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=490.0, lower_limit=490.0, lower_target=500.0, target=505.0, upper_target=510.0, upper_limit=520.0, upper_routine_release_limit=520.0, test_frequency=1, precision=2, engineering_unit='ml'),
        Characteristic(master_name='CM-10002', name='pH Level', specifics='Shampoo pH Level', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=4.0, lower_limit=4.0, lower_target=5.0, target=5.5, upper_target=6.0, upper_limit=7.0, upper_routine_release_limit=7.0, test_frequency=1, precision=2, engineering_unit='pH'),
        Characteristic(master_name='CM-10003', name='Viscosity', specifics='Shampoo Viscosity', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=10.0, lower_limit=10.0, lower_target=15.0, target=20.0, upper_target=25.0, upper_limit=30.0, upper_routine_release_limit=30.0, test_frequency=1, precision=2, engineering_unit='Pa.s'),
        Characteristic(master_name='CM-10004', name='Color', specifics='Shampoo Color', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
        Characteristic(master_name='CM-10005', name='Fragrance', specifics='Shampoo Fragrance', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
    ]
    session.add_all(characteristics)
    session.commit()

    # 7. IdentifierCharacteristics
    identifier_characteristics = [
        IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10001', characteristic_name='Volume'),
        IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10002', characteristic_name='pH Level'),
        IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10003', characteristic_name='Viscosity'),
        IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10004', characteristic_name='Color'),
        IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10005', characteristic_name='Fragrance'),
    ]
    session.add_all(identifier_characteristics)
    session.commit()

    print("Date inserate cu succes!")

except Exception as e:
    session.rollback()
    print("Eroare la inserare:", e)

finally:
    session.close()