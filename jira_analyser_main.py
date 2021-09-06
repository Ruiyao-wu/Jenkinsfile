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
    #* copy the daily download data to Jira_Export sheet and return WB wkbAnalysis and a dataframe of the download value
    app = NewAPP(download_path)
    wkbAnalysis, DFJiraExp = app.copy_sheet()
    #*get sheet 
    shtReleaseMatch = wkbAnalysis.sheets['Release_Matching']
    shtVars = wkbAnalysis.sheets['Variables']
    shtToday = wkbAnalysis.sheets['Today']
    shtData = wkbAnalysis.sheets['Data']
    #shtNoDeadline = wkbAnalysis.sheets['Ticket_noDeadline']
    #* update Data of WB wkbAnalysis
    print('------updating the data of Jira_Analyser-------')
    Var = VariablesDatabase(shtVars)
    Var.Update_Variables(DFJiraExp)
    # Ticket_Non = NoDeadlineDatabase(shtNoDeadline)
    # Ticket_Non.Update_TicketnoDeadline(DFJiraExp)
    # Ticket_Non.Update_RealeasenoDeadline()
    Rematch = ReleaseDatabase(shtReleaseMatch)
    Rematch.Update_Rematch(DFJiraExp)
    Today = TodayDatabase(shtToday)
    Today.Update_Today(Var.sht)
    Data = DataDatabase(shtData)
    Data.Update_Database(Today.sht)
    #*close the app
    app.close_app(wkbAnalysis)


if __name__ == "__main__":
    main()