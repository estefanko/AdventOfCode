# Test to understand zero crossing logic

def test_cases():
    dial_size = 100
    
    test_scenarios = [
        ("Start at 0, L10", 0, "L", 10),
        ("Start at 5, L10", 5, "L", 10),
        ("Start at 10, L10", 10, "L", 10),
        ("Start at 0, R10", 0, "R", 10),
        ("Start at 90, R10", 90, "R", 10),
        ("Start at 95, R10", 95, "R", 10),
    ]
    
    for desc, start_pos, direction, amount in test_scenarios:
        if direction == "L":
            crosses = start_pos < amount
            new_pos = (start_pos - amount) % dial_size
        else:  # R
            crosses = start_pos + amount >= dial_size
            new_pos = (start_pos + amount) % dial_size
        
        lands_on_zero = (new_pos == 0)
        
        print(f"{desc}:")
        print(f"  Crosses zero: {crosses}, Lands on zero: {lands_on_zero}, New pos: {new_pos}")
        print()

test_cases()
