from pydfs_lineup_optimizer import Site, Sport, get_optimizer, CSVLineupExporter
from pydfs_lineup_optimizer.stacks import TeamStack, PositionsStack, PlayersGroup, Stack

LINES = 30
#WR_TIER_1 = {'Kahlil Lewis', 'Rashad Ross', 'Mekale McKay', 'Jeff Badet', 'Flynn Nagel'}


optimizer = get_optimizer(Site.DRAFTKINGS_CAPTAIN_MODE, Sport.FOOTBALL)
optimizer.load_players_from_csv("DKSalaries1pmshowdown.csv")
#optimizer.add_stack(TeamStack(3))
#optimizer.add_stack(TeamStack(3, for_positions=['QB', 'WR']))
#optimizer.add_stack(PositionsStack(['QB', 'WR', 'WR']))
#optimizer.force_positions_for_opposing_team(('QB', 'WR'))
#optimizer.restrict_positions_for_same_team(('RB', 'RB'))
#optimizer.restrict_positions_for_opposing_team(['QB'], ['DST'])
optimizer.set_deviation(0.05, 0.3)
optimizer.set_max_repeating_players(5)
for player in optimizer.players:
    if player.fppg < 1:
        optimizer.remove_player(player)
#mekale = optimizer.get_player_by_name('Phillip Walker')
#optimizer.add_player_to_lineup(mekale)

    #dc_wrs = []
#for name in ['Eli Rogers', 'Rashad Ross', 'Deandre Thompkins', 'Malachi Dupre']:
#    for p in optimizer.find_players(name):
#        dc_wrs.append(p)
#group = PlayersGroup(dc_wrs, min_from_group=1)
#optimizer.add_stack(Stack([cardale, group]))
optimizer.restrict_positions_for_opposing_team(['K'], ['K'])

exporter = CSVLineupExporter(optimizer.optimize(LINES, randomness=True, generate_exposures=True))
exporter.export('result1pm.csv')
optimizer.player_exposures.write_exposures_csv(total_lineups=LINES, csv_filename='exposures1pm.csv')
