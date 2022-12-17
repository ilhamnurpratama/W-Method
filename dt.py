# Decision Tree
# Created by Ilham Nur Pratama - 2106663282
# Version 1.0

# Module Used
import time as tm
import pandas as pd

startTime = tm.time() # Start computation time
def minDT():    
        # Define the data for the decision tree
        data = {'choice': ['salaryA', 'salaryB','salaryA','salaryB'],
                'payoff': [200, 250,200,250],
                'probability': [0.55, 0.45,0.45,0.55]}
        df = pd.DataFrame(data)

        # Calculate the expected payoff for each choice
        df['expected_payoff'] = df['payoff'] * df['probability']

        # Find the maximum expected payoff
        min_expected_payoff = df['expected_payoff'].min()

        # Store the maximum expected payoff as the output for the first decision tree
        df['first_decision_tree'] = min_expected_payoff


        # Define the 2 data for the decision tree **DECISION
        data2 = {'choice': ['hybrid', 'nonHybrid'],
                'payoff': [112.5+70, min_expected_payoff+20],
                'probability': [1,0]}
        df2 = pd.DataFrame(data2)

        # Calculate the expected payoff for each choice
        df2['expected_payoff'] = df2['payoff'] * df2['probability']

        # Find the maximum expected payoff
        min_expected_payoff2 = df2[df2['expected_payoff'] > 0]['expected_payoff'].min()

        # Define the 3 data for the decision tree
        data3 = {'choice': ['hargaTerjangkau', 'hargaTerjangkauSparepartImitasi','sparePartOriginal','sparePartOriginalMahal',
        'hargaTerjangkau', 'hargaTerjangkauSparepartImitasi','sparePartOriginal','sparePartOriginalMahal'],
                'payoff': [min_expected_payoff2, min_expected_payoff2,min_expected_payoff2,min_expected_payoff2,
                min_expected_payoff2,min_expected_payoff2,min_expected_payoff2,min_expected_payoff2],
                'probability': [0.65,0.35,0.53,0.47,0.66,0.34,0.67,0.33]}
        df3 = pd.DataFrame(data3)

        # Calculate the expected payoff for each choice
        df3['expected_payoff'] = df3['payoff'] * df3['probability']

        # Find the maximum expected payoff
        min_expected_payoff3 = df3[df3['expected_payoff'] > 0]['expected_payoff'].min()

        # Define the 4 data for the decision tree
        data4 = {'choice': ['spBanyak','spSedikit','spBanyak','spSedikit'],
                'payoff': [min_expected_payoff3+40,min_expected_payoff3+50,min_expected_payoff3+50,min_expected_payoff3+70],
                'probability': [0.75,0.25,0.72,0.28]}
        df4 = pd.DataFrame(data4)

        # Calculate the expected payoff for each choice
        df4['expected_payoff'] = df4['payoff'] * df4['probability']

        # Find the maximum expected payoff
        min_expected_payoff4 = df4[df4['expected_payoff'] > 0]['expected_payoff'].min()

        # Define the 5 data for the decision tree **DECISION
        data5 = {'choice': ['spBanyak','spSedikit'],
                'payoff': [min_expected_payoff4,min_expected_payoff4],
                'probability': [0,1]}
        df5 = pd.DataFrame(data5)

        # Calculate the expected payoff for each choice
        df5['expected_payoff'] = df5['payoff'] * df5['probability']

        # Find the maximum expected payoff
        min_expected_payoff5 = df5[df5['expected_payoff'] > 0]['expected_payoff'].min()

        # Define the 6 data for the decision tree
        data6 = {'choice': ['hargaTurun','hargaTurunAsuransiSedikit','hargaNaik','hargaNaikAsuransiBertambah',
        'hargaTurun','hargaTurunAsuransiSedikit','hargaNaik','hargaNaikAsuransiBertambah'],
                'payoff': [min_expected_payoff5,min_expected_payoff5,min_expected_payoff5,min_expected_payoff5,
                min_expected_payoff5,min_expected_payoff5,min_expected_payoff5,min_expected_payoff5],
                'probability': [0.6,0.4,0.3,0.7,0.45,0.55,0.6,0.4]}
        df6 = pd.DataFrame(data6)

        # Calculate the expected payoff for each choice
        df6['expected_payoff'] = df6['payoff'] * df6['probability']

        # Find the maximum expected payoff
        min_expected_payoff6 = df6[df6['expected_payoff'] > 0]['expected_payoff'].min()

        # Print the choice with the maximum expected payoff
        print("Choice with minimum expected payoff:", df6[df6['expected_payoff'] == min_expected_payoff6]['choice'].values[0])
        print("Choice with minimum expected payoff:", df6[df6['expected_payoff'] == min_expected_payoff6]['expected_payoff'].values[0])
        print(df6['expected_payoff'])

        # Define the 7 data for the decision tree
        data7 = {'choice': ['cash','credit','cash','credit'],
                'payoff': [min_expected_payoff5,min_expected_payoff5,min_expected_payoff5,min_expected_payoff5],
                'probability': [0.3,0.7,0.6,0.4]}
        df7 = pd.DataFrame(data7)

        # Calculate the expected payoff for each choice
        df7['expected_payoff'] = df7['payoff'] * df7['probability']

        # Find the maximum expected payoff
        min_expected_payoff7 = df7[df7['expected_payoff'] > 0]['expected_payoff'].min()

        # Define the 8 data for the decision tree **DECISION
        data8 = {'choice': ['cash','credit'],
                'payoff': [min_expected_payoff6,min_expected_payoff6+90],
                'probability': [1,0]}
        df8 = pd.DataFrame(data8)

        # Calculate the expected payoff for each choice
        df8['expected_payoff'] = df8['payoff'] * df8['probability']

        # Find the maximum expected payoff
        min_expected_payoff8 = df8[df8['expected_payoff'] > 0]['expected_payoff'].min()

        # Print the choice with the maximum expected payoff
        print('\nFINAL RESULT')
        print('\n====================================================================================================')
        print("Choice with minimum expected payoff:", df[df['expected_payoff'] == min_expected_payoff]['choice'].values[0])
        print("Choice with minimum expected payoff:", df8[df8['expected_payoff'] == min_expected_payoff8]['expected_payoff'].values[0])
        print(df8['expected_payoff'])

def maxDT():
        # Define the data for the decision tree
        data = {'choice': ['salaryA', 'salaryB','salaryA','salaryB'],
                'payoff': [10, 15,10,15],
                'probability': [0.55, 0.45,0.45,0.55]}
        df = pd.DataFrame(data)

        # Calculate the expected payoff for each choice
        df['expected_payoff'] = df['payoff'] * df['probability']

        # Find the maximum expected payoff
        max_expected_payoff = df['expected_payoff'].max()

        # Store the maximum expected payoff as the output for the first decision tree
        df['first_decision_tree'] = max_expected_payoff


        # Define the 2 data for the decision tree **DECISION
        data2 = {'choice': ['hybrid', 'nonHybrid'],
                'payoff': [112.5+70, max_expected_payoff+20],
                'probability': [1,0]}
        df2 = pd.DataFrame(data2)

        # Calculate the expected payoff for each choice
        df2['expected_payoff'] = df2['payoff'] * df2['probability']

        # Find the maximum expected payoff
        max_expected_payoff2 = df2[df2['expected_payoff'] > 0]['expected_payoff'].max()

        # Define the 3 data for the decision tree
        data3 = {'choice': ['hargaTerjangkau', 'hargaTerjangkauSparepartImitasi','sparePartOriginal','sparePartOriginalMahal',
        'hargaTerjangkau', 'hargaTerjangkauSparepartImitasi','sparePartOriginal','sparePartOriginalMahal'],
                'payoff': [max_expected_payoff2, max_expected_payoff2,max_expected_payoff2,max_expected_payoff2,
                max_expected_payoff2,max_expected_payoff2,max_expected_payoff2,max_expected_payoff2],
                'probability': [0.65,0.35,0.53,0.47,0.66,0.34,0.67,0.33]}
        df3 = pd.DataFrame(data3)

        # Calculate the expected payoff for each choice
        df3['expected_payoff'] = df3['payoff'] * df3['probability']

        # Find the maximum expected payoff
        max_expected_payoff3 = df3[df3['expected_payoff'] > 0]['expected_payoff'].max()

        # Define the 4 data for the decision tree
        data4 = {'choice': ['spBanyak','spSedikit','spBanyak','spSedikit'],
                'payoff': [max_expected_payoff3+40,max_expected_payoff3+50,max_expected_payoff3+50,max_expected_payoff3+70],
                'probability': [0.75,0.25,0.72,0.28]}
        df4 = pd.DataFrame(data4)

        # Calculate the expected payoff for each choice
        df4['expected_payoff'] = df4['payoff'] * df4['probability']

        # Find the maximum expected payoff
        max_expected_payoff4 = df4[df4['expected_payoff'] > 0]['expected_payoff'].max()

        # Define the 5 data for the decision tree **DECISION
        data5 = {'choice': ['spBanyak','spSedikit'],
                'payoff': [max_expected_payoff4,max_expected_payoff4],
                'probability': [0,1]}
        df5 = pd.DataFrame(data5)

        # Calculate the expected payoff for each choice
        df5['expected_payoff'] = df5['payoff'] * df5['probability']

        # Find the maximum expected payoff
        max_expected_payoff5 = df5[df5['expected_payoff'] > 0]['expected_payoff'].max()

        # Define the 6 data for the decision tree
        data6 = {'choice': ['hargaTurun','hargaTurunAsuransiSedikit','hargaNaik','hargaNaikAsuransiBertambah',
        'hargaTurun','hargaTurunAsuransiSedikit','hargaNaik','hargaNaikAsuransiBertambah'],
                'payoff': [max_expected_payoff5,max_expected_payoff5,max_expected_payoff5,max_expected_payoff5,
                max_expected_payoff5,max_expected_payoff5,max_expected_payoff5,max_expected_payoff5],
                'probability': [0.6,0.4,0.3,0.7,0.45,0.55,0.6,0.4]}
        df6 = pd.DataFrame(data6)

        # Calculate the expected payoff for each choice
        df6['expected_payoff'] = df6['payoff'] * df6['probability']

        # Find the maximum expected payoff
        max_expected_payoff6 = df6[df6['expected_payoff'] > 0]['expected_payoff'].max()

        # Print the choice with the maximum expected payoff
        print("Choice with maximum expected payoff:", df6[df6['expected_payoff'] == max_expected_payoff6]['choice'].values[0])
        print("Choice with maximum expected payoff:", df6[df6['expected_payoff'] == max_expected_payoff6]['expected_payoff'].values[0])
        print(df6['expected_payoff'])

        # Define the 7 data for the decision tree
        data7 = {'choice': ['cash','credit','cash','credit'],
                'payoff': [max_expected_payoff5,max_expected_payoff5,max_expected_payoff5,max_expected_payoff5],
                'probability': [0.3,0.7,0.6,0.4]}
        df7 = pd.DataFrame(data7)

        # Calculate the expected payoff for each choice
        df7['expected_payoff'] = df7['payoff'] * df7['probability']

        # Find the maximum expected payoff
        max_expected_payoff7 = df7[df7['expected_payoff'] > 0]['expected_payoff'].max()

        # Define the 8 data for the decision tree **DECISION
        data8 = {'choice': ['cash','credit'],
                'payoff': [max_expected_payoff6,max_expected_payoff6+90],
                'probability': [1,0]}
        df8 = pd.DataFrame(data8)

        # Calculate the expected payoff for each choice
        df8['expected_payoff'] = df8['payoff'] * df8['probability']

        # Find the maximum expected payoff
        max_expected_payoff8 = df8[df8['expected_payoff'] > 0]['expected_payoff'].max()

        # Print the choice with the maximum expected payoff
        print('\nFINAL RESULT')
        print('\n====================================================================================================')
        print("Choice with maximum expected payoff:", df[df['expected_payoff'] == max_expected_payoff]['choice'].values[0])
        print("Choice with maximum expected payoff:", df8[df8['expected_payoff'] == max_expected_payoff8]['expected_payoff'].values[0])
        print(df8['expected_payoff'])

fungsiMinMax = int(input("Enter the function that system will solve (1=max, 2=min): ") )

if fungsiMinMax == 1:
        maxDT()
elif fungsiMinMax == 2:
        minDT()

endTime = tm.time() # Finish computation time
processTime = endTime - startTime
print('Time elapse for this calculation: %.3f'%processTime,' seconds \n')