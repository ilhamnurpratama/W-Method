# W Program 
# Created by Ilham Nur Pratama
# Version 1.1

# Module Used
import pandas as pd

# Extract Dataframe
mData = pd.read_csv('data.csv')
mData = mData.set_index(mData['id'])
oData = pd.read_csv('output.csv')
oData = oData.set_index(oData['oid'])

# Application UI
print('W Method Program')
print('Version 2.0')
print('Kelompok 7')
print('Riset Operasi Lanjut - Teknik Industri S2UI')
print('======================================================================')

# Type Conversion
mData['additionalPayoff'] = mData['additionalPayoff'].astype(float)

# Query Data
dataOutput = mData.loc[mData['type'] == 'output']
nodeEvent = mData.loc[mData['type'] == 'event']
nodeDecision = mData.loc[mData['type'] == 'decision']

# Main Logic
nullColumn = mData.loc[mData['parent'].isnull()]
notNullColumn = mData.loc[mData['parent'].notnull()]

for i in notNullColumn:
    # Calculating Logic
    mData['expectedPayoff'] = mData['RawPayoff'] * mData['probabilityBranch']
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