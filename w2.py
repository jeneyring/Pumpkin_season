import requests
from env import c_usda_quick_stats
import urllib.parse


parameters = 'source_desc=SURVEY' + '&' + urllib.parse.quote('sector_desc=CROPS') + '&' + urllib.parse.quote('group_desc=VEGETABLES') + '&' + urllib.parse.quote('commodity_desc=PUMPKINS') + '&' + urllib.parse.quote('statisticcat_desc=AREA HARVESTED') + '&' + urllib.parse.quote('unit_desc=ACRES') + '&' + urllib.parse.quote('freq_desc=ANNUAL') + '&' + urllib.parse.quote('reference_period_desc=YEAR') + '&' + urllib.parse.quote('year_GE=2000') + '&' + urllib.parse.quote('state_name=US TOTAL') + '&format=CSV'
            
stats = env.c_usda_quick_stats()

s_json = stats.get_data(parameters, 'national_pumpkin_harvested_2000')