#!/usr/bin/env python3
#
################################################################################
#
# Author: John T. Knowles, RN, RHIA
# Date: October 24, 2018
# Version: 0.1
#
################################################################################
#
'''
SFBulkTA: Automate adding multiple TA instances to SalesForce database
'''
################################################################################
# IMPORT
################################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from credentials import *
import time
import csv
import json
################################################################################
# Login to website
################################################################################

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/home/john/.config/google-chrome/")
chrome_options.add_argument("--kiosk")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://login.salesforce.com")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.clear()
username.send_keys(user)
password.clear()
password.send_keys(pswd)

driver.find_element_by_name("Login").click()

###############################################################################
# Begin looping through CSV and populating data
###############################################################################

csvdatafile = open("hha_data.csv")
salesforcedata = csv.DictReader(csvdatafile)

###############################################################################
# Load campaign information from json file
###############################################################################

with open('campaign.json','r') as campaignfile:
    campaigndata = json.load(campaignfile)

###############################################################################
# Loop through all rows in the CSV file and populate data
###############################################################################

for row in salesforcedata:
    sfurl = "https://na74.salesforce.com/00T/e?title=Call&what_id=a0Ao000000"
    sfurl = sfurl + row['PageURL'] + "&followup=1&tsk5=Technical%20Assistance"

    driver.get(sfurl)

    name = driver.find_element_by_id("tsk2")
    name.send_keys(row['POC'])
    
    duedate = driver.find_element_by_id("tsk4")
    duedate.clear()
    duedate.send_keys(campaigndata['date'])

    endddate = driver.find_element_by_id("00N1J00000EVeQ1")
    endddate.send_keys(campaigndata['date'])

    comments = driver.find_element_by_id("tsk6")
    comments.send_keys(campaigndata['comment'])

    bestpractices = Select(driver.find_element_by_id("00No000000EXDsE"))
    bestpractices.select_by_visible_text(campaigndata['BestPractices'])

    sustainability = Select(driver.find_element_by_id("00No000000EXDsL"))
    sustainability.select_by_visible_text(campaigndata['Sustainability'])

    hbpeval = Select(driver.find_element_by_id("00No000000EXDsI"))
    hbpeval.select_by_visible_text(campaigndata['HBPEvaluation'])

    meds = Select(driver.find_element_by_id("00No000000EXDsJ"))
    meds.select_by_visible_text(campaigndata['Medication'])

    selfmgmt = Select(driver.find_element_by_id("00No000000EXDsC"))
    selfmgmt.select_by_visible_text(campaigndata['SelfManagement'])

    lan = Select(driver.find_element_by_id("00No000000EXDsD"))
    lan.select_by_visible_text(campaigndata['Lan'])

    engagement = Select(driver.find_element_by_id("00No000000EXDsF"))
    engagement.select_by_visible_text(campaigndata['BeneEngagement'])

    literacy = Select(driver.find_element_by_id("00No000000EXDsH"))
    literacy.select_by_visible_text(campaigndata['HealthLiteracy'])

    bpguidelines = Select(driver.find_element_by_id("00No000000EXDsG"))
    bpguidelines.select_by_visible_text(campaigndata['BPGuidelines'])

    hhqi = Select(driver.find_element_by_id("00No000000EXDsK"))
    hhqi.select_by_visible_text(campaigndata['HHQI'])

    resources = Select(driver.find_element_by_id("00No000000EXDsB"))
    resources.select_by_visible_text(campaigndata['EdResources'])

###############################################################################
# Find and click the Save button
###############################################################################
    
    driver.find_element_by_name("save").click()
driver.quit()
