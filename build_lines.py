from pydfs_lineup_optimizer import Site, Sport, get_optimizer, CSVLineupExporter
from pydfs_lineup_optimizer.stacks import TeamStack, PositionsStack, PlayersGroup, Stack

LINES = 40
#WR_TIER_1 = {'Kahlil Lewis', 'Rashad Ross', 'Mekale McKay', 'Jeff Badet', 'Flynn Nagel'}


optimizer = get_optimizer(Site.DRAFTKINGS, Sport.CANADIAN_FOOTBALL)
optimizer.load_players_from_csv("DKSalaries.csv")
#lineups = optimizer.load_lineups_from_csv("DKSalaries.csv")
optimizer.add_stack(TeamStack(3))
#optimizer.add_stack(TeamStack(3, for_positions=['QB', 'WR']))
#optimizer.add_stack(PositionsStack(['QB', 'WR']))
#optimizer.force_positions_for_opposing_team(('QB', 'WR'))

#optimizer.add_stack(PositionsStack(['QB', 'WR']))
optimizer.restrict_positions_for_same_team(('RB', 'RB'))
optimizer.force_positions_for_opposing_team(('QB', 'WR'))
#optimizer.force_positions_for_opposing_team(('QB', 'WR'))

#optimizer.add_stack(TeamStack(2, for_positions=['QB', 'WR'], for_teams=['DAL', 'HOU', 'DC']))
optimizer.restrict_positions_for_opposing_team(['QB'], ['DST'])
optimizer.set_deviation(0.02, 0.35)
optimizer.set_max_repeating_players(5)
for player in optimizer.players:
    if player.fppg < 1:
        optimizer.remove_player(player)
    elif 'WR' in player.positions:
        player.min_deviation = 0.25
        player.max_deviation = 0.55
    elif 'QB' in player.positions:
        player.min_deviation = 0.15
        player.max_deviation = 0.35
#mekale = optimizer.get_player_by_name('Mekale McKay')
#optimizer.add_player_to_lineup(mekale)
exporter = CSVLineupExporter(optimizer.optimize(LINES, randomness=True, generate_exposures=True))
exporter.export('result.csv')
optimizer.player_exposures.write_exposures_csv(total_lineups=LINES)


#exporter = CSVLineupExporter(optimizer.optimize_lineups(lineups, generate_exposures=True))
#exporter.export('result.csv')
#optimizer.player_exposures.write_exposures_csv(total_lineups=LINES)
