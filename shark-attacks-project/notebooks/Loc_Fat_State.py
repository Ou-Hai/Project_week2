def Location(SAdf):
    def extract_county(location_string):
    """
    Attempts to extract the County name from a location string
    and ensures the result is always formatted as 'CountyName County'.
    """
    location = str(location_string).strip()
    
    # 1. Standard Pattern Check
    # Look for text preceding ' County' and capture ONLY the county name.
    match = re.search(r'([A-Za-z\s]+)\sCounty', location, re.IGNORECASE)
    if match:
        # Returns: 'Volusia County'
        return match.group(1).strip() + ' County'

    # 2. Handle Specific Common Cases
    # For these manual cases, we append ' County' directly.
    if 'Myrtle Beach' in location or 'North Myrtle Beach' in location:
        return 'Horry County'
    if 'Galveston' == location:
        return 'Galveston County'
    if 'New Smyrna Beach' == location:
        return 'Volusia County'
    if 'Kauai' in location:
        return 'Kauai County'
    if 'Maui' in location:
        return 'Maui County'
    if 'Oahu' in location or 'Haleiwa' in location:
        return 'Oahu County'
    if 'Miami Beach' in location or 'Miami' == location:
        return 'Miami-Dade County'
    if 'South Padre Island' in location:
        return 'Cameron County'
    
    # 3. Handle specific existing counties that don't need ' County' appended
    # (e.g., if you know 'Miami-Dade' is often in the data and you don't want 'Miami-Dade County County')
    if 'Miami-Dade' in location:
        return 'Miami-Dade County'

    # If no county is definitively found, return the full location for manual review
    # (These will be the entries that couldn't be grouped)
    return location
    SAdf['Location'] = SAdf['Location'].apply(extract_county)
    SAloc_df=SAdf["Location"].value_counts()
    SA_HighOccurences=SAloc_df[SAloc_df>9].index
    SAdf['Location']=SAdf.Location.fillna('UNKNOWN')
    SAdf_Location=SAdf[SAdf["Location"].isin(SA_HighOccurences)]
    SAdf['Location']=SAdf_Location
    return SAdf

def Fatal(SAdf):
    SAdf=SAdf.rename(columns={ "Fatal (Y/N)": "Fatal"})
    SAdf_Location['Fatal Y/N'] = SAdf_Location['Fatal Y/N'].str.strip()
    SAdf_Fatal_replacements={
    'F':'Y',
    'Nq':'N',
    'n':'N',
    'UNKNOWN':'Y'
    }
    SAdf_Location.replace(SAdf_Fatal_replacements, inplace=True)
    SAdf_Location.value_counts('Fatal Y/N')
    return SAdf

def State(SAdf)
    SAdf['State'] = SAdf['State'].str.strip()
    SAdf_Fatal_replacements={
    'Floria':'Florida',
    'BAHAMAS':'Bahamas',
    }
    SAdf.replace(SAdf_Fatal_replacements, inplace=True)
    return SAdf