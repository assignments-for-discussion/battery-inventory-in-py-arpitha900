def count_batteries_by_health(present_capacities):
    healthy_count = 0
    exchange_count = 0
    failed_count = 0
    
    # Rated capacity of a new battery
    rated_capacity = 120  # Ah
    
    # Calculate thresholds based on rated capacity
    threshold_health = 0.8 * rated_capacity
    threshold_failure = 0.63 * rated_capacity
    
    for present_capacity in present_capacities:
        # Calculate SoH for each battery
        soh = (present_capacity / rated_capacity) * 100
        
        # Categorize batteries based on SoH
        if soh >= 80:
            healthy_count += 1
        elif soh >= 63:
            exchange_count += 1
        else:
            failed_count += 1
    
    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 72]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :")

if __name__ == '__main__':
    test_bucketing_by_health()
