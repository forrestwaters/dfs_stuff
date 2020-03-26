from pydfs_lineup_optimizer import Site, Sport, get_optimizer, CSVLineupExporter
from pydfs_lineup_optimizer.stacks import TeamStack, PositionsStack
LINES = 60

optimizer = get_optimizer(Site.DRAFTKINGS_CAPTAIN_MODE, Sport.LEAGUE_OF_LEGENDS)

optimizer.load_players_from_csv("DKSalaries.csv")
optimizer.set_deviation(0.01, 0.08)

optimizer.add_stack(TeamStack(3))
optimizer.add_stack(TeamStack(4, for_positions=['TOP', 'JNG', 'MID', 'ADC', 'SUP', 'TEAM']))
optimizer.restrict_positions_for_opposing_team(['TOP'], ['JNG', 'MID', 'ADC', 'SUP', 'TEAM'])
optimizer.restrict_positions_for_same_team(('CPT', 'TEAM'))
optimizer.set_max_repeating_players(5)
for player in optimizer.players:
    if player.fppg < 1:
        optimizer.remove_player(player)
    elif 'CPT' in player.positions:
        player.min_deviation = 0.25
        player.max_deviation = 0.55
exporter = CSVLineupExporter(optimizer.optimize(LINES, randomness=True, generate_exposures=True))
exporter.export('result.csv')
optimizer.player_exposures.write_exposures_csv(total_lineups=LINES)