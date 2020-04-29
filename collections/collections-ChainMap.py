from collections import ChainMap

common_attributes = {"Species": "Human", "Residence": "Earth", "Powers": None}
goku_special_attributes = {
    "Name": "Son Goku",
    "Species": "Saiyan",
    "Powers": [
        "FTL combat",
        "Instantaneous transmission",
        "Ki blast",
        "Combat mastery",
    ],
}
superman_special_attributes = {
    "Name": "Clark Kent",
    "Species": "Kryptonian",
    "Powers": ["Invulnerable", "Frost Breath", "Heat Ray"],
}


goku_attributes = ChainMap(goku_special_attributes, common_attributes)
superman_attributes = ChainMap(superman_special_attributes, common_attributes)

print(goku_attributes["Residence"])  # Earth # * Taken from common attributes
print(
    goku_attributes["Powers"]
)  #  ['FTL combat','Instantaneous transmission','Ki blast','Combat mastery'] # * Taken from special attributes (overwrites common)
# print(goku_attributes["abc"]) # ! KeyError
common_attributes["Residence"] = "Mars"

print(
    goku_attributes["Residence"]
)  # Mars # * Holds reference to the original data structure
print(
    superman_attributes["Residence"]
)  # Mars # * References the same common_attributes object so changes

superman_attributes["Residence"] = "Krypton"

print(goku_attributes["Residence"])  # Mars # * Unchanged
print(superman_attributes["Residence"])  # Krypton # * Changed
print(
    superman_special_attributes.keys()
)  # dict_keys(['Name','Species','Powers','Residence']) # * The change is made in the leftmost mapping, the one that takes precedence.

print(superman_attributes.maps)  # * The underlying maps
print(
    superman_attributes.parents
)  # * The underlying maps; this skips the first mapping and can be used to access deeper attributes which are also defined in the default mapping
