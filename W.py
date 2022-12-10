# W Program 
# Created by Ilham Nur Pratama
# Version 1.0

# Module Used
import pandas as pd

# List Used
namaOutput_list = []
nilaiOutput_list = []

# Extract Dataframe
# Data = pd.read_csv('data.csv')
mData = pd.read_csv('data.csv')
#mData = mData.set_index(mData['id'])
oData = pd.read_csv('output.csv')
oData = oData.set_index(oData['oid'])

# Application UI
print('W Method Program')
print('Version 1.0')
print('Kelompok 7')
print('Riset Operasi Lanjut - Teknik Industri S2UI')
print('======================================================================')

'''
# Combine Data
mData = data.merge(dataPayoff, how='outer', on='Branch')

# Select Function
fungsi = int(input('Masukan fungsi yang akan anda pilih (Max = 1, Min = 2): '))
'''

# Type Conversion
mData['additionalPayoff'] = mData['additionalPayoff'].astype(float)

# Query Data
dataOutput = mData.loc[mData['type'] == 'output']
nodeEvent = mData.loc[mData['type'] == 'event']
nodeDecision = mData.loc[mData['type'] == 'decision']

# First Step : Output Calculation
# Calculating Logic
mData['expectedPayoff'] = mData['RawPayoff'] * mData['probabilityBranch']
mData['finalPayoff'] = mData['expectedPayoff'] + mData['additionalPayoff']

# Grouping Logic
mData_valueOutput = mData.groupby(['type','parent'])['id','finalPayoff'].max()
mData_valueOutput = mData_valueOutput.reset_index()

# Merging with parent
mpData = pd.merge(mData,mData_valueOutput, left_on='id', right_on='parent')
mpData.set_index('id_x')
# mpData.to_csv('mpData.csv')

# Event Calculation
mpData['expectedPayoff'] = mpData['finalPayoff_y'] * mpData['probabilityBranch']
mpData['finalPayoff'] = mpData['expectedPayoff'] + mpData['additionalPayoff']
mpData_eventOutput = mpData.groupby(['type_x'])['id_x','finalPayoff'].max()
mpData_eventOutput = mpData_eventOutput.reset_index()
print(mpData_eventOutput)