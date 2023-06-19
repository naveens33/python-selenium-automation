import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

file_path = os.path.dirname(os.path.abspath("top_level_file.txt")) + r"\extension\Google-Translate.crx"
options = Options()
options.add_extension(file_path)
driver = webdriver.Chrome(options=options)
