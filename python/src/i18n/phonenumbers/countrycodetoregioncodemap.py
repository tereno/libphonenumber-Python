class CountryCodeToRegionCodeMap:
    """
        A mapping from a country code to the region codes which
        denote the country/region reporesented by that country code.
        In the case of multiple countries sharing a calling code, 
        such as the NANPA countries, the one indicated with
        "isMainCountryCode" in the metadata should be first.
    """
    def getCountryCodeToRegionCodeMap():
        countryCodeToRegionCodeMap = {}
        
        listWithRegionCode = []
        listWithRegionCode.append("US")
        listWithRegionCode.append("AG")
        listWithRegionCode.append("AI")
        listWithRegionCode.append("AS")
        listWithRegionCode.append("BB")
        listWithRegionCode.append("BM")
        listWithRegionCode.append("BS")
        listWithRegionCode.append("CA")
        listWithRegionCode.append("DM")
        listWithRegionCode.append("DO")
        listWithRegionCode.append("GD")
        listWithRegionCode.append("GU")
        listWithRegionCode.append("JM")
        listWithRegionCode.append("KN")
        listWithRegionCode.append("KY")
        listWithRegionCode.append("LC")
        listWithRegionCode.append("MP")
        listWithRegionCode.append("MS")
        listWithRegionCode.append("PR")
        listWithRegionCode.append("TC")
        listWithRegionCode.append("TT")
        listWithRegionCode.append("VC")
        listWithRegionCode.append("VG")
        listWithRegionCode.append("VI")        
        countryCodeToRegionCodeMap[1] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("RU")
        listWithRegionCode.append("KZ")
        countryCodeToRegionCodeMap[7] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("EG")
        countryCodeToRegionCodeMap[20] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("ZA")
        countryCodeToRegionCodeMap[27] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("GR")
        countryCodeToRegionCodeMap[30] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("NL")
        countryCodeToRegionCodeMap[31] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("BE")
        countryCodeToRegionCodeMap[32] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("FR")
        countryCodeToRegionCodeMap[33] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("ES")
        countryCodeToRegionCodeMap[34] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("HU")
        countryCodeToRegionCodeMap[36] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("IT")
        countryCodeToRegionCodeMap[39] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("RO")
        countryCodeToRegionCodeMap[40] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("CH")
        countryCodeToRegionCodeMap[41] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("AT")
        countryCodeToRegionCodeMap[43] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("GB")
        listWithRegionCode.append("GG")
        listWithRegionCode.append("IM")
        listWithRegionCode.append("JE")
        countryCodeToRegionCodeMap[44] = listWithRegionCode
        
        listWithRegionCode = []
        listWithRegionCode.append("DK")
        countryCodeToRegionCodeMap[45] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SE")
        countryCodeToRegionCodeMap[46] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NO")
        countryCodeToRegionCodeMap[47] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PL")
        countryCodeToRegionCodeMap[48] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("DE")
        countryCodeToRegionCodeMap[49] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PE")
        countryCodeToRegionCodeMap[51] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MX")
        countryCodeToRegionCodeMap[52] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CU")
        countryCodeToRegionCodeMap[53] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AR")
        countryCodeToRegionCodeMap[54] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BR")
        countryCodeToRegionCodeMap[55] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CL")
        countryCodeToRegionCodeMap[56] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CO")
        countryCodeToRegionCodeMap[57] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("VE")
        countryCodeToRegionCodeMap[58] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MY")
        countryCodeToRegionCodeMap[60] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AU")
        countryCodeToRegionCodeMap[61] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ID")
        countryCodeToRegionCodeMap[62] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PH")
        countryCodeToRegionCodeMap[63] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NZ")
        countryCodeToRegionCodeMap[64] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SG")
        countryCodeToRegionCodeMap[65] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TH")
        countryCodeToRegionCodeMap[66] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("JP")
        countryCodeToRegionCodeMap[81] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KR")
        countryCodeToRegionCodeMap[82] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("VN")
        countryCodeToRegionCodeMap[84] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CN")
        countryCodeToRegionCodeMap[86] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TR")
        countryCodeToRegionCodeMap[90] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IN")
        countryCodeToRegionCodeMap[91] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PK")
        countryCodeToRegionCodeMap[92] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AF")
        countryCodeToRegionCodeMap[93] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LK")
        countryCodeToRegionCodeMap[94] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MM")
        countryCodeToRegionCodeMap[95] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IR")
        countryCodeToRegionCodeMap[98] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MA")
        countryCodeToRegionCodeMap[212] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("DZ")
        countryCodeToRegionCodeMap[213] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TN")
        countryCodeToRegionCodeMap[216] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LY")
        countryCodeToRegionCodeMap[218] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GM")
        countryCodeToRegionCodeMap[220] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SN")
        countryCodeToRegionCodeMap[221] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MR")
        countryCodeToRegionCodeMap[222] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ML")
        countryCodeToRegionCodeMap[223] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GN")
        countryCodeToRegionCodeMap[224] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CI")
        countryCodeToRegionCodeMap[225] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BF")
        countryCodeToRegionCodeMap[226] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NE")
        countryCodeToRegionCodeMap[227] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TG")
        countryCodeToRegionCodeMap[228] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BJ")
        countryCodeToRegionCodeMap[229] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MU")
        countryCodeToRegionCodeMap[230] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LR")
        countryCodeToRegionCodeMap[231] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SL")
        countryCodeToRegionCodeMap[232] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GH")
        countryCodeToRegionCodeMap[233] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NG")
        countryCodeToRegionCodeMap[234] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TD")
        countryCodeToRegionCodeMap[235] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CF")
        countryCodeToRegionCodeMap[236] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CM")
        countryCodeToRegionCodeMap[237] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CV")
        countryCodeToRegionCodeMap[238] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ST")
        countryCodeToRegionCodeMap[239] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GQ")
        countryCodeToRegionCodeMap[240] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GA")
        countryCodeToRegionCodeMap[241] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CG")
        countryCodeToRegionCodeMap[242] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CD")
        countryCodeToRegionCodeMap[243] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AO")
        countryCodeToRegionCodeMap[244] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GW")
        countryCodeToRegionCodeMap[245] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IO")
        countryCodeToRegionCodeMap[246] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SC")
        countryCodeToRegionCodeMap[248] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SD")
        countryCodeToRegionCodeMap[249] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("RW")
        countryCodeToRegionCodeMap[250] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ET")
        countryCodeToRegionCodeMap[251] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SO")
        countryCodeToRegionCodeMap[252] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("DJ")
        countryCodeToRegionCodeMap[253] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KE")
        countryCodeToRegionCodeMap[254] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TZ")
        countryCodeToRegionCodeMap[255] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("UG")
        countryCodeToRegionCodeMap[256] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BI")
        countryCodeToRegionCodeMap[257] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MZ")
        countryCodeToRegionCodeMap[258] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ZM")
        countryCodeToRegionCodeMap[260] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MG")
        countryCodeToRegionCodeMap[261] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("RE")
        listWithRegionCode.append("TF")
        listWithRegionCode.append("YT")
        countryCodeToRegionCodeMap[262] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ZW")
        countryCodeToRegionCodeMap[263] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NA")
        countryCodeToRegionCodeMap[264] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MW")
        countryCodeToRegionCodeMap[265] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LS")
        countryCodeToRegionCodeMap[266] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BW")
        countryCodeToRegionCodeMap[267] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SZ")
        countryCodeToRegionCodeMap[268] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KM")
        countryCodeToRegionCodeMap[269] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SH")
        countryCodeToRegionCodeMap[290] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ER")
        countryCodeToRegionCodeMap[291] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AW")
        countryCodeToRegionCodeMap[297] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("FO")
        countryCodeToRegionCodeMap[298] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GL")
        countryCodeToRegionCodeMap[299] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GI")
        countryCodeToRegionCodeMap[350] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PT")
        countryCodeToRegionCodeMap[351] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LU")
        countryCodeToRegionCodeMap[352] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IE")
        countryCodeToRegionCodeMap[353] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IS")
        countryCodeToRegionCodeMap[354] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AL")
        countryCodeToRegionCodeMap[355] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MT")
        countryCodeToRegionCodeMap[356] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CY")
        countryCodeToRegionCodeMap[357] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("FI")
        countryCodeToRegionCodeMap[358] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BG")
        countryCodeToRegionCodeMap[359] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LT")
        countryCodeToRegionCodeMap[370] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LV")
        countryCodeToRegionCodeMap[371] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("EE")
        countryCodeToRegionCodeMap[372] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MD")
        countryCodeToRegionCodeMap[373] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AM")
        countryCodeToRegionCodeMap[374] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BY")
        countryCodeToRegionCodeMap[375] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AD")
        countryCodeToRegionCodeMap[376] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MC")
        countryCodeToRegionCodeMap[377] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SM")
        countryCodeToRegionCodeMap[378] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("VA")
        countryCodeToRegionCodeMap[379] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("UA")
        countryCodeToRegionCodeMap[380] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("RS")
        countryCodeToRegionCodeMap[381] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("ME")
        countryCodeToRegionCodeMap[382] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("HR")
        countryCodeToRegionCodeMap[385] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SI")
        countryCodeToRegionCodeMap[386] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BA")
        countryCodeToRegionCodeMap[387] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MK")
        countryCodeToRegionCodeMap[389] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CZ")
        countryCodeToRegionCodeMap[420] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SK")
        countryCodeToRegionCodeMap[421] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LI")
        countryCodeToRegionCodeMap[423] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("FK")
        countryCodeToRegionCodeMap[500] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BZ")
        countryCodeToRegionCodeMap[501] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GT")
        countryCodeToRegionCodeMap[502] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SV")
        countryCodeToRegionCodeMap[503] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("HN")
        countryCodeToRegionCodeMap[504] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NI")
        countryCodeToRegionCodeMap[505] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CR")
        countryCodeToRegionCodeMap[506] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PA")
        countryCodeToRegionCodeMap[507] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PM")
        countryCodeToRegionCodeMap[508] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("HT")
        countryCodeToRegionCodeMap[509] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GP")
        listWithRegionCode.append("BL")
        listWithRegionCode.append("MF")
        countryCodeToRegionCodeMap[590] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BO")
        countryCodeToRegionCodeMap[591] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GY")
        countryCodeToRegionCodeMap[592] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("EC")
        countryCodeToRegionCodeMap[593] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GF")
        countryCodeToRegionCodeMap[594] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PY")
        countryCodeToRegionCodeMap[595] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MQ")
        countryCodeToRegionCodeMap[596] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SR")
        countryCodeToRegionCodeMap[597] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("UY")
        countryCodeToRegionCodeMap[598] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AN")
        countryCodeToRegionCodeMap[599] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TL")
        countryCodeToRegionCodeMap[670] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NF")
        countryCodeToRegionCodeMap[672] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BN")
        countryCodeToRegionCodeMap[673] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NR")
        countryCodeToRegionCodeMap[674] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PG")
        countryCodeToRegionCodeMap[675] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TO")
        countryCodeToRegionCodeMap[676] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SB")
        countryCodeToRegionCodeMap[677] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("VU")
        countryCodeToRegionCodeMap[678] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("FJ")
        countryCodeToRegionCodeMap[679] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PW")
        countryCodeToRegionCodeMap[680] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("WF")
        countryCodeToRegionCodeMap[681] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("CK")
        countryCodeToRegionCodeMap[682] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NU")
        countryCodeToRegionCodeMap[683] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("WS")
        countryCodeToRegionCodeMap[685] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KI")
        countryCodeToRegionCodeMap[686] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NC")
        countryCodeToRegionCodeMap[687] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TV")
        countryCodeToRegionCodeMap[688] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PF")
        countryCodeToRegionCodeMap[689] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TK")
        countryCodeToRegionCodeMap[690] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("FM")
        countryCodeToRegionCodeMap[691] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MH")
        countryCodeToRegionCodeMap[692] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KP")
        countryCodeToRegionCodeMap[850] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("HK")
        countryCodeToRegionCodeMap[852] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MO")
        countryCodeToRegionCodeMap[853] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KH")
        countryCodeToRegionCodeMap[855] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LA")
        countryCodeToRegionCodeMap[856] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BD")
        countryCodeToRegionCodeMap[880] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TW")
        countryCodeToRegionCodeMap[886] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MV")
        countryCodeToRegionCodeMap[960] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("LB")
        countryCodeToRegionCodeMap[961] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("JO")
        countryCodeToRegionCodeMap[962] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SY")
        countryCodeToRegionCodeMap[963] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IQ")
        countryCodeToRegionCodeMap[964] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KW")
        countryCodeToRegionCodeMap[965] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("SA")
        countryCodeToRegionCodeMap[966] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("YE")
        countryCodeToRegionCodeMap[967] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("OM")
        countryCodeToRegionCodeMap[968] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("PS")
        countryCodeToRegionCodeMap[970] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AE")
        countryCodeToRegionCodeMap[971] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("IL")
        countryCodeToRegionCodeMap[972] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BH")
        countryCodeToRegionCodeMap[973] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("QA")
        countryCodeToRegionCodeMap[974] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("BT")
        countryCodeToRegionCodeMap[975] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("MN")
        countryCodeToRegionCodeMap[976] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("NP")
        countryCodeToRegionCodeMap[977] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TJ")
        countryCodeToRegionCodeMap[992] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("TM")
        countryCodeToRegionCodeMap[993] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("AZ")
        countryCodeToRegionCodeMap[994] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("GE")
        countryCodeToRegionCodeMap[995] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("KG")
        countryCodeToRegionCodeMap[996] = listWithRegionCode
    
        listWithRegionCode = []
        listWithRegionCode.append("UZ")
        countryCodeToRegionCodeMap[998] = listWithRegionCode
        
        return countryCodeToRegionCodeMap
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        