from jira_download_driver import DriverBuilder
from jira_app_creator import NewAPP
from jira_analyser_database import VariablesDatabase, NoDeadlineDatabase, ReleaseDatabase, TodayDatabase, DataDatabase
import pandas as pd

def main():
    #variables
    download_path = r"C:\Users\WUU7FE\OneDrive - Robert Bosch GmbH\excel"
    #r"C:\Users\WUU7FE\Documents\Wu\FROP\excel"
    url = 'https://rb-tracker.bosch.com/tracker08/sr/jira.issueviews:searchrequest-excel-current-fields/98761/SearchRequest-98761.xls'

    #*download JIRA_Report from jira filter to the assigned file path
    driver= DriverBuilder(download_path)
    driver.download_from_friver(url)

if __name__ == "__main__":
    main()
