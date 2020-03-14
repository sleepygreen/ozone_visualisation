import cdsapi
import os
c = cdsapi.Client()

years = [str(x) for x in range(1989,2019)]

c.retrieve(
    'satellite-ozone',
    {
        'processing_level': 'level_4',
        'variable': 'ozone_mole_content',
        'vertical_aggregation': 'total_column',
        'sensor': 'combination_of_15_sensors_using_gap_filling_assimilation_methods',
        'year': years,
        'month': '01',
        'version': '0021',
        'format': 'zip',
    },
    'download.zip')