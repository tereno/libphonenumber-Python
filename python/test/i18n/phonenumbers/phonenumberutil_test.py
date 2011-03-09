# Unit tests for phonenumberutil.py
import unittest
from i18n.phonenumbers.phonenumber import *
from i18n.phonenumbers.phonenumberutil import *

class PhoneNumberUtilTest(unittest.TestCase):
    TEST_META_DATA_FILE_PREFIX = "/com/google/i18n/phonenumbers/data/PhoneNumberMetadataProtoForTesting"
    
    TEST_COUNTRY_CODE_TO_REGION_CODE_MAP_CLASS_NAME = "CountryCodeToRegionCodeMapForTesting"

    def __init__(self, name='runTest'):
        unittest.TestCase.__init__(self, name)
        #self.phoneUtil = self.initializePhoneUtilForTesting()
        
    def initializePhoneUtilForTesting(self):
        PhoneNumberUtil.resetInstance()
        return PhoneNumberUtil.getInstance(
            TEST_META_DATA_FILE_PREFIX,
            CountryCodeToRegionCodeMapForTesting.getCountryCodeToRegionCodeMap()
        )
        
    def setUp(self):
        pass
        #super().setUp()

    def tearDown(self):
        pass
        #super().tearDown()

    def assertEquals(self, number1, number2):
        equal = False
        if (number1 is None and number2 is None):
            equal = True
        elif (number1 is not None and number2 is not None):
            equal = number1.exactlySameAs(number2)

        if not equal:
            self.fail("The phone numbers do not match")
            
    def testGetLengthOfGeographicalAreaCode(self):
        number = PhoneNumber()
        # Google MTV, which has area code "650".
        number.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals(3, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # A North America toll-free number, which has no area code.
        number.setCountryCode(1).setNationalNumber(8002530000L)
        self.assertEquals(0, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # An invalid US number (1 digit shorter), which has no area code.
        number.setCountryCode(1).setNationalNumber(650253000L)
        self.assertEquals(0, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # Google London, which has area code "20".
        number.setCountryCode(44).setNationalNumber(2070313000L)
        self.assertEquals(2, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # A UK mobile phone, which has no area code.
        number.setCountryCode(44).setNationalNumber(7123456789L)
        self.assertEquals(0, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # Google Buenos Aires, which has area code "11".
        number.setCountryCode(54).setNationalNumber(1155303000L)
        self.assertEquals(2, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # Google Sydney, which has area code "2".
        number.setCountryCode(61).setNationalNumber(293744000L)
        self.assertEquals(1, phoneUtil.getLengthOfGeographicalAreaCode(number))
    
        # Google Singapore. Singapore has no area code and no national prefix.
        number.setCountryCode(65).setNationalNumber(65218000L)
        self.assertEquals(0, phoneUtil.getLengthOfGeographicalAreaCode(number))

 #==============================================================================
 #   def testGetInstanceLoadUSMetadata(self):
 #       metadata = self.phoneUtil.getMetadataForRegion("US")
 #       self.assertEquals("US", metadata.getId())
 #       self.assertEquals(1, metadata.getCountryCode())
 #       self.assertEquals("011", metadata.getInternationalPrefix())
 #       assertTrue(metadata.hasNationalPrefix())
 #       self.assertEquals(2, metadata.getNumberFormatCount())
 #       self.assertEquals("(\\d{3})(\\d{3})(\\d{4})",
 #                    metadata.getNumberFormat(0).getPattern())
 #       self.assertEquals("$1 $2 $3", metadata.getNumberFormat(0).getFormat())
 #       self.assertEquals("[13-9]\\d{9}|2[0-35-9]\\d{8}",
 #                    metadata.getGeneralDesc().getNationalNumberPattern())
 #       self.assertEquals("\\d{7,10}", metadata.getGeneralDesc().getPossibleNumberPattern())
 #       assertTrue(metadata.getGeneralDesc().exactlySameAs(metadata.getFixedLine()))
 #       self.assertEquals("\\d{10}", metadata.getTollFree().getPossibleNumberPattern())
 #       self.assertEquals("900\\d{7}", metadata.getPremiumRate().getNationalNumberPattern())
 #       # No shared-cost data is available, so it should be initialised to "NA".
 #       self.assertEquals("NA", metadata.getSharedCost().getNationalNumberPattern())
 #       self.assertEquals("NA", metadata.getSharedCost().getPossibleNumberPattern())
 #       
 #   def testGetInstanceLoadDEMetadata(self):
 #       metadata = self.phoneUtil.getMetadataForRegion("DE")
 #       self.assertEquals("DE", metadata.getId())
 #       self.assertEquals(49, metadata.getCountryCode())
 #       self.assertEquals("00", metadata.getInternationalPrefix())
 #       self.assertEquals("0", metadata.getNationalPrefix())
 #       self.assertEquals(5, metadata.getNumberFormatCount())
 #       self.assertEquals(1, metadata.getNumberFormat(4).getLeadingDigitsPatternCount())
 #       self.assertEquals("900", metadata.getNumberFormat(4).getLeadingDigitsPattern(0))
 #       self.assertEquals("(\\d{3})(\\d{3,4})(\\d{4})",
 #                    metadata.getNumberFormat(4).getPattern())
 #       self.assertEquals("$1 $2 $3", metadata.getNumberFormat(4).getFormat())
 #       self.assertEquals("(?:[24-6]\\d{2}|3[03-9]\\d|[789](?:[1-9]\\d|0[2-9]))\\d{3,8}",
 #                    metadata.getFixedLine().getNationalNumberPattern())
 #       self.assertEquals("\\d{2,14}", metadata.getFixedLine().getPossibleNumberPattern())
 #       self.assertEquals("30123456", metadata.getFixedLine().getExampleNumber())
 #       self.assertEquals("\\d{10}", metadata.getTollFree().getPossibleNumberPattern())
 #       self.assertEquals("900([135]\\d{6}|9\\d{7})", metadata.getPremiumRate().getNationalNumberPattern())
 # 
 #   def testGetInstanceLoadARMetadata(self):
 #       metadata = self.phoneUtil.getMetadataForRegion("AR")
 #       self.assertEquals("AR", metadata.getId())
 #       self.assertEquals(54, metadata.getCountryCode())
 #       self.assertEquals("00", metadata.getInternationalPrefix())
 #       self.assertEquals("0", metadata.getNationalPrefix())
 #       self.assertEquals("0(?:(11|343|3715)15)?", metadata.getNationalPrefixForParsing())
 #       self.assertEquals("9$1", metadata.getNationalPrefixTransformRule())
 #       self.assertEquals("$1 15 $2-$3", metadata.getNumberFormat(2).getFormat())
 #       self.assertEquals("9(\\d{4})(\\d{2})(\\d{4})",
 #                    metadata.getNumberFormat(3).getPattern())
 #       self.assertEquals("(9)(\\d{4})(\\d{2})(\\d{4})",
 #                    metadata.getIntlNumberFormat(3).getPattern())
 #       self.assertEquals("$1 $2 $3 $4", metadata.getIntlNumberFormat(3).getFormat())
 #==============================================================================

    def testGetNationalSignificantNumber(self):
        number = PhoneNumber()
        number.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals("6502530000", PhoneNumberUtil.getNationalSignificantNumber(number))
    
        # An Italian mobile number.
        number.setCountryCode(39).setNationalNumber(312345678L)
        self.assertEquals("312345678", PhoneNumberUtil.getNationalSignificantNumber(number))
    
        # An Italian fixed line number.
        number.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        self.assertEquals("0236618300", PhoneNumberUtil.getNationalSignificantNumber(number))

    def testGetExampleNumber(self):
        deNumber = PhoneNumber()
        deNumber.setCountryCode(49).setNationalNumber(30123456)
        self.assertEquals(deNumber, phoneUtil.getExampleNumber("DE"))
        self.assertEquals(deNumber, phoneUtil.getExampleNumber("de"))
    
        self.assertEquals(deNumber,
                     phoneUtil.getExampleNumberForType("DE",
                                                       PhoneNumberUtil.PhoneNumberType.FIXED_LINE))
        self.assertEquals(null,
                     phoneUtil.getExampleNumberForType("DE",
                                                       PhoneNumberUtil.PhoneNumberType.MOBILE))
        # For the US, the example number is placed under general description, and hence should be used
        # for both fixed line and mobile, so neither of these should return null.
        self.assertNotNull(phoneUtil.getExampleNumberForType("US",
                                                        PhoneNumberUtil.PhoneNumberType.FIXED_LINE))
        self.assertNotNull(phoneUtil.getExampleNumberForType("US",
                                                        PhoneNumberUtil.PhoneNumberType.MOBILE))

    def testNormaliseRemovePunctuation(self):
        inputNumber = "034-56&+#234"
        expectedOutput = "03456234"
        self.assertEquals("Conversion did not correctly remove punctuation",
                     expectedOutput,
                     PhoneNumberUtil.normalize(inputNumber))

    def testNormaliseReplaceAlphaCharacters(self):
        inputNumber = "034-I-am-HUNGRY"
        expectedOutput = "034426486479"
        self.assertEquals("Conversion did not correctly replace alpha characters",
                     expectedOutput,
                     PhoneNumberUtil.normalize(inputNumber))

    def testNormaliseOtherDigits(self):
        inputNumber = "\uFF125\u0665"
        expectedOutput = "255"
        self.assertEquals("Conversion did not correctly replace non-latin digits",
                     expectedOutput,
                     PhoneNumberUtil.normalize(inputNumber))

    def testNormaliseStripAlphaCharacters(self):
        inputNumber = "034-56&+a#234"
        expectedOutput = "03456234"
        self.assertEquals("Conversion did not correctly remove alpha character",
                     expectedOutput,
                     PhoneNumberUtil.normalizeDigitsOnly(inputNumber))

    def testFormatUSNumber(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals("650 253 0000", phoneUtil.format(usNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+1 650 253 0000", phoneUtil.format(usNumber, PhoneNumberFormat.INTERNATIONAL))
    
        usNumber.clear()
        usNumber.setCountryCode(1).setNationalNumber(8002530000L)
        self.assertEquals("800 253 0000", phoneUtil.format(usNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+1 800 253 0000", phoneUtil.format(usNumber, PhoneNumberFormat.INTERNATIONAL))
    
        usNumber.clear()
        usNumber.setCountryCode(1).setNationalNumber(9002530000L)
        self.assertEquals("900 253 0000", phoneUtil.format(usNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+1 900 253 0000", phoneUtil.format(usNumber, PhoneNumberFormat.INTERNATIONAL))

    def testFormatBSNumber(self):
        bsNumber = PhoneNumber()
        bsNumber.setCountryCode(1).setNationalNumber(2421234567L)
        self.assertEquals("242 123 4567", phoneUtil.format(bsNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+1 242 123 4567", phoneUtil.format(bsNumber, PhoneNumberFormat.INTERNATIONAL))
    
        bsNumber.clear()
        bsNumber.setCountryCode(1).setNationalNumber(8002530000L)
        self.assertEquals("800 253 0000", phoneUtil.format(bsNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+1 800 253 0000", phoneUtil.format(bsNumber, PhoneNumberFormat.INTERNATIONAL))
    
        bsNumber.clear()
        bsNumber.setCountryCode(1).setNationalNumber(9002530000L)
        self.assertEquals("900 253 0000", phoneUtil.format(bsNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+1 900 253 0000", phoneUtil.format(bsNumber, PhoneNumberFormat.INTERNATIONAL))


    def testFormatGBNumber(self):
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(2087389353L)
        self.assertEquals("(020) 8738 9353", phoneUtil.format(gbNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+44 20 8738 9353", phoneUtil.format(gbNumber, PhoneNumberFormat.INTERNATIONAL))
    
        gbNumber.clear()
        gbNumber.setCountryCode(44).setNationalNumber(7912345678L)
        self.assertEquals("(07912) 345 678", phoneUtil.format(gbNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+44 7912 345 678", phoneUtil.format(gbNumber, PhoneNumberFormat.INTERNATIONAL))
    
    
    def testFormatDENumber(self):
        deNumber = PhoneNumber()
        deNumber.setCountryCode(49).setNationalNumber(301234L)
        self.assertEquals("030 1234", phoneUtil.format(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+49 30 1234", phoneUtil.format(deNumber, PhoneNumberFormat.INTERNATIONAL))
    
        deNumber.clear()
        deNumber.setCountryCode(49).setNationalNumber(291123L)
        self.assertEquals("0291 123", phoneUtil.format(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+49 291 123", phoneUtil.format(deNumber, PhoneNumberFormat.INTERNATIONAL))
    
        deNumber.clear()
        deNumber.setCountryCode(49).setNationalNumber(29112345678L)
        self.assertEquals("0291 12345678", phoneUtil.format(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+49 291 12345678", phoneUtil.format(deNumber, PhoneNumberFormat.INTERNATIONAL))
    
        deNumber.clear()
        deNumber.setCountryCode(49).setNationalNumber(9123123L)
        self.assertEquals("09123 123", phoneUtil.format(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+49 9123 123", phoneUtil.format(deNumber, PhoneNumberFormat.INTERNATIONAL))
        deNumber.clear()
        deNumber.setCountryCode(49).setNationalNumber(80212345L)
        self.assertEquals("08021 2345", phoneUtil.format(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+49 8021 2345", phoneUtil.format(deNumber, PhoneNumberFormat.INTERNATIONAL))
        deNumber.clear()
        deNumber.setCountryCode(49).setNationalNumber(1234L)
        # Note this number is correctly formatted without national prefix. Most of the numbers that
        # are treated as invalid numbers by the library are short numbers, and they are usually not
        # dialed with national prefix.
        self.assertEquals("1234", phoneUtil.format(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+49 1234", phoneUtil.format(deNumber, PhoneNumberFormat.INTERNATIONAL))
    
    
    def testFormatITNumber(self):
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        self.assertEquals("02 3661 8300", phoneUtil.format(itNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+39 02 3661 8300", phoneUtil.format(itNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+390236618300", phoneUtil.format(itNumber, PhoneNumberFormat.E164))
    
        itNumber.clear()
        itNumber.setCountryCode(39).setNationalNumber(345678901L)
        self.assertEquals("345 678 901", phoneUtil.format(itNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+39 345 678 901", phoneUtil.format(itNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+39345678901", phoneUtil.format(itNumber, PhoneNumberFormat.E164))
    
    
    def testFormatAUNumber(self):
        auNumber = PhoneNumber()
        auNumber.setCountryCode(61).setNationalNumber(236618300L)
        self.assertEquals("02 3661 8300", phoneUtil.format(auNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+61 2 3661 8300", phoneUtil.format(auNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+61236618300", phoneUtil.format(auNumber, PhoneNumberFormat.E164))
    
        auNumber.clear()
        auNumber.setCountryCode(61).setNationalNumber(1800123456L)
        self.assertEquals("1800 123 456", phoneUtil.format(auNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+61 1800 123 456", phoneUtil.format(auNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+611800123456", phoneUtil.format(auNumber, PhoneNumberFormat.E164))
    
    
    def testFormatARNumber(self):
        arNumber = PhoneNumber()
        arNumber.setCountryCode(54).setNationalNumber(1187654321L)
        self.assertEquals("011 8765-4321", phoneUtil.format(arNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+54 11 8765-4321", phoneUtil.format(arNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+541187654321", phoneUtil.format(arNumber, PhoneNumberFormat.E164))
    
        arNumber.clear()
        arNumber.setCountryCode(54).setNationalNumber(91187654321L)
        self.assertEquals("011 15 8765-4321", phoneUtil.format(arNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("+54 9 11 8765 4321", phoneUtil.format(arNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+5491187654321", phoneUtil.format(arNumber, PhoneNumberFormat.E164))
    
    
    def testFormatOutOfCountryCallingNumber(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(9002530000L)
        self.assertEquals("00 1 900 253 0000",
                     phoneUtil.formatOutOfCountryCallingNumber(usNumber, "DE"))
    
        usNumber.clear()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals("1 650 253 0000",
                     phoneUtil.formatOutOfCountryCallingNumber(usNumber, "BS"))
    
        self.assertEquals("0~0 1 650 253 0000",
                     phoneUtil.formatOutOfCountryCallingNumber(usNumber, "PL"))
    
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(7912345678L)
        self.assertEquals("011 44 7912 345 678",
                     phoneUtil.formatOutOfCountryCallingNumber(gbNumber, "US"))
    
        deNumber = PhoneNumber()
        deNumber.setCountryCode(49).setNationalNumber(1234L)
        self.assertEquals("00 49 1234",
                     phoneUtil.formatOutOfCountryCallingNumber(deNumber, "GB"))
        # Note this number is correctly formatted without national prefix. Most of the numbers that
        # are treated as invalid numbers by the library are short numbers, and they are usually not
        # dialed with national prefix.
        self.assertEquals("1234",
                     phoneUtil.formatOutOfCountryCallingNumber(deNumber, "DE"))
    
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        self.assertEquals("011 39 02 3661 8300",
                     phoneUtil.formatOutOfCountryCallingNumber(itNumber, "US"))
        self.assertEquals("02 3661 8300",
                     phoneUtil.formatOutOfCountryCallingNumber(itNumber, "IT"))
        self.assertEquals("+39 02 3661 8300",
                     phoneUtil.formatOutOfCountryCallingNumber(itNumber, "SG"))
    
        sgNumber = PhoneNumber()
        sgNumber.setCountryCode(65).setNationalNumber(94777892L)
        self.assertEquals("9477 7892",
                     phoneUtil.formatOutOfCountryCallingNumber(sgNumber, "SG"))
    
        arNumber = PhoneNumber()
        arNumber.setCountryCode(54).setNationalNumber(91187654321L)
        self.assertEquals("011 54 9 11 8765 4321",
                     phoneUtil.formatOutOfCountryCallingNumber(arNumber, "US"))
    
        arNumber.setExtension("1234")
        self.assertEquals("011 54 9 11 8765 4321 ext. 1234",
                     phoneUtil.formatOutOfCountryCallingNumber(arNumber, "US"))
        self.assertEquals("0011 54 9 11 8765 4321 ext. 1234",
                     phoneUtil.formatOutOfCountryCallingNumber(arNumber, "AU"))
        self.assertEquals("011 15 8765-4321 ext. 1234",
                     phoneUtil.formatOutOfCountryCallingNumber(arNumber, "AR"))
        self.assertEquals("011 15 8765-4321 ext. 1234",
                     phoneUtil.formatOutOfCountryCallingNumber(arNumber, "ar"))
    
    
    def testFormatOutOfCountryWithPreferredIntlPrefix(self):
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        # This should use 0011, since that is the preferred international prefix (both 0011 and 0012
        # are accepted as possible international prefixes in our test metadta.)
        self.assertEquals("0011 39 02 3661 8300",
                     phoneUtil.formatOutOfCountryCallingNumber(itNumber, "AU"))
    
    
    def testFormatWithCarrierCode(self):
        # We only support this for AR in our test metadata.
        arNumber = PhoneNumber()
        arNumber.setCountryCode(54).setNationalNumber(91234125678L)
        self.assertEquals("01234 12-5678", phoneUtil.format(arNumber, PhoneNumberFormat.NATIONAL))
        # Test formatting with a carrier code.
        self.assertEquals("01234 15 12-5678", phoneUtil.formatNationalNumberWithCarrierCode(arNumber, "15"))
        # Here the international rule is used, so no carrier code should be present.
        self.assertEquals("+5491234125678", phoneUtil.format(arNumber, PhoneNumberFormat.E164))
        # We don't support this for the US so there should be no change.
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(4241231234L)
        self.assertEquals("424 123 1234", phoneUtil.format(usNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals("424 123 1234", phoneUtil.formatNationalNumberWithCarrierCode(usNumber, "15"))
    
    
    def testFormatByPattern(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
    
        newNumFormat = NumberFormat()
        newNumFormat.setPattern("(\\d{3})(\\d{3})(\\d{4})")
        newNumFormat.setFormat("($1) $2-$3")
        newNumberFormats = []
        newNumberFormats.append(newNumFormat)
    
        self.assertEquals("(650) 253-0000", phoneUtil.formatByPattern(usNumber, PhoneNumberFormat.NATIONAL,
                                                                 newNumberFormats))
        self.assertEquals("+1 (650) 253-0000", phoneUtil.formatByPattern(usNumber,
                                                                    PhoneNumberFormat.INTERNATIONAL,
                                                                    newNumberFormats))
    
        # $NP is set to '1' for the US. Here we check that for other NANPA countries the US rules are
        # followed.
        newNumFormat.setNationalPrefixFormattingRule("$NP ($FG)")
        newNumFormat.setFormat("$1 $2-$3")
        bsNumber = PhoneNumber()
        bsNumber.setCountryCode(1).setNationalNumber(4168819999L)
        self.assertEquals("1 (416) 881-9999",
                     phoneUtil.formatByPattern(bsNumber, PhoneNumberFormat.NATIONAL, newNumberFormats))
        self.assertEquals("+1 416 881-9999",
                     phoneUtil.formatByPattern(bsNumber, PhoneNumberFormat.INTERNATIONAL,
                                               newNumberFormats))
    
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
    
        newNumFormat.setPattern("(\\d{2})(\\d{5})(\\d{3})")
        newNumFormat.setFormat("$1-$2 $3")
        newNumberFormats.set(0, newNumFormat)
    
        self.assertEquals("02-36618 300",
                     phoneUtil.formatByPattern(itNumber, PhoneNumberFormat.NATIONAL, newNumberFormats))
        self.assertEquals("+39 02-36618 300",
                     phoneUtil.formatByPattern(itNumber, PhoneNumberFormat.INTERNATIONAL,
                                               newNumberFormats))
    
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(2012345678L)
    
        newNumFormat.setNationalPrefixFormattingRule("$NP$FG")
        newNumFormat.setPattern("(\\d{2})(\\d{4})(\\d{4})")
        newNumFormat.setFormat("$1 $2 $3")
        newNumberFormats.set(0, newNumFormat)
        self.assertEquals("020 1234 5678",
                     phoneUtil.formatByPattern(gbNumber, PhoneNumberFormat.NATIONAL, newNumberFormats))
    
        newNumFormat.setNationalPrefixFormattingRule("($NP$FG)")
        self.assertEquals("(020) 1234 5678",
                     phoneUtil.formatByPattern(gbNumber, PhoneNumberFormat.NATIONAL, newNumberFormats))
    
        newNumFormat.setNationalPrefixFormattingRule("")
        self.assertEquals("20 1234 5678",
                     phoneUtil.formatByPattern(gbNumber, PhoneNumberFormat.NATIONAL, newNumberFormats))
    
        newNumFormat.setNationalPrefixFormattingRule("")
        self.assertEquals("+44 20 1234 5678",
                     phoneUtil.formatByPattern(gbNumber, PhoneNumberFormat.INTERNATIONAL,
                                               newNumberFormats))
    
    
    def testFormatE164Number(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals("+16502530000", phoneUtil.format(usNumber, PhoneNumberFormat.E164))
        deNumber = PhoneNumber()
        deNumber.setCountryCode(49).setNationalNumber(301234L)
        self.assertEquals("+49301234", phoneUtil.format(deNumber, PhoneNumberFormat.E164))
    
    
    def testFormatNumberWithExtension(self):
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(33316005L).setExtension("1234")
        # Uses default extension prefix:
        self.assertEquals("03-331 6005 ext. 1234", phoneUtil.format(nzNumber, PhoneNumberFormat.NATIONAL))
        # Extension prefix overridden in the territory information for the US:
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L).setExtension("4567")
        self.assertEquals("650 253 0000 extn. 4567", phoneUtil.format(usNumber, PhoneNumberFormat.NATIONAL))
    
    
    def testFormatUsingOriginalNumberFormat(self):
        number1 = phoneUtil.parseAndKeepRawInput("+442087654321", "GB")
        self.assertEquals("+44 20 8765 4321", phoneUtil.formatInOriginalFormat(number1, "GB"))
    
        number2 = phoneUtil.parseAndKeepRawInput("02087654321", "GB")
        self.assertEquals("(020) 8765 4321", phoneUtil.formatInOriginalFormat(number2, "GB"))
    
        number3 = phoneUtil.parseAndKeepRawInput("011442087654321", "US")
        self.assertEquals("011 44 20 8765 4321", phoneUtil.formatInOriginalFormat(number3, "US"))
    
        number4 = phoneUtil.parseAndKeepRawInput("442087654321", "GB")
        self.assertEquals("44 20 8765 4321", phoneUtil.formatInOriginalFormat(number4, "GB"))
    
        number5 = phoneUtil.parse("+442087654321", "GB")
        self.assertEquals("(020) 8765 4321", phoneUtil.formatInOriginalFormat(number5, "GB"))
    
    
    def testIsPremiumRate(self):
        premiumRateNumber = PhoneNumber()
    
        premiumRateNumber.setCountryCode(1).setNationalNumber(9004433030L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.PREMIUM_RATE,
                     phoneUtil.getNumberType(premiumRateNumber))
    
        premiumRateNumber.clear()
        premiumRateNumber.setCountryCode(39).setNationalNumber(892123L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.PREMIUM_RATE,
                     phoneUtil.getNumberType(premiumRateNumber))
    
        premiumRateNumber.clear()
        premiumRateNumber.setCountryCode(44).setNationalNumber(9187654321L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.PREMIUM_RATE,
                     phoneUtil.getNumberType(premiumRateNumber))
    
        premiumRateNumber.clear()
        premiumRateNumber.setCountryCode(49).setNationalNumber(9001654321L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.PREMIUM_RATE,
                     phoneUtil.getNumberType(premiumRateNumber))
    
        premiumRateNumber.clear()
        premiumRateNumber.setCountryCode(49).setNationalNumber(90091234567L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.PREMIUM_RATE,
                     phoneUtil.getNumberType(premiumRateNumber))
    
    
    def testIsTollFree(self):
        tollFreeNumber = PhoneNumber()
    
        tollFreeNumber.setCountryCode(1).setNationalNumber(8881234567L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.TOLL_FREE,
                     phoneUtil.getNumberType(tollFreeNumber))
    
        tollFreeNumber.clear()
        tollFreeNumber.setCountryCode(39).setNationalNumber(803123L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.TOLL_FREE,
                     phoneUtil.getNumberType(tollFreeNumber))
    
        tollFreeNumber.clear()
        tollFreeNumber.setCountryCode(44).setNationalNumber(8012345678L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.TOLL_FREE,
                     phoneUtil.getNumberType(tollFreeNumber))
    
        tollFreeNumber.clear()
        tollFreeNumber.setCountryCode(49).setNationalNumber(8001234567L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.TOLL_FREE,
                     phoneUtil.getNumberType(tollFreeNumber))
    
    
    def testIsMobile(self):
        mobileNumber = PhoneNumber()
    
        # A Bahama mobile number
        mobileNumber.setCountryCode(1).setNationalNumber(2423570000L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.MOBILE,
                     phoneUtil.getNumberType(mobileNumber))
    
        mobileNumber.clear()
        mobileNumber.setCountryCode(39).setNationalNumber(312345678L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.MOBILE,
                     phoneUtil.getNumberType(mobileNumber))
    
        mobileNumber.clear()
        mobileNumber.setCountryCode(44).setNationalNumber(7912345678L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.MOBILE,
                     phoneUtil.getNumberType(mobileNumber))
    
        mobileNumber.clear()
        mobileNumber.setCountryCode(49).setNationalNumber(15123456789L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.MOBILE,
                     phoneUtil.getNumberType(mobileNumber))
    
        mobileNumber.clear()
        mobileNumber.setCountryCode(54).setNationalNumber(91187654321L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.MOBILE,
                     phoneUtil.getNumberType(mobileNumber))
    
    
    def testIsFixedLine(self):
        fixedLineNumber = PhoneNumber()
    
        # A Bahama fixed-line number
        fixedLineNumber.setCountryCode(1).setNationalNumber(2423651234L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.FIXED_LINE,
                     phoneUtil.getNumberType(fixedLineNumber))
    
        # An Italian fixed-line number
        fixedLineNumber.clear()
        fixedLineNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.FIXED_LINE,
                     phoneUtil.getNumberType(fixedLineNumber))
    
        fixedLineNumber.clear()
        fixedLineNumber.setCountryCode(44).setNationalNumber(2012345678L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.FIXED_LINE,
                     phoneUtil.getNumberType(fixedLineNumber))
    
        fixedLineNumber.clear()
        fixedLineNumber.setCountryCode(49).setNationalNumber(301234L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.FIXED_LINE,
                     phoneUtil.getNumberType(fixedLineNumber))
    
    
    def testIsFixedLineAndMobile(self):
        fixedLineAndMobileNumber = PhoneNumber()
        fixedLineAndMobileNumber.setCountryCode(1).setNationalNumber(6502531111L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.FIXED_LINE_OR_MOBILE,
                     phoneUtil.getNumberType(fixedLineAndMobileNumber))
    
        fixedLineAndMobileNumber.clear()
        fixedLineAndMobileNumber.setCountryCode(54).setNationalNumber(1987654321L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.FIXED_LINE_OR_MOBILE,
                     phoneUtil.getNumberType(fixedLineAndMobileNumber))
    
    
    def testIsSharedCost(self):
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(8431231234L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.SHARED_COST, phoneUtil.getNumberType(gbNumber))
    
    
    def testIsVoip(self):
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(5631231234L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.VOIP, phoneUtil.getNumberType(gbNumber))
    
    
    def testIsPersonalNumber(self):
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(7031231234L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.PERSONAL_NUMBER,
                     phoneUtil.getNumberType(gbNumber))
    
    
    def testIsUnknown(self):
        unknownNumber = PhoneNumber()
        unknownNumber.setCountryCode(1).setNationalNumber(65025311111L)
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.UNKNOWN,
                     phoneUtil.getNumberType(unknownNumber))
    
    
    def testIsValidNumber(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
        assertTrue(phoneUtil.isValidNumber(usNumber))
    
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        assertTrue(phoneUtil.isValidNumber(itNumber))
    
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(7912345678L)
        assertTrue(phoneUtil.isValidNumber(gbNumber))
    
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(21387835L)
        assertTrue(phoneUtil.isValidNumber(nzNumber))
    
    
    def testIsValidForRegion(self):
        # This number is valid for the Bahamas, but is not a valid US number.
        bsNumber = PhoneNumber()
        bsNumber.setCountryCode(1).setNationalNumber(2423232345L)
        assertTrue(phoneUtil.isValidNumber(bsNumber))
        assertTrue(phoneUtil.isValidNumberForRegion(bsNumber, "BS"))
        assertTrue(phoneUtil.isValidNumberForRegion(bsNumber, "bs"))
        assertFalse(phoneUtil.isValidNumberForRegion(bsNumber, "US"))
        bsNumber.setNationalNumber(2421232345L)
        # This number is no longer valid.
        assertFalse(phoneUtil.isValidNumber(bsNumber))
    
        # La Mayotte and Reunion use 'leadingDigits' to differentiate them.
        reNumber = PhoneNumber()
        reNumber.setCountryCode(262).setNationalNumber(262123456L)
        assertTrue(phoneUtil.isValidNumber(reNumber))
        assertTrue(phoneUtil.isValidNumberForRegion(reNumber, "RE"))
        assertFalse(phoneUtil.isValidNumberForRegion(reNumber, "YT"))
        # Now change the number to be a number for La Mayotte.
        reNumber.setNationalNumber(269601234L)
        assertTrue(phoneUtil.isValidNumberForRegion(reNumber, "YT"))
        assertFalse(phoneUtil.isValidNumberForRegion(reNumber, "RE"))
        # This number is no longer valid for La Reunion.
        reNumber.setNationalNumber(269123456L)
        assertFalse(phoneUtil.isValidNumberForRegion(reNumber, "YT"))
        assertFalse(phoneUtil.isValidNumberForRegion(reNumber, "RE"))
        assertFalse(phoneUtil.isValidNumber(reNumber))
        # However, it should be recognised as from La Mayotte, since it is valid for this region.
        self.assertEquals("YT", phoneUtil.getRegionCodeForNumber(reNumber))
        # This number is valid in both places.
        reNumber.setNationalNumber(800123456L)
        assertTrue(phoneUtil.isValidNumberForRegion(reNumber, "YT"))
        assertTrue(phoneUtil.isValidNumberForRegion(reNumber, "RE"))
    
    
    def testIsNotValidNumber(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(2530000L)
        assertFalse(phoneUtil.isValidNumber(usNumber))
    
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(23661830000L).setItalianLeadingZero(true)
        assertFalse(phoneUtil.isValidNumber(itNumber))
    
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(791234567L)
        assertFalse(phoneUtil.isValidNumber(gbNumber))
    
        deNumber = PhoneNumber()
        deNumber.setCountryCode(49).setNationalNumber(1234L)
        assertFalse(phoneUtil.isValidNumber(deNumber))
    
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(3316005L)
        assertFalse(phoneUtil.isValidNumber(nzNumber))
    
    def testGetRegionCodeForCountryCode(self):
        self.assertEquals("US", phoneUtil.getRegionCodeForCountryCode(1))
        self.assertEquals("GB", phoneUtil.getRegionCodeForCountryCode(44))
        self.assertEquals("DE", phoneUtil.getRegionCodeForCountryCode(49))
    
    
    def testGetRegionCodeForNumber(self):
        bsNumber = PhoneNumber()
        bsNumber.setCountryCode(1).setNationalNumber(2423027000L)
        self.assertEquals("BS", phoneUtil.getRegionCodeForNumber(bsNumber))
    
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals("US", phoneUtil.getRegionCodeForNumber(usNumber))
    
        gbNumber = PhoneNumber()
        gbNumber.setCountryCode(44).setNationalNumber(7912345678L)
        self.assertEquals("GB", phoneUtil.getRegionCodeForNumber(gbNumber))
    
    
    def testGetCountryCodeForRegion(self):
        self.assertEquals(1, phoneUtil.getCountryCodeForRegion("US"))
        self.assertEquals(64, phoneUtil.getCountryCodeForRegion("NZ"))
        self.assertEquals(64, phoneUtil.getCountryCodeForRegion("nz"))
        self.assertEquals(0, phoneUtil.getCountryCodeForRegion(null))
        self.assertEquals(0, phoneUtil.getCountryCodeForRegion("ZZ"))
        # CS is already deprecated so the library doesn't support it.
        self.assertEquals(0, phoneUtil.getCountryCodeForRegion("CS"))
    
    
    #@SuppressWarnings("deprecation")
    def testGetNationalDiallingPrefixForRegion(self):
        self.assertEquals("1", phoneUtil.getNddPrefixForRegion("US", false))
        # Test non-main country to see it gets the national dialling prefix for the main country with
        # that country calling code.
        self.assertEquals("1", phoneUtil.getNddPrefixForRegion("BS", false))
        self.assertEquals("0", phoneUtil.getNddPrefixForRegion("NZ", false))
        # Test case with non digit in the national prefix.
        self.assertEquals("0~0", phoneUtil.getNddPrefixForRegion("AO", false))
        self.assertEquals("00", phoneUtil.getNddPrefixForRegion("AO", true))
        # Test cases with invalid regions.
        self.assertEquals(null, phoneUtil.getNddPrefixForRegion(null, false))
        self.assertEquals(null, phoneUtil.getNddPrefixForRegion("ZZ", false))
        # CS is already deprecated so the library doesn't support it.
        self.assertEquals(null, phoneUtil.getNddPrefixForRegion("CS", false))
    
    
    def testIsNANPACountry(self):
        assertTrue(phoneUtil.isNANPACountry("US"))
        assertTrue(phoneUtil.isNANPACountry("BS"))
        assertTrue(phoneUtil.isNANPACountry("bs"))
    
    
    def testIsPossibleNumber(self):
        number = PhoneNumber()
        number.setCountryCode(1).setNationalNumber(6502530000L)
        assertTrue(phoneUtil.isPossibleNumber(number))
    
        number.clear()
        number.setCountryCode(1).setNationalNumber(2530000L)
        assertTrue(phoneUtil.isPossibleNumber(number))
    
        number.clear()
        number.setCountryCode(44).setNationalNumber(2070313000L)
        assertTrue(phoneUtil.isPossibleNumber(number))
    
        assertTrue(phoneUtil.isPossibleNumber("+1 650 253 0000", "US"))
        assertTrue(phoneUtil.isPossibleNumber("+1 650 GOO OGLE", "US"))
        assertTrue(phoneUtil.isPossibleNumber("(650) 253-0000", "US"))
        assertTrue(phoneUtil.isPossibleNumber("253-0000", "US"))
        assertTrue(phoneUtil.isPossibleNumber("+1 650 253 0000", "GB"))
        assertTrue(phoneUtil.isPossibleNumber("+44 20 7031 3000", "GB"))
        assertTrue(phoneUtil.isPossibleNumber("(020) 7031 3000", "GB"))
        assertTrue(phoneUtil.isPossibleNumber("7031 3000", "GB"))
        assertTrue(phoneUtil.isPossibleNumber("3331 6005", "NZ"))
        assertTrue(phoneUtil.isPossibleNumber("3331 6005", "nz"))
    
    
    def testIsPossibleNumberWithReason(self):
        # FYI, national numbers for country code +1 that are within 7 to 10 digits are possible.
        number = PhoneNumber()
        number.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.IS_POSSIBLE,
                     phoneUtil.isPossibleNumberWithReason(number))
    
        number.clear()
        number.setCountryCode(1).setNationalNumber(2530000L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.IS_POSSIBLE,
                     phoneUtil.isPossibleNumberWithReason(number))
    
        number.clear()
        number.setCountryCode(0).setNationalNumber(2530000L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.INVALID_COUNTRY_CODE,
                     phoneUtil.isPossibleNumberWithReason(number))
    
        number.clear()
        number.setCountryCode(1).setNationalNumber(253000L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.TOO_SHORT,
                     phoneUtil.isPossibleNumberWithReason(number))
    
        number.clear()
        number.setCountryCode(1).setNationalNumber(65025300000L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.TOO_LONG,
                     phoneUtil.isPossibleNumberWithReason(number))
    
        # Try with number that we don't have metadata for.
        adNumber = PhoneNumber()
        adNumber.setCountryCode(376).setNationalNumber(12345L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.IS_POSSIBLE,
                     phoneUtil.isPossibleNumberWithReason(adNumber))
        adNumber.setCountryCode(376).setNationalNumber(13L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.TOO_SHORT,
                     phoneUtil.isPossibleNumberWithReason(adNumber))
        adNumber.setCountryCode(376).setNationalNumber(1234567890123456L)
        self.assertEquals(PhoneNumberUtil.ValidationResult.TOO_LONG,
                     phoneUtil.isPossibleNumberWithReason(adNumber))
    
    
    def testIsNotPossibleNumber(self):
        number = PhoneNumber()
        number.setCountryCode(1).setNationalNumber(65025300000L)
        assertFalse(phoneUtil.isPossibleNumber(number))
    
        number.clear()
        number.setCountryCode(1).setNationalNumber(253000L)
        assertFalse(phoneUtil.isPossibleNumber(number))
    
        number.clear()
        number.setCountryCode(44).setNationalNumber(300L)
        assertFalse(phoneUtil.isPossibleNumber(number))
    
        assertFalse(phoneUtil.isPossibleNumber("+1 650 253 00000", "US"))
        assertFalse(phoneUtil.isPossibleNumber("(650) 253-00000", "US"))
        assertFalse(phoneUtil.isPossibleNumber("I want a Pizza", "US"))
        assertFalse(phoneUtil.isPossibleNumber("253-000", "US"))
        assertFalse(phoneUtil.isPossibleNumber("1 3000", "GB"))
        assertFalse(phoneUtil.isPossibleNumber("+44 300", "GB"))
    
    
    def testTruncateTooLongNumber(self):
        # US number 650-253-0000, but entered with one additional digit at the end.
        tooLongNumber = PhoneNumber()
        tooLongNumber.setCountryCode(1).setNationalNumber(65025300001L)
        validNumber = PhoneNumber()
        validNumber.setCountryCode(1).setNationalNumber(6502530000L)
        assertTrue(phoneUtil.truncateTooLongNumber(tooLongNumber))
        self.assertEquals(validNumber, tooLongNumber)
    
        # GB number 080 1234 5678, but entered with 4 extra digits at the end.
        tooLongNumber.clear()
        tooLongNumber.setCountryCode(44).setNationalNumber(80123456780123L)
        validNumber.clear()
        validNumber.setCountryCode(44).setNationalNumber(8012345678L)
        assertTrue(phoneUtil.truncateTooLongNumber(tooLongNumber))
        self.assertEquals(validNumber, tooLongNumber)
    
        # IT number 022 3456 7890, but entered with 3 extra digits at the end.
        tooLongNumber.clear()
        tooLongNumber.setCountryCode(39).setNationalNumber(2234567890123L).setItalianLeadingZero(true)
        validNumber.clear()
        validNumber.setCountryCode(39).setNationalNumber(2234567890L).setItalianLeadingZero(true)
        assertTrue(phoneUtil.truncateTooLongNumber(tooLongNumber))
        self.assertEquals(validNumber, tooLongNumber)
    
        # Tests what happens when a valid number is passed in.
        validNumberCopy = PhoneNumber()
        validNumberCopy.mergeFrom(validNumber)
        assertTrue(phoneUtil.truncateTooLongNumber(validNumber))
        # Tests the number is not modified.
        self.assertEquals(validNumberCopy, validNumber)
    
        # Tests what happens when a number with invalid prefix is passed in.
        numberWithInvalidPrefix = PhoneNumber()
        # The test metadata says US numbers cannot have prefix 240.
        numberWithInvalidPrefix.setCountryCode(1).setNationalNumber(2401234567L)
        invalidNumberCopy = PhoneNumber()
        invalidNumberCopy.mergeFrom(numberWithInvalidPrefix)
        assertFalse(phoneUtil.truncateTooLongNumber(numberWithInvalidPrefix))
        # Tests the number is not modified.
        self.assertEquals(invalidNumberCopy, numberWithInvalidPrefix)
    
        # Tests what happens when a too short number is passed in.
        tooShortNumber = PhoneNumber()
        tooShortNumber.setCountryCode(1).setNationalNumber(1234L)
        tooShortNumberCopy = PhoneNumber()
        tooShortNumberCopy.mergeFrom(tooShortNumber)
        assertFalse(phoneUtil.truncateTooLongNumber(tooShortNumber))
        # Tests the number is not modified.
        self.assertEquals(tooShortNumberCopy, tooShortNumber)
    
    
    def testIsViablePhoneNumber(self):
        # Only one or two digits before strange non-possible punctuation.
        assertFalse(PhoneNumberUtil.isViablePhoneNumber("12. March"))
        assertFalse(PhoneNumberUtil.isViablePhoneNumber("1+1+1"))
        assertFalse(PhoneNumberUtil.isViablePhoneNumber("80+0"))
        assertFalse(PhoneNumberUtil.isViablePhoneNumber("00"))
        # Three digits is viable.
        assertTrue(PhoneNumberUtil.isViablePhoneNumber("111"))
        # Alpha numbers.
        assertTrue(PhoneNumberUtil.isViablePhoneNumber("0800-4-pizza"))
        assertTrue(PhoneNumberUtil.isViablePhoneNumber("0800-4-PIZZA"))
        # Only one or two digits before possible punctuation followed by more digits.
        assertTrue(PhoneNumberUtil.isViablePhoneNumber("1\u300034"))
        assertFalse(PhoneNumberUtil.isViablePhoneNumber("1\u30003+4"))
        # Unicode variants of possible starting character and other allowed punctuation/digits.
        assertTrue(PhoneNumberUtil.isViablePhoneNumber("\uFF081\uFF09\u30003456789"))
        # Testing a leading + is okay.
        assertTrue(PhoneNumberUtil.isViablePhoneNumber("+1\uFF09\u30003456789"))
    
    
    def testExtractPossibleNumber(self):
        # Removes preceding funky punctuation and letters but leaves the rest untouched.
        self.assertEquals("0800-345-600", PhoneNumberUtil.extractPossibleNumber("Tel:0800-345-600"))
        self.assertEquals("0800 FOR PIZZA", PhoneNumberUtil.extractPossibleNumber("Tel:0800 FOR PIZZA"))
        # Should not remove plus sign
        self.assertEquals("+800-345-600", PhoneNumberUtil.extractPossibleNumber("Tel:+800-345-600"))
        # Should recognise wide digits as possible start values.
        self.assertEquals("\uFF10\uFF12\uFF13",
                     PhoneNumberUtil.extractPossibleNumber("\uFF10\uFF12\uFF13"))
        # Dashes are not possible start values and should be removed.
        self.assertEquals("\uFF11\uFF12\uFF13",
                     PhoneNumberUtil.extractPossibleNumber("Num-\uFF11\uFF12\uFF13"))
        # If not possible number present, return empty string.
        self.assertEquals("", PhoneNumberUtil.extractPossibleNumber("Num-...."))
        # Leading brackets are stripped - these are not used when parsing.
        self.assertEquals("650) 253-0000", PhoneNumberUtil.extractPossibleNumber("(650) 253-0000"))
    
        # Trailing non-alpha-numeric characters should be removed.
        self.assertEquals("650) 253-0000", PhoneNumberUtil.extractPossibleNumber("(650) 253-0000..- .."))
        self.assertEquals("650) 253-0000", PhoneNumberUtil.extractPossibleNumber("(650) 253-0000."))
        # This case has a trailing RTL char.
        self.assertEquals("650) 253-0000", PhoneNumberUtil.extractPossibleNumber("(650) 253-0000\u200F"))
    
"""    
    def testMaybeStripNationalPrefix(self):
        nationalPrefix = "34"
        StringBuffer numberToStrip = StringBuffer("34356778")
        String strippedNumber = "356778"
        String nationalRuleRegExp = "\\d{4,7}"
        Pattern nationalRule = Pattern.compile(nationalRuleRegExp)
        phoneUtil.maybeStripNationalPrefix(numberToStrip, nationalPrefix, "", nationalRule)
        self.assertEquals("Should have had national prefix stripped.",
                     strippedNumber, numberToStrip.toString())
        # Retry stripping - now the number should not start with the national prefix, so no more
        # stripping should occur.
        phoneUtil.maybeStripNationalPrefix(numberToStrip, nationalPrefix, "", nationalRule)
        self.assertEquals("Should have had no change - no national prefix present.",
                     strippedNumber, numberToStrip.toString())
        # Some countries have no national prefix. Repeat test with none specified.
        nationalPrefix = ""
        phoneUtil.maybeStripNationalPrefix(numberToStrip, nationalPrefix, "", nationalRule)
        self.assertEquals("Should not strip anything with empty national prefix.",
                     strippedNumber, numberToStrip.toString())
        # If the resultant number doesn't match the national rule, it shouldn't be stripped.
        nationalPrefix = "3"
        numberToStrip = StringBuffer("3123")
        strippedNumber = "3123"
        phoneUtil.maybeStripNationalPrefix(numberToStrip, nationalPrefix, "", nationalRule)
        self.assertEquals("Should have had no change - after stripping, it wouldn't have matched " +
                     "the national rule.",
                     strippedNumber, numberToStrip.toString())
    
    
    def testMaybeStripInternationalPrefix(self):
        String internationalPrefix = "00[39]"
        StringBuffer numberToStrip = StringBuffer("0034567700-3898003")
        # Note the dash is removed as part of the normalization.
        StringBuffer strippedNumber = StringBuffer("45677003898003")
        self.assertEquals(CountryCodeSource.FROM_NUMBER_WITH_IDD,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
        self.assertEquals("The number supplied was not stripped of its international prefix.",
                     strippedNumber.toString(), numberToStrip.toString())
        # Now the number no longer starts with an IDD prefix, so it should now report
        # FROM_DEFAULT_COUNTRY.
        self.assertEquals(CountryCodeSource.FROM_DEFAULT_COUNTRY,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
    
        numberToStrip = StringBuffer("00945677003898003")
        self.assertEquals(CountryCodeSource.FROM_NUMBER_WITH_IDD,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
        self.assertEquals("The number supplied was not stripped of its international prefix.",
                     strippedNumber.toString(), numberToStrip.toString())
        # Test it works when the international prefix is broken up by spaces.
        numberToStrip = StringBuffer("00 9 45677003898003")
        self.assertEquals(CountryCodeSource.FROM_NUMBER_WITH_IDD,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
        self.assertEquals("The number supplied was not stripped of its international prefix.",
                     strippedNumber.toString(), numberToStrip.toString())
        # Now the number no longer starts with an IDD prefix, so it should now report
        # FROM_DEFAULT_COUNTRY.
        self.assertEquals(CountryCodeSource.FROM_DEFAULT_COUNTRY,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
    
        # Test the + symbol is also recognised and stripped.
        numberToStrip = StringBuffer("+45677003898003")
        strippedNumber = StringBuffer("45677003898003")
        self.assertEquals(CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
        self.assertEquals("The number supplied was not stripped of the plus symbol.",
                     strippedNumber.toString(), numberToStrip.toString())
    
        # If the number afterwards is a zero, we should not strip this - no country code begins with 0.
        numberToStrip = StringBuffer("0090112-3123")
        strippedNumber = StringBuffer("00901123123")
        self.assertEquals(CountryCodeSource.FROM_DEFAULT_COUNTRY,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
        self.assertEquals("The number supplied had a 0 after the match so shouldn't be stripped.",
                     strippedNumber.toString(), numberToStrip.toString())
        # Here the 0 is separated by a space from the IDD.
        numberToStrip = StringBuffer("009 0-112-3123")
        self.assertEquals(CountryCodeSource.FROM_DEFAULT_COUNTRY,
                     phoneUtil.maybeStripInternationalPrefixAndNormalize(numberToStrip,
                                                                         internationalPrefix))
    
    
    def testMaybeExtractCountryCode(self):
        number = PhoneNumber()
        metadata = phoneUtil.getMetadataForRegion("US")
        # Note that for the US, the IDD is 011.
        try:
            phoneNumber = "011112-3456789"
            strippedNumber = "123456789"
            countryCode = 1
            StringBuffer numberToFill = StringBuffer()
            self.assertEquals("Did not extract country code " + countryCode + " correctly.",
                       countryCode,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, true,
                                                         number))
            self.assertEquals("Did not figure out CountryCodeSource correctly",
                       CountryCodeSource.FROM_NUMBER_WITH_IDD, number.getCountryCodeSource())
            # Should strip and normalize national significant number.
            self.assertEquals("Did not strip off the country code correctly.",
                       strippedNumber,
                       numberToFill.toString())
       except NumberParseException e:
           fail("Should not have thrown an exception: " + e.toString())
      
           number.clear()
       try:
          String phoneNumber = "+6423456789"
          int countryCode = 64
          StringBuffer numberToFill = StringBuffer()
          self.assertEquals("Did not extract country code " + countryCode + " correctly.",
                       countryCode,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, true,
                                                         number))
          self.assertEquals("Did not figure out CountryCodeSource correctly",
                       CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN, number.getCountryCodeSource())
       catch (NumberParseException e) {
          fail("Should not have thrown an exception: " + e.toString())
      
        number.clear()
        try {
          String phoneNumber = "2345-6789"
          StringBuffer numberToFill = StringBuffer()
          self.assertEquals("Should not have extracted a country code - no international prefix present.",
                       0,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, true,
                                                         number))
          self.assertEquals("Did not figure out CountryCodeSource correctly",
                       CountryCodeSource.FROM_DEFAULT_COUNTRY, number.getCountryCodeSource())
       catch (NumberParseException e) {
          fail("Should not have thrown an exception: " + e.toString())
      
        number.clear()
        try {
          String phoneNumber = "0119991123456789"
          StringBuffer numberToFill = StringBuffer()
          phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, true, number)
          fail("Should have thrown an exception, no valid country code present.")
       catch (NumberParseException e) {
          # Expected.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.INVALID_COUNTRY_CODE,
                       e.getErrorType())
      
        number.clear()
        try {
          String phoneNumber = "(1 610) 619 4466"
          int countryCode = 1
          StringBuffer numberToFill = StringBuffer()
          self.assertEquals("Should have extracted the country code of the region passed in",
                       countryCode,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, true,
                                                         number))
          self.assertEquals("Did not figure out CountryCodeSource correctly",
                       CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN,
                       number.getCountryCodeSource())
       catch (NumberParseException e) {
          fail("Should not have thrown an exception: " + e.toString())
      
        number.clear()
        try {
          String phoneNumber = "(1 610) 619 4466"
          int countryCode = 1
          StringBuffer numberToFill = StringBuffer()
          self.assertEquals("Should have extracted the country code of the region passed in",
                       countryCode,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, false,
                                                         number))
          assertFalse("Should not contain CountryCodeSource.", number.hasCountryCodeSource())
       catch (NumberParseException e) {
          fail("Should not have thrown an exception: " + e.toString())
      
        number.clear()
        try {
          String phoneNumber = "(1 610) 619 446"
          StringBuffer numberToFill = StringBuffer()
          self.assertEquals("Should not have extracted a country code - invalid number after extraction " +
                       "of uncertain country code.",
                       0,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, false,
                                                         number))
          assertFalse("Should not contain CountryCodeSource.", number.hasCountryCodeSource())
       catch (NumberParseException e) {
          fail("Should not have thrown an exception: " + e.toString())
      
        number.clear()
        try {
          String phoneNumber = "(1 610) 619 43"
          StringBuffer numberToFill = StringBuffer()
          self.assertEquals("Should not have extracted a country code - invalid number both before and " +
                       "after extraction of uncertain country code.",
                       0,
                       phoneUtil.maybeExtractCountryCode(phoneNumber, metadata, numberToFill, true,
                                                         number))
          self.assertEquals("Did not figure out CountryCodeSource correctly",
                       CountryCodeSource.FROM_DEFAULT_COUNTRY, number.getCountryCodeSource())
       catch (NumberParseException e) {
          fail("Should not have thrown an exception: " + e.toString())
      
    
    
      def testParseNationalNumber(self):
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(33316005L)
    
        # National prefix attached.
        self.assertEquals(nzNumber, phoneUtil.parse("033316005", "NZ"))
        self.assertEquals(nzNumber, phoneUtil.parse("033316005", "nz"))
        self.assertEquals(nzNumber, phoneUtil.parse("33316005", "NZ"))
        # National prefix attached and some formatting present.
        self.assertEquals(nzNumber, phoneUtil.parse("03-331 6005", "NZ"))
        self.assertEquals(nzNumber, phoneUtil.parse("03 331 6005", "NZ"))
    
        # Testing international prefixes.
        # Should strip country code.
        self.assertEquals(nzNumber, phoneUtil.parse("0064 3 331 6005", "NZ"))
        # Try again, but this time we have an international number with Region Code US. It should
        # recognise the country code and parse accordingly.
        self.assertEquals(nzNumber, phoneUtil.parse("01164 3 331 6005", "US"))
        self.assertEquals(nzNumber, phoneUtil.parse("+64 3 331 6005", "US"))
    
        nzNumber.clear()
        nzNumber.setCountryCode(64).setNationalNumber(64123456L)
        self.assertEquals(nzNumber, phoneUtil.parse("64(0)64123456", "NZ"))
        # Check that using a "/" is fine in a phone number.
        deNumber = PhoneNumber()
        deNumber.setCountryCode(49).setNationalNumber(12345678L)
        self.assertEquals(deNumber, phoneUtil.parse("123/45678", "DE"))
    
        usNumber = PhoneNumber()
        # Check it doesn't use the '1' as a country code when parsing if the phone number was already
        # possible.
        usNumber.setCountryCode(1).setNationalNumber(1234567890L)
        self.assertEquals(usNumber, phoneUtil.parse("123-456-7890", "US"))
    
    
      def testParseNumberWithAlphaCharacters(self):
        # Test case with alpha characters.
        tollfreeNumber = PhoneNumber()
        tollfreeNumber.setCountryCode(64).setNationalNumber(800332005L)
        self.assertEquals(tollfreeNumber, phoneUtil.parse("0800 DDA 005", "NZ"))
        premiumNumber = PhoneNumber()
        premiumNumber.setCountryCode(64).setNationalNumber(9003326005L)
        self.assertEquals(premiumNumber, phoneUtil.parse("0900 DDA 6005", "NZ"))
        # Not enough alpha characters for them to be considered intentional, so they are stripped.
        self.assertEquals(premiumNumber, phoneUtil.parse("0900 332 6005a", "NZ"))
        self.assertEquals(premiumNumber, phoneUtil.parse("0900 332 600a5", "NZ"))
        self.assertEquals(premiumNumber, phoneUtil.parse("0900 332 600A5", "NZ"))
        self.assertEquals(premiumNumber, phoneUtil.parse("0900 a332 600A5", "NZ"))
    
    
      def testParseWithInternationalPrefixes(self):
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6503336000L)
        self.assertEquals(usNumber, phoneUtil.parse("+1 (650) 333-6000", "NZ"))
        self.assertEquals(usNumber, phoneUtil.parse("1-650-333-6000", "US"))
        # Calling the US number from Singapore by using different service providers
        # 1st test: calling using SingTel IDD service (IDD is 001)
        self.assertEquals(usNumber, phoneUtil.parse("0011-650-333-6000", "SG"))
        # 2nd test: calling using StarHub IDD service (IDD is 008)
        self.assertEquals(usNumber, phoneUtil.parse("0081-650-333-6000", "SG"))
        # 3rd test: calling using SingTel V019 service (IDD is 019)
        self.assertEquals(usNumber, phoneUtil.parse("0191-650-333-6000", "SG"))
        # Calling the US number from Poland
        self.assertEquals(usNumber, phoneUtil.parse("0~01-650-333-6000", "PL"))
        # Using "++" at the start.
        self.assertEquals(usNumber, phoneUtil.parse("++1 (650) 333-6000", "PL"))
        # Using a full-width plus sign.
        self.assertEquals(usNumber, phoneUtil.parse("\uFF0B1 (650) 333-6000", "SG"))
        # The whole number, including punctuation, is here represented in full-width form.
        self.assertEquals(usNumber, phoneUtil.parse("\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09" +
                                               "\u3000\uFF13\uFF13\uFF13\uFF0D\uFF16\uFF10\uFF10\uFF10",
                                               "SG"))
    
    
      def testParseWithLeadingZero(self):
        itNumber = PhoneNumber()
        itNumber.setCountryCode(39).setNationalNumber(236618300L).setItalianLeadingZero(true)
        self.assertEquals(itNumber, phoneUtil.parse("+39 02-36618 300", "NZ"))
        self.assertEquals(itNumber, phoneUtil.parse("02-36618 300", "IT"))
    
        itNumber.clear()
        itNumber.setCountryCode(39).setNationalNumber(312345678L)
        self.assertEquals(itNumber, phoneUtil.parse("312 345 678", "IT"))
    
    
      def testParseNationalNumberArgentina(self):
        # Test parsing mobile numbers of Argentina.
        arNumber = PhoneNumber()
    
        arNumber.setCountryCode(54).setNationalNumber(93435551212L)
        self.assertEquals(arNumber, phoneUtil.parse("+54 9 343 555 1212", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("0343 15 555 1212", "AR"))
    
        arNumber.clear()
        arNumber.setCountryCode(54).setNationalNumber(93715654320L)
        self.assertEquals(arNumber, phoneUtil.parse("+54 9 3715 65 4320", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("03715 15 65 4320", "AR"))
    
        # Test parsing fixed-line numbers of Argentina.
        arNumber.clear()
        arNumber.setCountryCode(54).setNationalNumber(1137970000L)
        self.assertEquals(arNumber, phoneUtil.parse("+54 11 3797 0000", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("011 3797 0000", "AR"))
    
        arNumber.clear()
        arNumber.setCountryCode(54).setNationalNumber(3715654321L)
        self.assertEquals(arNumber, phoneUtil.parse("+54 3715 65 4321", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("03715 65 4321", "AR"))
    
        arNumber.clear()
        arNumber.setCountryCode(54).setNationalNumber(2312340000L)
        self.assertEquals(arNumber, phoneUtil.parse("+54 23 1234 0000", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("023 1234 0000", "AR"))
    
    
      def testParseWithXInNumber(self):
        # Test that having an 'x' in the phone number at the start is ok and that it just gets removed.
        arNumber = PhoneNumber()
        arNumber.setCountryCode(54).setNationalNumber(123456789L)
        self.assertEquals(arNumber, phoneUtil.parse("0123456789", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("(0) 123456789", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("0 123456789", "AR"))
        self.assertEquals(arNumber, phoneUtil.parse("(0xx) 123456789", "AR"))
        arFromUs = PhoneNumber()
        arFromUs.setCountryCode(54).setNationalNumber(81429712L)
        # This test is intentionally constructed such that the number of digit after xx is larger than
        # 7, so that the number won't be mistakenly treated as an extension, as we allow extensions up
        # to 7 digits. This assumption is okay for now as all the countries where a carrier selection
        # code is written in the form of xx have a national significant number of length larger than 7.
        self.assertEquals(arFromUs, phoneUtil.parse("011xx5481429712", "US"))
    
    
      def testParseNumbersMexico(self):
        # Test parsing fixed-line numbers of Mexico.
        mxNumber = PhoneNumber()
        mxNumber.setCountryCode(52).setNationalNumber(4499780001L)
        self.assertEquals(mxNumber, phoneUtil.parse("+52 (449)978-0001", "MX"))
        self.assertEquals(mxNumber, phoneUtil.parse("01 (449)978-0001", "MX"))
        self.assertEquals(mxNumber, phoneUtil.parse("(449)978-0001", "MX"))
    
        # Test parsing mobile numbers of Mexico.
        mxNumber.clear()
        mxNumber.setCountryCode(52).setNationalNumber(13312345678L)
        self.assertEquals(mxNumber, phoneUtil.parse("+52 1 33 1234-5678", "MX"))
        self.assertEquals(mxNumber, phoneUtil.parse("044 (33) 1234-5678", "MX"))
        self.assertEquals(mxNumber, phoneUtil.parse("045 33 1234-5678", "MX"))
    
    
      def testFailedParseOnInvalidNumbers(self):
        try {
          String sentencePhoneNumber = "This is not a phone number"
          phoneUtil.parse(sentencePhoneNumber, "NZ")
          fail("This should not parse without throwing an exception " + sentencePhoneNumber)
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.NOT_A_NUMBER,
                       e.getErrorType())
      
        try {
          String tooLongPhoneNumber = "01495 72553301873 810104"
          phoneUtil.parse(tooLongPhoneNumber, "GB")
          fail("This should not parse without throwing an exception " + tooLongPhoneNumber)
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.TOO_LONG,
                       e.getErrorType())
      
        try {
          String plusMinusPhoneNumber = "+---"
          phoneUtil.parse(plusMinusPhoneNumber, "DE")
          fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.NOT_A_NUMBER,
                       e.getErrorType())
      
        try {
          String tooShortPhoneNumber = "+49 0"
          phoneUtil.parse(tooShortPhoneNumber, "DE")
          fail("This should not parse without throwing an exception " + tooShortPhoneNumber)
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.TOO_SHORT_NSN,
                       e.getErrorType())
      
        try {
          String invalidCountryCode = "+210 3456 56789"
          phoneUtil.parse(invalidCountryCode, "NZ")
          fail("This is not a recognised country code: should fail: " + invalidCountryCode)
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.INVALID_COUNTRY_CODE,
                       e.getErrorType())
      
        try {
          String someNumber = "123 456 7890"
          phoneUtil.parse(someNumber, "YY")
          fail("'Unknown' country code not allowed: should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.INVALID_COUNTRY_CODE,
                       e.getErrorType())
      
        try {
          String someNumber = "123 456 7890"
          phoneUtil.parse(someNumber, "CS")
          fail("Deprecated country code not allowed: should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.INVALID_COUNTRY_CODE,
                       e.getErrorType())
      
        try {
          String someNumber = "123 456 7890"
          phoneUtil.parse(someNumber, null)
          fail("Null country code not allowed: should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.INVALID_COUNTRY_CODE,
                       e.getErrorType())
      
        try {
          String someNumber = "0044------"
          phoneUtil.parse(someNumber, "GB")
          fail("No number provided, only country code: should fail")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.TOO_SHORT_AFTER_IDD,
                       e.getErrorType())
      
        try {
          String someNumber = "0044"
          phoneUtil.parse(someNumber, "GB")
          fail("No number provided, only country code: should fail")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.TOO_SHORT_AFTER_IDD,
                       e.getErrorType())
      
        try {
          String someNumber = "011"
          phoneUtil.parse(someNumber, "US")
          fail("Only IDD provided - should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.TOO_SHORT_AFTER_IDD,
                       e.getErrorType())
      
        try {
          String someNumber = "0119"
          phoneUtil.parse(someNumber, "US")
          fail("Only IDD provided and then 9 - should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.TOO_SHORT_AFTER_IDD,
                       e.getErrorType())
      
        try {
          String emptyNumber = ""
          # Invalid region.
          phoneUtil.parse(emptyNumber, "ZZ")
          fail("Empty string - should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.NOT_A_NUMBER,
                       e.getErrorType())
      
    
    
      def testParseNumbersWithPlusWithNoRegion(self):
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(33316005L)
        # "ZZ" is allowed only if the number starts with a '+' - then the country code can be
        # calculated.
        self.assertEquals(nzNumber, phoneUtil.parse("+64 3 331 6005", "ZZ"))
        self.assertEquals(nzNumber, phoneUtil.parse("+64 3 331 6005", null))
        nzNumber.setRawInput("+64 3 331 6005").
            setCountryCodeSource(CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN)
        self.assertEquals(nzNumber, phoneUtil.parseAndKeepRawInput("+64 3 331 6005", "ZZ"))
        # Null is also allowed for the region code in these cases.
        self.assertEquals(nzNumber, phoneUtil.parseAndKeepRawInput("+64 3 331 6005", null))
    
    
      def testParseExtensions(self):
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(33316005L).setExtension("3456")
        self.assertEquals(nzNumber, phoneUtil.parse("03 331 6005 ext 3456", "NZ"))
        self.assertEquals(nzNumber, phoneUtil.parse("03-3316005x3456", "NZ"))
        self.assertEquals(nzNumber, phoneUtil.parse("03-3316005 int.3456", "NZ"))
        self.assertEquals(nzNumber, phoneUtil.parse("03 3316005 #3456", "NZ"))
        # Test the following do not extract extensions:
        nonExtnNumber = PhoneNumber()
        nonExtnNumber.setCountryCode(1).setNationalNumber(80074935247L)
        self.assertEquals(nonExtnNumber, phoneUtil.parse("1800 six-flags", "US"))
        self.assertEquals(nonExtnNumber, phoneUtil.parse("1800 SIX FLAGS", "US"))
        self.assertEquals(nonExtnNumber, phoneUtil.parse("0~0 1800 7493 5247", "PL"))
        self.assertEquals(nonExtnNumber, phoneUtil.parse("(1800) 7493.5247", "US"))
        # Check that the last instance of an extension token is matched.
        extnNumber = PhoneNumber()
        extnNumber.setCountryCode(1).setNationalNumber(80074935247L).setExtension("1234")
        self.assertEquals(extnNumber, phoneUtil.parse("0~0 1800 7493 5247 ~1234", "PL"))
        # Verifying bug-fix where the last digit of a number was previously omitted if it was a 0 when
        # extracting the extension. Also verifying a few different cases of extensions.
        ukNumber = PhoneNumber()
        ukNumber.setCountryCode(44).setNationalNumber(2034567890L).setExtension("456")
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890x456", "NZ"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890x456", "GB"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890 x456", "GB"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890 X456", "GB"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890 X 456", "GB"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890 X  456", "GB"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890 x 456  ", "GB"))
        self.assertEquals(ukNumber, phoneUtil.parse("+44 2034567890  X 456", "GB"))
    
        usWithExtension = PhoneNumber()
        usWithExtension.setCountryCode(1).setNationalNumber(8009013355L).setExtension("7246433")
        self.assertEquals(usWithExtension, phoneUtil.parse("(800) 901-3355 x 7246433", "US"))
        self.assertEquals(usWithExtension, phoneUtil.parse("(800) 901-3355 , ext 7246433", "US"))
        self.assertEquals(usWithExtension,
                     phoneUtil.parse("(800) 901-3355 ,extension 7246433", "US"))
        self.assertEquals(usWithExtension, phoneUtil.parse("(800) 901-3355 , 7246433", "US"))
        self.assertEquals(usWithExtension, phoneUtil.parse("(800) 901-3355 ext: 7246433", "US"))
    
        # Test that if a number has two extensions specified, we ignore the second.
        usWithTwoExtensionsNumber = PhoneNumber()
        usWithTwoExtensionsNumber.setCountryCode(1).setNationalNumber(2121231234L).setExtension("508")
        self.assertEquals(usWithTwoExtensionsNumber, phoneUtil.parse("(212)123-1234 x508/x1234",
                                                                "US"))
        self.assertEquals(usWithTwoExtensionsNumber, phoneUtil.parse("(212)123-1234 x508/ x1234",
                                                                "US"))
        self.assertEquals(usWithTwoExtensionsNumber, phoneUtil.parse("(212)123-1234 x508\\x1234",
                                                                "US"))
    
        # Test parsing numbers in the form (645) 123-1234-910# works, where the last 3 digits before
        # the # are an extension.
        usWithExtension.clear()
        usWithExtension.setCountryCode(1).setNationalNumber(6451231234L).setExtension("910")
        self.assertEquals(usWithExtension, phoneUtil.parse("+1 (645) 123 1234-910#", "US"))
        # Retry with the same number in a slightly different format.
        self.assertEquals(usWithExtension, phoneUtil.parse("+1 (645) 123 1234 ext. 910#", "US"))
    
    
      def testParseAndKeepRaw(self):
        alphaNumericNumber = PhoneNumber()
        alphaNumericNumber.
            setCountryCode(1).setNationalNumber(80074935247L).setRawInput("800 six-flags").
            setCountryCodeSource(CountryCodeSource.FROM_DEFAULT_COUNTRY)
        self.assertEquals(alphaNumericNumber,
                     phoneUtil.parseAndKeepRawInput("800 six-flags", "US"))
    
        alphaNumericNumber.
            setCountryCode(1).setNationalNumber(8007493524L).setRawInput("1800 six-flag").
            setCountryCodeSource(CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN)
        self.assertEquals(alphaNumericNumber,
                     phoneUtil.parseAndKeepRawInput("1800 six-flag", "US"))
    
        alphaNumericNumber.
            setCountryCode(1).setNationalNumber(8007493524L).setRawInput("+1800 six-flag").
            setCountryCodeSource(CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN)
        self.assertEquals(alphaNumericNumber,
                     phoneUtil.parseAndKeepRawInput("+1800 six-flag", "NZ"))
    
        alphaNumericNumber.
            setCountryCode(1).setNationalNumber(8007493524L).setRawInput("001800 six-flag").
            setCountryCodeSource(CountryCodeSource.FROM_NUMBER_WITH_IDD)
        self.assertEquals(alphaNumericNumber,
                     phoneUtil.parseAndKeepRawInput("001800 six-flag", "NZ"))
    
        # Invalid region code supplied.
        try {
          phoneUtil.parseAndKeepRawInput("123 456 7890", "CS")
          fail("Deprecated country code not allowed: should fail.")
       catch (NumberParseException e) {
          # Expected this exception.
          self.assertEquals("Wrong error type stored in exception.",
                       NumberParseException.ErrorType.INVALID_COUNTRY_CODE,
                       e.getErrorType())
      
    
    
      def testCountryWithNoNumberDesc(self):
        # Andorra is a country where we don't have PhoneNumberDesc info in the metadata.
        adNumber = PhoneNumber()
        adNumber.setCountryCode(376).setNationalNumber(12345L)
        self.assertEquals("+376 12345", phoneUtil.format(adNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEquals("+37612345", phoneUtil.format(adNumber, PhoneNumberFormat.E164))
        self.assertEquals("12345", phoneUtil.format(adNumber, PhoneNumberFormat.NATIONAL))
        self.assertEquals(PhoneNumberUtil.PhoneNumberType.UNKNOWN, phoneUtil.getNumberType(adNumber))
        assertTrue(phoneUtil.isValidNumber(adNumber))
    
        # Test dialing a US number from within Andorra.
        usNumber = PhoneNumber()
        usNumber.setCountryCode(1).setNationalNumber(6502530000L)
        self.assertEquals("00 1 650 253 0000",
                     phoneUtil.formatOutOfCountryCallingNumber(usNumber, "AD"))
    
    
      def testUnknownCountryCallingCodeForValidation(self):
        invalidNumber = PhoneNumber()
        invalidNumber.setCountryCode(0).setNationalNumber(1234L)
        assertFalse(phoneUtil.isValidNumber(invalidNumber))
    
    
      def testIsNumberMatchMatches(self):
        # Test simple matches where formatting is different, or leading zeroes, or country code has
        # been specified.
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331 6005", "+64 03 331 6005"))
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+64 03 331-6005", "+64 03331 6005"))
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+643 331-6005", "+64033316005"))
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+643 331-6005", "+6433316005"))
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005", "+6433316005"))
        # Test alpha numbers.
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+1800 siX-Flags", "+1 800 7493 5247"))
        # Test numbers with extensions.
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005 extn 1234", "+6433316005#1234"))
        # Test proto buffers.
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(33316005L).setExtension("3456")
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch(nzNumber, "+643 331 6005 ext 3456"))
        nzNumber.clearExtension()
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch(nzNumber, "+6403 331 6005"))
        # Check empty extensions are ignored.
        nzNumber.setExtension("")
        self.assertEquals(PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch(nzNumber, "+6403 331 6005"))
        # Check variant with two proto buffers.
        nzNumberTwo = PhoneNumber()
        nzNumberTwo.setCountryCode(64).setNationalNumber(33316005L)
        self.assertEquals("Number " + nzNumber.toString() + " did not match " + nzNumberTwo.toString(),
                     PhoneNumberUtil.MatchType.EXACT_MATCH,
                     phoneUtil.isNumberMatch(nzNumber, nzNumberTwo))
    
    
      def testIsNumberMatchNonMatches(self):
        # Non-matches.
        self.assertEquals(PhoneNumberUtil.MatchType.NO_MATCH,
                     phoneUtil.isNumberMatch("03 331 6005", "03 331 6006"))
        # Different country code, partial number match.
        self.assertEquals(PhoneNumberUtil.MatchType.NO_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005", "+16433316005"))
        # Different country code, same number.
        self.assertEquals(PhoneNumberUtil.MatchType.NO_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005", "+6133316005"))
        # Extension different, all else the same.
        self.assertEquals(PhoneNumberUtil.MatchType.NO_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005 extn 1234", "0116433316005#1235"))
        # NSN matches, but extension is different - not the same number.
        self.assertEquals(PhoneNumberUtil.MatchType.NO_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005 ext.1235", "3 331 6005#1234"))
    
    
      def testIsNumberMatchNsnMatches(self):
        # NSN matches.
        self.assertEquals(PhoneNumberUtil.MatchType.NSN_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005", "03 331 6005"))
        self.assertEquals(PhoneNumberUtil.MatchType.NSN_MATCH,
                     phoneUtil.isNumberMatch("3 331-6005", "03 331 6005"))
        nzNumber = PhoneNumber()
        nzNumber.setCountryCode(64).setNationalNumber(33316005L).setExtension("")
        self.assertEquals(PhoneNumberUtil.MatchType.NSN_MATCH,
                     phoneUtil.isNumberMatch(nzNumber, "03 331 6005"))
        unchangedNzNumber = PhoneNumber()
        unchangedNzNumber.setCountryCode(64).setNationalNumber(33316005L).setExtension("")
        # Check the phone number proto was not edited during the method call.
        self.assertEquals(unchangedNzNumber, nzNumber)
    
    
      def testIsNumberMatchShortNsnMatches(self):
        # Short NSN matches with the country not specified for either one or both numbers.
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005", "331 6005"))
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("3 331-6005", "331 6005"))
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("3 331-6005", "+64 331 6005"))
        # Short NSN match with the country specified.
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("03 331-6005", "331 6005"))
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("1 234 345 6789", "345 6789"))
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("+1 (234) 345 6789", "345 6789"))
        # NSN matches, country code omitted for one number, extension missing for one.
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch("+64 3 331-6005", "3 331 6005#1234"))
        # One has Italian leading zero, one does not.
        italianNumberOne = PhoneNumber()
        italianNumberOne.setCountryCode(39).setNationalNumber(1234L).setItalianLeadingZero(true)
        italianNumberTwo = PhoneNumber()
        italianNumberTwo.setCountryCode(39).setNationalNumber(1234L)
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch(italianNumberOne, italianNumberTwo))
        # One has an extension, the other has an extension of "".
        italianNumberOne.setExtension("1234").clearItalianLeadingZero()
        italianNumberTwo.setExtension("")
        self.assertEquals(PhoneNumberUtil.MatchType.SHORT_NSN_MATCH,
                     phoneUtil.isNumberMatch(italianNumberOne, italianNumberTwo))
"""

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PhoneNumberUtilTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
