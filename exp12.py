import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib . pyplot as plt
import re
import os
riturl ="https://ajce.in"
webpage = requests.get (riturl)
ritsoup = BeautifulSoup ( webpage . content , "html.parser")
print ( ritsoup )
ritsoup.title
links = [ link.get('href') for link in ritsoup . find_all ('a') ]
print ( links )
ritsoup.h1
ritsoup.h1.name
ritsoup.head
ritsoup.head.meta