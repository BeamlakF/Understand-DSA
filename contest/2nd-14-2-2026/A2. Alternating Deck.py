t = int(input())

for i in range(t):
    n = int(input())
    
    alice_white = 0
    alice_black = 0
    bob_white = 0
    bob_black = 0
    
    step = 1
    remaining = n
    position = 1 
    
    while remaining > 0:
        take = min(step, remaining)
        
        # Count whites and blacks in this segment
        if position % 2 == 1:
            whites = (take + 1) // 2
            blacks = take // 2
        else:
            whites = take // 2
            blacks = (take + 1) // 2
        
        # Decide player
        if step == 1:
            alice_white += whites
            alice_black += blacks
        else:
            if ((step - 2) // 2) % 2 == 0:
                bob_white += whites
                bob_black += blacks
            else:
                alice_white += whites
                alice_black += blacks
        
        remaining -= take
        position += take
        step += 1
    
    print(alice_white, alice_black, bob_white, bob_black)
