# UIS-assets
This repository contains python scripts to analyze University of Illinois System assets invested in companies that profit from the extraction, transportation, or combustion of coal, petroleum, or natural gas.

## Background

The University of Illinois System has over $3.9 Billion assets under management (note that this asset pool is independent of the University of Illinois Foundation’s (UIF) Endowment, which has $2.2+ Billion assets under management). Of these assets, $2.8+ Billion are housed in the Operating Pool. The Operating Pool **"includes cash from state appropriations, tuition and fees, student loan funds, grants, self-insurance programs, and hospital and auxiliary services."** [UIS Annual Report pg. 9](https://www.treasury.uillinois.edu/userfiles/Servers/Server_338/file/Investments/FY21%20University%20System%20Investment%20Office%20Annual%20Report_ALL.pdf)

![image](https://github.com/kennykos/UIS-assets/blob/main/Images/opp_asset_distro.png)

For more information regarding the motivation of this project, refer to:

https://secsatuiuc.web.illinois.edu/2021/12/01/uis-investment-data-report-2021/


## Python Script

* **database.py**
    + Running the database python script initializes a sqlite3 database of securities held in the operating pool and their associated information. The industry and ticker of the related asset were mined from wikipedia, while all other data is publicly provided by UIS.

* **investment_analysis.py**
    + Running the investment analysis python script outputs relevant information regarding holdings in the Operating Pool.
    
```python
%run investment_analysis.py
```

    The University of Illinois System (UIS) has $121,458,102.87 out of the $2,809,677,874.72 operating pool funds (4.32%) invested in 78 companies that profit from the extraction, transportation, or combustion of coal, petroleum, or natural gas. 
    
    Here is a comprehensive list of these companies:  
     ['AEP TEX INC', 'ALABAMA PWR CO', 'ALLIANT ENERGY FIN LLC', 'AMEREN ILL CO', 'AMERICAN ELEC PWR CO', 'ATMOS ENERGY CO', 'BAKER HUGHES A GE CO', 'BERKSHIRE HATHAWAY ENERGY CO', 'BLACK HILLS CO', 'BP CAP MKTS', 'BPCE S A MEDIUM TERM NT', 'CANADIAN NAT RES LTD', 'CENTERPOINT ENERGY', 'CHEVRON', 'CONNECTICUT LIGHT & POWER CO', 'DOMINION ENERGY INC', 'DOMINION RES INC', 'DTE E', 'DUKE ENERGY', 'EAST OHIO GAS CO', 'EL PASO PIPELINE PART OP', 'ENBRIDGE INC', 'ENEL FIN INTL N V NT', 'ENERGY TRANSFER PARTNERS', 'ENGIE SA NT', 'ENTERGY ARK INC', 'ENTERGY CO', 'ENTERGY LOUISIANA LLC', 'ENTERGY TEX INC', 'ENTERPRISE PRODS OPER LLC', 'EVERSOURCE ENERGY', 'EXELON CO', 'EXXON MOBIL CO', 'FLORIDA PWR & LT CO', 'GETTY PAUL J TR', 'HARVEST OPERATIONS CO', 'INTERSTATE PWR & LT CO', 'JERSEY CENT PWR & LT CO', 'KANSAS CITY POWER & LT', 'MPLX LP BNDS', 'MPLX LP FLTG RT', 'NATL RURAL UTILS CO', 'NEXTERA ENERGY CA', 'NEXTERA ENERGY CAP HLDGS INC', 'NORTHEAST UTILS', 'NORTHERN STS PWR CO', 'NORTHWESTERN CO', 'NRG ENERGY INC', 'OCCIDENTAL PETE CO', 'OGE ENERGY CO', 'OKLAHOMA GAS & ELEC CO', 'ONCOR ELEC DELIVERY CO', 'ONE GAS INC', 'PACIFICORP', 'PEACHTREE CO', 'PHILLIPS 66', 'PIONEER NAT RES CO', 'PPL CAPITAL FUNDING INC', 'PPL ELEC UTILS CO', 'PUBLIC SVC CO', 'PUBLIC SVC ELEC GAS CO', 'PVPTL HARVEST OPERATIONS CO', 'SCHLUMBERGER', 'SHELL INTL FIN B V', 'SINOPEC GROUP OVERSEAS D', 'SOUTHERN CALIF EDISON CO', 'SOUTHERN CALIF GAS CO', 'SOUTHERN CO', 'SOUTHERN NAT GAS CO', 'SOUTHWESTERN PUBLIC SERVICE CO', 'STATOIL ASA FORMERLY STATOIL A', 'SUNOCO LOGISTICS PARTNERS OPER', 'TOTAL CAP INTL', 'VALERO ENERGY CO', 'VIRGINIA ELEC & POWER CO', 'WEC ENERGY GROUP INC', 'WILLIAMS PARTNERS L P', 'XCEL ENERGY INC'] 
    
    More information on UIS investments can be found at: https://www.treasury.uillinois.edu/investments

## References

1. [University of Illinois System Office of Investments Annual Report Fiscal Year Ending June 30, 2021](https://www.treasury.uillinois.edu/userfiles/Servers/Server_338/file/Investments/FY21%20University%20System%20Investment%20Office%20Annual%20Report_ALL.pdf)
2. [Students for Environmental Concerns ](https://secsatuiuc.web.illinois.edu/)
