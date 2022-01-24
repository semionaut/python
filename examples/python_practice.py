counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for key, value in counties_dict.items():
    print(f"{key} county has {value} voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                    {"county":"Denver", "registered_voters": 463353}, 
                    {"county":"Jefferson", "registered_voters": 432438
                    }]

for i in voting_data:
    print(f"In {i['county']} county there are {i['registered_voters']} registered voters.")
