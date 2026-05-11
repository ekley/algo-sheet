# Machine coordinates and trip counts
machines = [
    ((8, 5), 9),
    ((4, 2), 6),
    ((11, 8), 4),
    ((13, 2), 12)
]


def weighted_median(values, weights):
    half = sum(weights) / 2
    cumulative = 0

    for value, weight in sorted(zip(values, weights)):
        cumulative += weight
        if cumulative >= half:
            return value


# Extract coordinates and weights
x_coords, y_coords = zip(*(coords for coords, _ in machines))
weights = [trips for _, trips in machines]

# Optimal facility location
location = (
    weighted_median(x_coords, weights),
    weighted_median(y_coords, weights)
)

print(f"The location of the new facility: {location}")