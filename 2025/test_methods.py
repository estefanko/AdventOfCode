# Compare two interpretations

rotations_order = ["L1", "L8", "R35", "L50", "R12"]  # Just first few for testing

def count_method_1():
    """Current method - crosses but doesn't land"""
    dial_value = 50
    dial_size = 100
    counter = 0
    
    for rotation in rotations_order:
        rotation_type = rotation[0]
        rotation_value = int(rotation[1:])
        
        guaranteed_turns = rotation_value // dial_size
        counter += guaranteed_turns
        rotation_value = rotation_value % dial_size
        
        if rotation_type == "L":
            if dial_value < rotation_value:
                counter += 1
            dial_value = (dial_value - rotation_value) % dial_size
        elif rotation_type == "R":
            if dial_value + rotation_value >= dial_size:
                counter += 1
            dial_value = (dial_value + rotation_value) % dial_size
    
    return counter

def count_method_2():
    """Alternative - crosses OR lands on zero"""
    dial_value = 50
    dial_size = 100
    counter = 0
    
    for rotation in rotations_order:
        rotation_type = rotation[0]
        rotation_value = int(rotation[1:])
        
        guaranteed_turns = rotation_value // dial_size
        counter += guaranteed_turns
        rotation_value = rotation_value % dial_size
        
        if rotation_type == "L":
            new_pos = (dial_value - rotation_value) % dial_size
            if dial_value < rotation_value or new_pos == 0:
                counter += 1
            dial_value = new_pos
        elif rotation_type == "R":
            new_pos = (dial_value + rotation_value) % dial_size
            if dial_value + rotation_value >= dial_size or new_pos == 0:
                counter += 1
            dial_value = new_pos
    
    return counter

print(f"Method 1 (current - crosses only): {count_method_1()}")
print(f"Method 2 (crosses OR lands): {count_method_2()}")
