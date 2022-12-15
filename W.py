# W Program 
# Created by Ilham Nur Pratama - 2106663282
# Version 1.3

# Module Used
import pandas as pd
import mysql.connector as sql
import numpy as np

'''
# Open this command if want to use database
# Database connection
cnx = sql.connect(
    user="root",
    password="YOURPASSWORD",
    host="localhost",
    database="rol"
)

cursor = cnx.connect()

# Database Extract
Data = pd.read_sql("SELECT * FROM data",cnx)
oData = pd.read_sql("SELECT * FROM output",cnx)
mData = pd.merge(Data,oData,left_on='type',right_on='type',how='outer')
# drop duplicated column
mData = mData.drop([
                'branch_y'],axis=1)
# rename column
mData = mData.rename(columns = {'branch_x':'branch'})
'''

# Open this command if want to use csv data source
# Extract Dataframe
rData = pd.read_csv('data.csv')
rData = rData.set_index(rData['id'])
oData = pd.read_csv('output.csv')
oData = oData.set_index(oData['oid'])
cData = pd.read_csv('criteria.csv')
cData = cData.set_index(cData['cid'])
roData = pd.merge(rData,oData,left_on='oid',right_index=True,how='outer')
mData = pd.merge(roData,cData,left_on='cid',right_index=True,how='outer')

# drop duplicated & rename column
roData = roData.drop(['oid_y',
'type_y',
'branch_y',
'oid_x'],axis=1)

roData = roData.rename(columns = {'branch_x':'branch',
'type_x':'type'})

mData = mData.drop(['oid_y',
'type_y',
'branch_y',
'criteria_y',
'cid_y',
'cid_x',
'oid_x'],axis=1)

mData = mData.rename(columns = {'criteria_x':'criteria',
'branch_x':'branch',
'type_x':'type'})

# Application UI
print('W Method Program')
print('Version 1.2')
print('Group 7')
print('Riset Operasi Lanjut - Teknik Industri S2UI')
print('====================================================================== \n')

# Data Cleansing, Scrapping, query
mData['additionalPayoff'] = mData['additionalPayoff'].astype(float)
mData['probabilityBranch'] = pd.to_numeric(mData['probabilityBranch'],errors='coerce')
notNullColumn = mData.loc[mData['parent'].notnull()]
countCriteria = mData['criteria'].nunique()
rBobot = []
decisionArray = []

# Inputs and Options
# Input function min max
fungsiMinMax = int(input("Enter the function that system will solve (1=max, 2=min): ") )
print('Number of criterias: %i'%countCriteria)
for i in cData['cid']:
    rankBobot = float(input('Enter the priority of %i criteria: '%i))
    rBobot.append(rankBobot)
cData = cData.loc[:, 'rank'] = pd.DataFrame(rBobot, index=cData['cid'])

# Input Decision
filteredDid
for i in mData['did']:
    decisionChoosen = int(input("Enter your decision for decision #%i: "%i))
    decisionArray.append(decisionChoosen)

# Function Definition
def maxDT():
    for i in notNullColumn:
        # Calculating Logic
        mData['expectedPayoff'] = mData['rawPayoff'] * mData['probabilityBranch']
        mData['finalPayoff'] = mData['expectedPayoff'] + mData['additionalPayoff']
        
        # Grouping Logic
        mData_value = mData.groupby(['type','parent'])['id','finalPayoff','branch'].max()
        mData_value = mData_value.reset_index()
        mData_value = mData_value.set_index(mData_value['parent'])
        mData['finalPayoff']=(mData_value['finalPayoff'])
        mData['finalBranch']=(mData_value['branch'])
        
        # null Value calculation
        nullRows = mData.loc[mData['parent'].notnull()]
        
        # Calculating Logic
        nullRows['expectedPayoff'] = nullRows['finalPayoff'] * nullRows['probabilityBranch']
        nullRows['finalPayoff'] = nullRows['expectedPayoff'] + nullRows['additionalPayoff']
        
        # Grouping Logic
        nullRows_value = nullRows.groupby(['type','parent'])['id','finalPayoff','branch'].max()
        nullRows_value = nullRows_value.reset_index()
        nullRows_value = nullRows_value.set_index(nullRows_value['parent'])
        
        # Merge dataframe
        mdf = pd.merge(mData,nullRows_value,left_index=True,right_index=True,how='outer')
        mdf['finalPayoff_x'] = mdf['finalPayoff_x'].fillna(0)
        mdf['finalPayoff_y'] = mdf['finalPayoff_y'].fillna(0)
        mdf['finalPayoff'] = mdf.apply(lambda x: x['finalPayoff_x'] + x['finalPayoff_y'],axis=1)

        #drop duplicated column
        mdf = mdf.drop(['finalPayoff_x',
                        'finalPayoff_y',
                        'parent_y',
                        'id_y',
                        'branch_y',
                        'type_y'],axis=1)

def minDT():
    for i in notNullColumn:
        # Calculating Logic
        mData['expectedPayoff'] = mData['rawPayoff'] * mData['probabilityBranch']
        mData['finalPayoff'] = mData['expectedPayoff'] + mData['additionalPayoff']
        
        # Grouping Logic
        mData_value = mData.groupby(['type','parent'])['id','finalPayoff','branch'].min()
        mData_value = mData_value.reset_index()
        mData_value = mData_value.set_index(mData_value['parent'])
        mData['finalPayoff']=(mData_value['finalPayoff'])
        mData['finalBranch']=(mData_value['branch'])
        
          
        # null Value calculation
        nullRows = mData.loc[mData['parent'].notnull()]
        
        # Calculating Logic
        nullRows['expectedPayoff'] = nullRows['finalPayoff'] * nullRows['probabilityBranch']
        nullRows['finalPayoff'] = nullRows['expectedPayoff'] + nullRows['additionalPayoff']
        
        # Grouping Logic
        nullRows_value = nullRows.groupby(['type','parent'])['id','finalPayoff','branch'].min()
        nullRows_value = nullRows_value.reset_index()
        nullRows_value = nullRows_value.set_index(nullRows_value['parent'])
        
        # Merge dataframe
        mdf = pd.merge(mData,nullRows_value,left_index=True,right_index=True,how='outer')
        mdf['finalPayoff_x'] = mdf['finalPayoff_x'].fillna(0)
        mdf['finalPayoff_y'] = mdf['finalPayoff_y'].fillna(0)
        mdf['finalPayoff'] = mdf.apply(lambda x: x['finalPayoff_x'] + x['finalPayoff_y'],axis=1)

        #drop duplicated column
        mdf = mdf.drop(['finalPayoff_x',
                        'finalPayoff_y',
                        'parent_y',
                        'id_y',
                        'branch_y',
                        'type_y'],axis=1)

# Main Logic
if fungsiMinMax == 1:
    maxDT()
elif fungsiMinMax == 2:
    minDT()