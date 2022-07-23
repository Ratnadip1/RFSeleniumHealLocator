import os
from os import path

from src.SeleniumHealLocator.keywords.ManageInformation import ManageInformation


def testInitiateHealingProcessFolderOnlyXml():
    try:
        manage_info = ManageInformation()
        manage_info.initiate_Healing_Process('Test')
        test_folder = os.getcwd() + os.sep + 'Test'
        assert True, path.exists(test_folder)
        test_file = path.join(test_folder, 'elements.xml')
        assert True, path.isfile(test_file)
    except AssertionError as assertError:
        print(assertError)
        raise assertError


def testInitiateHealingProcessFolder_FileNameXml():
    try:
        manage_info = ManageInformation()
        manage_info.initiate_Healing_Process('Test', 'newdoc')
        test_folder = os.getcwd() + os.sep + 'Test'
        assert True, path.exists(test_folder)
        test_file = path.join(test_folder, 'newdoc.xml')
        assert True, path.isfile(test_file)
    except AssertionError as assertError:
        print(assertError)
        raise assertError


def testInitiateHealingProcessInvalid_Format():
    try:
        manage_info = ManageInformation()
        manage_info.initiate_Healing_Process('Test', 'newdoc', '.xls')

    except Exception as expectedException:
        print(expectedException)
        raise AssertionError('Invalid Format')
