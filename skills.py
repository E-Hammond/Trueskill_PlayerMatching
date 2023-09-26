from trueskill import Rating, quality_1vs1,rate_1vs1, quality,setup
import random
import pandas as pd

# setup(backend='mpmath')
## FrontEnd information needed for the app
matching_info = {
    'random_player_id': 'player6',
    'skillbased_player_id': 'player4'
}
result_info = {
    'player3':'win',
    'player4':'lose'
}


match_player1 = list(result_info.keys())[0]
match_player2 = list(result_info.keys())[1]

df = pd.read_csv('data.csv')
# print(df)


def random_match(player_id):
    matches = []
    players = [key for key in df.players]

    while len(matches) < len(players)-1:
        player1 = player_id
        player2 = random.choice(players)

        # Ensure that player1 and player2 are not the same and have not been matched before
        if player1 != player2 and (player1,player2) not in matches and (player1,player2) not in matches:
            matches.append((player1,player2))

    return matches

# print(random_match(matching_info['random_player_id']))

def skill_matching(df):
    df = df.set_index(['players'])
    player2match = matching_info['skillbased_player_id']
    players = [i for i in df.index if i != player2match]
    matches = list()

    for player in players:
        player_skill,player_conf = df.at[player,'skill_level'],df.at[player,'conf']
        player_rating = Rating(mu=player_skill, sigma=player_conf)
        player2match_skill,player2match_conf = df.at[player2match,'skill_level'],df.at[player2match,'conf']
        player2match_rating = Rating(mu=player2match_skill, sigma=player2match_conf)

        if quality_1vs1(player2match_rating,player_rating)>0.5 : 
            matches.append((player2match,player))
            
        else:
            pass
            
    return matches
    
print(skill_matching(df))

def update_player_ratings(match_results,df):
    df = df.set_index(['players'])
    p1_skill,p1_conf = df.at[match_player1,'skill_level'],df.at[match_player1,'conf']
    p1_rating = Rating(mu=p1_skill, sigma=int(p1_conf))
    p2_skill,p2_conf = df.at[match_player2,'skill_level'],df.at[match_player2,'conf']
    p2_rating = Rating(mu=p2_skill, sigma=int(p2_conf))

    ## Update player ratings based on results
    if result_info[match_player1]=='win':
        player1, player2 = rate_1vs1(p1_rating, p2_rating)
    if result_info[match_player1]=='lose':
        player2, player1 = rate_1vs1(p2_rating, p1_rating)
    else : 
        player1, player2 = rate_1vs1(p1_rating, p2_rating, drawn=True)

    df.loc[df.index==match_player1, 'skill_level'] = player1.mu
    df.loc[df.index==match_player1, 'conf'] = player1.sigma
    df.loc[df.index==match_player2, 'skill_level'] = player2.mu
    df.loc[df.index==match_player2, 'conf'] = player2.sigma
    df = df.reset_index()

    return df


# print(update_player_ratings(result_info,df))

# update_player_ratings(result_info,df).to_csv('data.csv', index=False)