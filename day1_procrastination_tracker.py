def track_procrastination():  
    """Logs how many times you delayed coding today."""  
    delays = int(input("How many times did you procrastinate today? "))  
    with open("punishments.txt", "a") as f:  
        f.write(f"Day 1: {delays} delays. {'🚨' * delays}\n")  
    print(f"Consequence: {delays * 10} push-ups NOW.")  

if __name__ == "__main__":  
    track_procrastination()  
