__author__ = 'David'

from datetime import datetime

from peewee import *
import loadextantdata

db = SqliteDatabase("Housing.db")

class Housing(Model):
    """
    The base model for the housing database.
    """
    building_name = CharField(max_length=100)
    address = CharField(max_length=255)
    available_subsidized_units = IntegerField(default=0)
    num_of_subsidized_units = IntegerField(default=0)
    available_affordable_units = IntegerField(default=0)
    num_of_affordable_units = IntegerField(default=0)
    num_of_units = IntegerField(default=0)
    property_management = CharField(max_length=255)
    contact_info = CharField(max_length=20)
    website = CharField(max_length=255)
    types_of_housing = CharField(max_length=255)
    housing_programs = CharField(max_length=100)
    color = CharField(max_length=25)
    number = IntegerField(default=0)
    extra_1 = CharField(max_length=50, default=" ")
    extra_2 = CharField(max_length=50, default=" ")

    class Meta:
        database = db

def add_housing_complex(building=None,
                        address=None,
                        asub=None,
                        sub=None,
                        aaff=None,
                        aff=None,
                        units=None,
                        management=None,
                        contact=None,
                        website=None,
                        types=None,
                        programs=None,
                        extra1=None,
                        extra2=None
                        ):
    """
    This will add a housing model from the Housing table.
    :return:
    """
    try:
        Housing.create(building_name=building,
                       address=address,
                       available_subsidized_units=asub,
                       num_of_subsidized_units=sub,
                       available_affordable_units=aaff,
                       num_of_affordable_units=aff,
                       num_of_units=units,
                       property_management=management,
                       contact_info=contact,
                       website=website,
                       types_of_housing=types,
                       housing_programs=programs,
                       extra_1=extra1,
                       extra_2=extra2
                       )
        return "Entry Added"
    except:
        return "Error"

def remove_housing_complex(entry):
    """
    This will remove a housing model from the Housing table.
    :param entry:
    :return:
    """
    if input("Are you sure? [yN]: ").lower == "y":
        Housing.delete_instance(entry)
        print("Entry deleted")

def change_available_housing():
    """
    This will modify either the available_subsidized_units or the available_affordable_units
    :return:
    """
    pass

def search_entries():
    """
    Search entries for a string.
    :return:
    """
    view_entry(input("search query: "))

def view_entry(search_query=None):
    """
    View previous entries
    :return:
    """
    entries = Housing.select().order_by(Housing.building_name)

    if search_query:
        entries = entries.select().where(Housing.contains(search_query))

    for entry in entries:
        print(entry.building_name, entry.num_of_subsidized_units)

def return_specific(name=None):
    """
    Looks for a specific entry by housing complex name and returns that complex' name and address
    :param name:
    :return:
    """
    entries = Housing.select().order_by(Housing.building_name)

    if name:
        entries = Housing.select().where(Housing.building_name.contains(name),
                                         Housing.address.contains("1"))

    for entry in entries:
        print(entry.building_name, entry.address)

def load_database():
    """
    Initializes the data base loading it from the csv downloaded from google along with the loadextantdata module.
    :return:
    """
    data = loadextantdata.get_data()
    for name, address, units, subu, au, propm, cont, web, type, hp, col, num, ext1, ext2 in data:
        Housing.create(
            building_name=name,
            address=address,
            num_of_subsidized_units=subu,
            num_of_affordable_units=au,
            num_of_units=units,
            property_management=propm,
            contact_info=cont,
            website=web,
            types_of_housing=type,
            housing_programs=hp,
            color=col,
            number=num,
            extra_1=ext1,
            extra_2=ext2,
            safe=True
        )

if __name__ == "__main__":
    db.connect()
    db.create_tables([Housing], safe=True)
    # view_entry()
    return_specific("ARC")


