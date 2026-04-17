def ways(stairs):
    # Edge case
    if stairs < 0:
        return 0
    
    # Reached top
    if stairs == 0:
        return 1

    twoSteps = 0
    oneStep = 0

    # Take 2 steps
    if stairs >= 2:
        twoSteps = ways(stairs - 2)

    # Take 1 step
    oneStep = ways(stairs - 1)

    # Total ways
    return twoSteps + oneStep


stairs = int(input("Enter number of steps: "))
print("Number of ways to climb:", ways(stairs))