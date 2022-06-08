import pandas as pd

REFERENCE_VARIABLE = ["Country Name","Country Code","Region"]


def create_dataframe_from_given_dataframe_and_variable(from_dataframe, variable):
    """ Creates a data frame which contains only given variable's info
    
    Args:
        from_dataframe (pd.DataFrame): data source
        variable (str): variable to extract
    
    Returns
        pd.DataFrame: new data frame with variable's info
    
    """
    dataframe = from_dataframe[from_dataframe["Indicator Name"] == variable]
    print(str(len(dataframe)) + " rows in dataframe")
    print(str(len(dataframe.columns)) + " columns in dataframe")
    print(dataframe.columns)
    return dataframe
     
def create_dataframe_from_csv_file(csv_file):
    """ Creates a data frame from given csv file
    
    Args:
        csv_file (.csv): data source
    
    Returns
        pd.DataFrame: new data frame with csv file's data
    
    """
    dataframe = pd.read_csv(csv_file, sep=',')
    print(str(len(dataframe)) + " rows in dataframe")
    print(str(len(dataframe.columns)) + " columns in dataframe")
    print(dataframe.columns)
    return dataframe 
    
def select_columns(dataframe, start_date, end_date):
    """ Filters columns of given data frame
    
    Args:
        dataframe (pd.DataFrame): data source
        start_date (str) : start column's variable
        end_date (str) : end colum's variable
    
    Returns
        pd.DataFrame: new data frame with filtered columns
    
    """
    return dataframe[REFERENCE_VARIABLE + list(dataframe.loc[:, start_date:end_date])]
    
def display_missing_data(dataframe, column_name):
    """ Prints percentage of missing data for given column in given data frame 
    
    Args:
        dataframe (pd.DataFrame): data source
        column_name (str): column to compute
    
    Returns
        Prints percentage of missing data for given column and prints list of missing data's indexes 
    
    """
    list=[]
    for index, line in dataframe.iterrows():
        if pd.isna(line[column_name]):
            list.append(index)
    missing_Percentage = (len(list)/len(dataframe))*100 
    print("-- Missing values' index for " + column_name + " :")   
    print(str(missing_Percentage) + "%")
    print(list)
    
def display_missing_data_from_dataframe(dataframe):
    """ Prints percentage of missing data for every column in given data frame 
    
    Args:
        dataframe (pd.DataFrame): data source
    
    Returns
        Prints percentage of missing data for every column and prints list of its indexes for each 
        column
    
    """
    for column in dataframe.columns:
        display_missing_data(dataframe, column) 
 

            




