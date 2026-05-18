t = int(input())

for i in range(t):
    n = int(input())
    
    alice = 0
    bob = 0
    
    step = 1
    remaining = n
    
    while remaining > 0:
        take = min(step, remaining)
        
        if step == 1:
            alice += take
        else:
            # after step 1, players switch every 2 steps
            if ((step - 2) // 2) % 2 == 0:
                bob += take
            else:
                alice += take
        
        remaining -= take
        step += 1
    
    print(alice, bob)
