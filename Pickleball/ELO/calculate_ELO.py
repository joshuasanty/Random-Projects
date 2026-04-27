
def expected_score(elo_a: float, elo_b: float) -> float:
    return 1 / (1+ 10**((elo_b - elo_a)/400))

def calculate_ELO(elo_a1: float, elo_a2: float, elo_b1: float, elo_b2: float, k: float, score_a: float, score_b: float) -> tuple[float, float, float, float, float, float]:

    # Calculate current Team ELOs
    elo_team_a = (elo_a1 + elo_a2) / 2
    elo_team_b = (elo_b1 + elo_b2) / 2

    # Calculate expected scores
    expected_a = expected_score(elo_team_a, elo_team_b)
    expected_b = 1 - expected_a

    # Actual score encoding
    actual_a = 1 if score_a > score_b else 0
    actual_b = 1 - actual_a

    #Calculate new Team ELOs
    elo_team_a_new = elo_team_a + k * (actual_a - expected_a)
    elo_team_b_new = elo_team_b + k * (actual_b - expected_b)

    #Calculate new Player ELOs
    elo_a1_new = elo_a1 + k * (actual_a - expected_a) / 2
    elo_a2_new = elo_a2 + k * (actual_a - expected_a) / 2
    elo_b1_new = elo_b1 + k * (actual_b - expected_b) / 2
    elo_b2_new = elo_b2 + k * (actual_b - expected_b) / 2

    return elo_team_a_new, elo_team_b_new, elo_a1_new, elo_a2_new, elo_b1_new, elo_b2_new

#Initialize ELOs and parameters

currentELO_A1 = 1000.0
currentELO_A2 = 1000.0
currentELO_B1 = 1000.0
currentELO_B2 = 1000.0
k = 40.0

# Simulate a game
score_a = 7
score_b = 11

# Calculate new ELOs
new_ELOs = calculate_ELO(currentELO_A1, currentELO_A2, currentELO_B1, currentELO_B2, k, score_a, score_b)

# Print results
print(f"Current ELOs: A1={currentELO_A1}, A2={currentELO_A2}, B1={currentELO_B1}, B2={currentELO_B2}")
print(f"New ELOs: A1={new_ELOs[2]}, A2={new_ELOs[3]}, B1={new_ELOs[4]}, B2={new_ELOs[5]}")

