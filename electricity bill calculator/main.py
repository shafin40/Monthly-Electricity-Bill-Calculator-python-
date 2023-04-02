def calculate_monthly_bill():
    # Ask for number of devices
    num_devices = int(input("Enter the number of devices: "))
    
    total_energy = 0
    
    # Ask for wattage and usage time for each device
    for i in range(num_devices):
        device_wattage = float(input(f"Enter the wattage of device {i+1}: "))
        usage_time = float(input(f"Enter the number of hours device {i+1} is used per day: "))
        daily_energy = device_wattage * usage_time / 1000.0  # convert watt-hours to kilowatt-hours
        total_energy += daily_energy
    
    # Calculate monthly bill based on energy consumption and electricity rate
    electricity_rate = 6.20  # TK per unit
    total_cost = total_energy * electricity_rate * 30
    
    # Print the result
    print(f"Total energy consumption: {total_energy:.2f} kWh")
    print(f"Total monthly bill: {total_cost:.2f} TK")

calculate_monthly_bill()
