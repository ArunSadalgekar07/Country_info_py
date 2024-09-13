# Import the required module
from countryinfo import CountryInfo

# Input the Name of the Country
name=input("Enter your country : ")

# Passing the country name to the in-built function of the module
country = CountryInfo(name)

#using the predefined functions

#Capital of the Country
print("Capital is : ",country.capital())

#Currency used in the Country
print("Currencies is :",country.currencies())

#Languages spoken in the Country
print("Language is : ",country. languages())

#Borders of the Country and Function
print("Borders are : ",country.borders())

#Provinces of the Country
print("Provinces are : ", country.provinces())

#Areas in the Country
print("Area are : ", country.area())

#Country Code of the Country
print("Calling are : ", country.calling_codes())

#Latitudes and Longitudes of the Country
print("Capital Latitudes and Longitudes are : ", 
                          country.capital_latlng())

#TimeZone in the Country
print("TimeZone : ", country.timezones())

#Current Population in the Country
print("Population : ", country.population())

#Other Names of the Country
print("Others names : ",country.alt_spellings())

