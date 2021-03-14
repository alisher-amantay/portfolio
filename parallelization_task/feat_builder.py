
def feat_var(timesT, df_data):
    res_1_9 = []
    for oneT in timesT:
        day1 = df_data[(df_data['ActionTime'] > (df_data['ActionTime'][oneT] - 86400))&
                         (df_data['ActionTime'] < df_data['ActionTime'][oneT])&
                         (df_data['ProfileID'] == df_data['ProfileID'][oneT])]
        day3 = df_data[(df_data['ActionTime'] < (df_data['ActionTime'][oneT] - 86400))&
                         (df_data['ActionTime'] > (df_data['ActionTime'][oneT]-259200))&
                         (df_data['ProfileID'] == df_data['ProfileID'][oneT])]
        did_action = df_data[(df_data['ProfileID'] == df_data['ProfileID'][oneT])&
                         (df_data['ActionTime'] < df_data['ActionTime'][oneT])&
                         (df_data['ActionID'].isin([0, 4, 5]))]
        if len(did_action.index) < 2:
            feat8 = float('NaN')
        else:
            feat8 = int((did_action.iloc[-1]['ActionTime'] - did_action.iloc[0]['ActionTime'])/86400)

        if len(did_action.index) == 0:
            feat9 = float('NaN')
        else:
            feat9 = int((df_data['ActionTime'][oneT] - did_action.iloc[-1]['ActionTime'])/86400)

        res_1_9.append([
                #feature 1. доставки за 24 часа
                int(len(day1[df_data['ActionID'] == 3].index)),
                #feature 2. открытия за 24 часа
                int(len(day1[df_data['ActionID'] == 4].index)),
                #feature 3. клики за 24 часа
                int(len(day1[df_data['ActionID'] == 5].index)),
                #feature 4. доставки за 3 дня
                int(len(day3[df_data['ActionID'] == 3].index)),
                #feature 5. открытия за 3 дня
                int(len(day3[df_data['ActionID'] == 4].index)),
                #feature 6. клики за 3 дня
                int(len(day3[df_data['ActionID'] == 5].index)),
                #feature 7. количество уникальных дней активности - надо доработать
                int(len(did_action['ActionTimeDt'].unique())),
                #feature 8. макс дней между действиями
                feat8,
                #feature 9. дней между действием и доставкой
                feat9
        ])
    return res_1_9
