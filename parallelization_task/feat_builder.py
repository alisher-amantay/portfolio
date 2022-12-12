SECONDS_DAY = 86400

def feat_var(timesT, df_data):
    # setting variables
    periods = [day1, day3] # 1 and 3 day periods
    # mapping actions and action ids
    actions_map = {'delivery': 3, 'opening': 4, 'clicks': 5}

    res_1_9 = []
    for oneT in timesT:
        day1 = df_data[(df_data['ActionTime'] > (df_data['ActionTime'][oneT] - SECONDS_DAY)) &
                         (df_data['ActionTime'] < df_data['ActionTime'][oneT]) &
                         (df_data['ProfileID'] == df_data['ProfileID'][oneT])]
        day3 = df_data[(df_data['ActionTime'] < (df_data['ActionTime'][oneT] - SECONDS_DAY)) &
                         (df_data['ActionTime'] > (df_data['ActionTime'][oneT] - SECONDS_DAY * 3)) &
                         (df_data['ProfileID'] == df_data['ProfileID'][oneT])]
        did_action = df_data[(df_data['ProfileID'] == df_data['ProfileID'][oneT]) &
                         (df_data['ActionTime'] < df_data['ActionTime'][oneT]) &
                         (df_data['ActionID'].isin([0, 4, 5]))]
        # features 1-6: delivery, openings and clicks over specified periods
        features = [int(len(period_stats[df_data['ActionID'] == action_id].index))
                    for period_stats in periods
                    for action_id in actions_map.values()]

        # feature 7. count of unique days of having interactions
        features.append(int(len(did_action['ActionTimeDt'].unique())))
        
        # feature 8
        if len(did_action.index) < 2:
            feat_8 = float('NaN')
        else:
            feat_8 = int((did_action.iloc[-1]['ActionTime'] - did_action.iloc[0]['ActionTime']) / SECONDS_DAY)
        features.append(feat_8)
        
        # feature 9. days between interaction and delivery
        if len(did_action.index) == 0:
            feat_9 = float('NaN')
        else:
            feat_9 = int((df_data['ActionTime'][oneT] - did_action.iloc[-1]['ActionTime']) / SECONDS_DAY)
        features.append(feat_9)

        res_1_9.append(features)
    return res_1_9
