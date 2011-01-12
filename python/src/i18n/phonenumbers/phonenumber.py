# This class is based on Phonenumber.java

class PhoneNumber:

    # Constructor
    def __init__(self):
        self.countryCodeSource_ = CountryCodeSource['FROM_NUMBER_WITH_PLUS_SIGN']
        self.hasCountryCode = False
        self._countryCode = 0
        
        self.hasNationalNumber = False
        self._nationalNumber = 0
        
        self.hasExtension = False
        self._extension = ''
        
        self.hasItalianLeadingZero = False
        self._italianLeadingZero = False
        
        self.hasRawInput = False
        self._rawInput = ''
        
        self.hasCountryCodeSource = False
        self._countryCodeSource = ''

    # Enum - CountryCodeSource
    CountryCodeSource = {'FROM_NUMBER_WITH_PLUS_SIGN' : 0,
                         'FROM_NUMBER_WITH_IDD' : 1,
                         'FROM_NUMBER_WITHOUT_PLUS_SIGN' : 2,
                         'FROM_DEFAULT_COUNTRY' : 3}

    
    
    # required int32 country_code = 1;
    def hasCountryCode(self):
        return self.hasCountryCode
    
    def getCountryCode(self):
        return self._countryCode
    
    def setCountryCode(self, code):
        self.hasCountryCode = True
        self._countryCode = code
        return self
    
    def clearCountryCode(self):
        self.hasCountryCode = False
        self._countryCode = 0
        return self
    
    # required uint64 national_number = 2;
    def hasNationalNumber(self):
        return self.hasNationalNumber
    
    def getNationalNumber(self):
        return self._nationalNumber
    
    def setNationalNumber(self, number):
        self.hasNationalNumber = True
        self._nationalNumber = number
        return self
    
    def clearNationalNumber(self):
        self.hasNationalNumber = False
        self._nationalNumber = 0
        return self
    
    # optional string extension = 3
    def hasExtension(self):
        return self.hasExtension
    
    def getExtension(self):
        return self._extension
    
    def setExtension(self, extension):
        if extension is None:
            raise ValueError('No extension provided - extension must not be None')
        self.hasExtension = True
        self._extension = extension
        return self
        
    def clearExtension(self):
       self.hasExtension = False
       self._extension = ''
       return self 

    # optional bool italian_leading_zero = 4;
    def hasItalianLeadingZero(self):
        return self.hasItalianLeadingZero
    
    def getItalianLeadingZero(self):
        return self._italianLeadingZero
    
    def setItalianLeadingZero(self, value):
        self.hasItalianLeadingZero = True
        self._italianLeadingZero = value
        return self

    def clearItalianLeadingZero(self):
        self.hasItalianLeadingZero = False
        self._italianLeadingZero = False
        return self

    # optional string raw_input = 5;
    def hasRawInput(self):
        return self.hasRawInput
    
    def getRawInput(self):
        return self._rawInput
    
    def setRawInput(self, value):
        if value is None:
            raise ValueError("Value provided must not be None")
        self.hasRawInput = True
        self._rawInput = value
        return self
    
    def clearRawInput(self):
        self.hasRawInput = False
        self._rawInput = ''
        return self
    
    # optional CountryCodeSource country_code_source = 6;
    def hasCountryCodeSource(self):
        return self.hasCountryCodeSource
    
    def getCountryCodeSource(self):
        return self._countryCodeSource
    
    def setCountryCodeSource(self, countryCodeSource):
        if countryCodeSource is None:
            raise ValueError("Country Code source provided must not be None")
        self.hasCountryCodeSource = True
        self._countryCodeSource = countryCodeSource
        return self
    
    def clearCountryCodeSource(self):
        self.hasCountryCodeSource = False
        self._countryCodeSource = CountryCodeSource['FROM_NUMBER_WITH_PLUS_SIGN']
        return self

    def clear(self):
        self.clearCountryCode()
        self.clearNationalNumber()
        self.clearExtension()
        self.clearItalianLeadingZero()
        self.clearRawInput()
        self.clearCountryCodeSource()
        return self

    def mergeFrom(self, otherNumber):
        if otherNumber.hasCountryCode():
            self.setCountryCode(otherNumber.getCountryCode())
        if otherNumber.hasNationalNumber():
            self.setNationalNumber(otherNumber.getNationalNumber())
        if otherNumber.hasExtension():
            self.setExtension(otherNumber.getExtension())
        if otherNumber.hasItalianLeadingZero():
            self.setItalianLeadingZero(otherNumber.getItalianLeadingZero)
        if otherNumber.hasRawInput():
            self.setRawInput(otherNumber.getRawInput())
        if otherNumber.hasCountryCodeSource():
            self.setCountryCodeSource(otherNumber.getCountryCodeSource())
        return self

    def exactlySameAs(self, number):
        return (
                self._countryCode == number._countryCode
                and self._nationalNumber == number._nationalNumber
                and self._extension == number._extension
                and self._italianLeadingZero == number._italianLeadingZero
                and self._rawInput == number._rawInput
                and self._countryCodeSource == number._countryCodeSource
                )

    def __str__(self):
        outputString = ''
        outputString += 'Country Code: ' + self._countryCode
        outputString += ' National Number: ' + self._nationalNumber
        if (self.hasItalianLeadingZero() and self.getItalianLeadingZero()):
            outputString += ' Leading Zero: True'
            
        if self.hasExtension():
            outputString += ' Extension: ' + self._extension
            
        if self.hasCountryCodeSource():
            outputString += ' Country Code Source: ' + self._countryCodeSource
        return outputString
