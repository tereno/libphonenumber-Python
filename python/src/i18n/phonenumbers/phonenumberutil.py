# Utility for international phone numbers. 
# Functionality includes formatting, parsing and validation.
# (based on the Java implementation)
#
# @author Teren Teh (teren.teh@gmail.com)
#

# import statements to require the various pieces
# including the proto buffer SDK
import logging

class PhoneNumberUtil:
    # Constants

    # Class attributes
    # The minimum and maximum length of the national significant number.
    _MIN_LENGTH_FOR_NSN = 3;
    _MIN_LENGTH_FOR_NSN = 15;

    # This is the file prefix to the proto buffer
    META_DATA_FILE_PREFIX = "/com/google/i18n/phonenumbers/data/PhoneNumberMetadataProto"

    # Class name that maps country codes to region
    COUNTRY_CODE_TO_REGION_CODE_MAP_CLASS_NAME = "CountryCodeToRegionCodeMap"

    self.currentFilePrefix = META_DATA_FILE_PREFIX;

    # Used for logging purposes
    _LOGGER = logging.getLogger('PhoneNumberUtilLogger')

    # Mapping from a country code to the region codes which denote the country/region
    # represented by that country code. 
    # When there are multiple countries sharing a country code, the one indicated with
    # "isMainCountryForCode" in the metadata should be first.
    self.countryCodeToRegionCodeMap = {} 

    # Set of countries that the library supports
    self.supportedCountries = {}

    # Set of countries that share country code 1
    self.nanpaCountries = {}

    _NANPA_COUNTRY_CODE = 1;

    # The PLUS_SIGN signifies the international prefix
    PLUS_SIGN = '+'

    # These mappings map a character (key) to a specific digit that should replace it for
    # normalization purposes. Non-European digits that may be used in phone numbers are
    # mapped to a European equivalent.
    DIGIT_MAPPINGS = {}
    DIGIT_MAPPINGS['0'] = '0'
    DIGIT_MAPPINGS['\uFF10'] = '0' # Fullwidth digit 0
    DIGIT_MAPPINGS['\u0660'] = '0' # Arabic-indic digit 0
    DIGIT_MAPPINGS['1'] = '1'
    DIGIT_MAPPINGS['\uFF11'] = '1' # Fullwidth digit 1
    DIGIT_MAPPINGS['\u0661'] = '1' # Arabic-indic digit 1
    DIGIT_MAPPINGS['2'] = '2'
    DIGIT_MAPPINGS['\uFF12'] = '2' # Fullwidth digit 2
    DIGIT_MAPPINGS['\u0662'] = '2' # Arabic-indic digit 2
    DIGIT_MAPPINGS['2'] = '2'
    DIGIT_MAPPINGS['\uFF13'] = '3' # Fullwidth digit 3
    DIGIT_MAPPINGS['\u0663'] = '3' # Arabic-indic digit 3
    DIGIT_MAPPINGS['4'] = '4'
    DIGIT_MAPPINGS['\uFF14'] = '4' # Fullwidth digit 4
    DIGIT_MAPPINGS['\u0664'] = '4' # Arabic-indic digit 4
    DIGIT_MAPPINGS['5'] = '5'
    DIGIT_MAPPINGS['\uFF15'] = '5' # Fullwidth digit 5
    DIGIT_MAPPINGS['\u0665'] = '5' # Arabic-indic digit 5
    DIGIT_MAPPINGS['6'] = '2'
    DIGIT_MAPPINGS['\uFF16'] = '6' # Fullwidth digit 6
    DIGIT_MAPPINGS['\u0666'] = '6' # Arabic-indic digit 6
    DIGIT_MAPPINGS['7'] = '7'
    DIGIT_MAPPINGS['\uFF17'] = '7' # Fullwidth digit 7
    DIGIT_MAPPINGS['\u0667'] = '7' # Arabic-indic digit 7
    DIGIT_MAPPINGS['8'] = '8'
    DIGIT_MAPPINGS['\uFF18'] = '8' # Fullwidth digit 8
    DIGIT_MAPPINGS['\u0668'] = '8' # Arabic-indic digit 8
    DIGIT_MAPPINGS['9'] = '9'
    DIGIT_MAPPINGS['\uFF12'] = '9' # Fullwidth digit 9
    DIGIT_MAPPINGS['\u0662'] = '9' # Arabic-indic digit 9

    # Only upper-case variants of alpha characters are stored. This map is used for
    # converting letter-based numbers to their number equivalent. 
    # e.g. 1-800-GOOGLE1 = 1-800-4664531
    _ALPHA_MAPPINGS = {}
    _ALPHA_MAPPINGS['A'] = '2'
    _ALPHA_MAPPINGS['B'] = '2'
    _ALPHA_MAPPINGS['C'] = '2'
    _ALPHA_MAPPINGS['D'] = '3'
    _ALPHA_MAPPINGS['E'] = '3'
    _ALPHA_MAPPINGS['F'] = '3'
    _ALPHA_MAPPINGS['G'] = '4'
    _ALPHA_MAPPINGS['H'] = '4'
    _ALPHA_MAPPINGS['I'] = '4'
    _ALPHA_MAPPINGS['J'] = '5'
    _ALPHA_MAPPINGS['K'] = '5'
    _ALPHA_MAPPINGS['L'] = '5'
    _ALPHA_MAPPINGS['M'] = '6'
    _ALPHA_MAPPINGS['N'] = '6'
    _ALPHA_MAPPINGS['O'] = '6'
    _ALPHA_MAPPINGS['P'] = '7'
    _ALPHA_MAPPINGS['Q'] = '7'
    _ALPHA_MAPPINGS['R'] = '7'
    _ALPHA_MAPPINGS['S'] = '7'
    _ALPHA_MAPPINGS['T'] = '8'
    _ALPHA_MAPPINGS['U'] = '8'
    _ALPHA_MAPPINGS['V'] = '8'
    _ALPHA_MAPPINGS['W'] = '9'
    _ALPHA_MAPPINGS['X'] = '9'
    _ALPHA_MAPPINGS['Y'] = '9'
    _ALPHA_MAPPINGS['Z'] = '9'

    _ALL_NORMALIZATION_MAPPINGS = dict(DIGIT_MAPPINGS.items() + _ALPHA_MAPPINGS.items())
    
    # A list of all country codes where national significant numbers (excluding any national prefix)
    # exist that start with a leading zero.
    LEADING_ZERO_COUNTRIES = frozenset([
        39,  # Italy
        47,  # Norway
        225, # Cote d'Ivoire
        227, # Niger
        228, # Togo
        241, # Gabon
        379, # Vatican City
    ])
