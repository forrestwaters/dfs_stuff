from pydfs_lineup_optimizer import Site, Sport, get_optimizer, CSVLineupExporter
from pydfs_lineup_optimizer.stacks import TeamStack, PositionsStack

LINES = 19

optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASEBALL)
#optimizer = get_optimizer(Site.DRAFTKINGS_CAPTAIN_MODE, Sport.BASEBALL)
optimizer.load_players_from_csv("DKSalaries.csv")
optimizer.set_deviation(0.01, 0.05)
#optimizer.add_stack(TeamStack(4))
#zg = optimizer.get_player_by_name('Zack Greinke')
#optimizer.add_player_to_lineup(zg)
#optimizer.add_stack(TeamStack(4, for_positions=['C', 'OF', '1B', '2B', '3B', 'SS']))
#optimizer.restrict_positions_for_opposing_team(['P'], ['C', 'OF', '1B', '2B', '3B', 'SS'])
optimizer.set_max_repeating_players(6)
for player in optimizer.players:
    if player.fppg < 1:
        optimizer.remove_player(player)
exporter = CSVLineupExporter(optimizer.optimize(LINES, randomness=True, generate_exposures=True))
exporter.export('result.csv')
optimizer.player_exposures.write_exposures_csv(total_lineups=LINES)
