#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import requests
from pathlib import Path
from selenium import webdriver

__author__ = 'mejty'


class Downloader(object):
    DOWNLOAD_URL_TEMPLATE = "http://dl.ubnt.com/unifi/{version}/UniFi.unix.zip"
    FILE_NAME_TEMPLATE = "UniFi-{version}.unix.zip"
    GET_LAST_VERSION_URL = "https://www.ubnt.com/download/unifi/unifi-ap-ac-lr/uap-ac-lr/"

    @staticmethod
    def download(version, file_name=None):
        url = Downloader.DOWNLOAD_URL_TEMPLATE.format(version=version)
        r = requests.get(url)
        file_name = file_name or Downloader.FILE_NAME_TEMPLATE.format(version=version)
        with Path(file_name).open('wb') as zip_file:
            zip_file.write(r.content)
        return file_name

    @staticmethod
    def get_last_version():
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome(options=options)
        selenium.get(Downloader.GET_LAST_VERSION_URL)
        selenium.implicitly_wait(3)
        tbody = selenium.find_element_by_css_selector("tbody.js-table-results-software")
        table_rows = tbody.find_elements_by_css_selector("tr")
        first_result_row = table_rows[1]
        newest_controller_name_column = first_result_row.find_element_by_css_selector("td.downloadResults__name")
        last_version = newest_controller_name_column.text.split()[1]
        selenium.quit()
        return last_version


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Downloading unifi controller.')
    parser.add_argument('--version', help='requested version of controller eg. 5.7.20')
    parser.add_argument('-o', help='output file name eg. UniFi-5.7.20.unix.zip')
    args = parser.parse_args()
    if args.version is None:
        print("Required version not provided. Getting last version")
        last_version = Downloader.get_last_version()
        print("Last released version is {version}".format(version=last_version))
        version = last_version
    else:
        version = args.version
    print("Downloading unifi controller {version}".format(version=version))
    output_file = args.o
    file_name = Downloader.download(version, output_file)
    print("Controller saved to file {file_name}".format(file_name=file_name))



