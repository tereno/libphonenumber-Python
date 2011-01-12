# Generic exception class for errors encountered when parsing phone numbers
# This is a port from the Java implementation
# @author: Teren Teh
class NumberParseException(Exception):

    def __init__(self, errorType, message):
        self.super(message)
        self.message = message
        self.errorType = errorType
        
    ErrorType = {
                    'INVALID_COUNTRY_CODE':  0,
                    
                    # The string passed in had less than 3 digits in it
                    # The number failed to match the regular expression
                    # VALID_PHONE_NUMBER in phonenumberutil.py
                    'NOT_A_NUMBER': 1,
                    
                    # The string started with an international dialing prefix
                    # but after this was removed, it had less digits than
                    # any valid phone number (including country code) 
                    # could have
                    'TOO_SHORT_AFTER_IDD': 2,
                    
                    # After any country code has been stripped, the string
                    # had less digits than any valid phone number could have
                    'TOO_SHORT_NSN': 3,
                    
                    # String had more digits than any valid phone number could
                    # have
                    'TOO_LONG': 4
                 }
    
    def __str__(self):
        return "Error type: %s. %s" % (self.errorType, self.message)

    def getErrorType(self):
        return errorType
