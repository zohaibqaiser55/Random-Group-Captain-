import random

# Function to read names from a given file and return them as a list
def read_names_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to assign members and captains to groups
def assign_groups(members, captains, num_groups=8):
    # Shuffle the members and captains lists to ensure randomness
    random.shuffle(members)
    random.shuffle(captains)

    # Initialize empty groups
    groups = [[] for _ in range(num_groups)]
    
    # Select the first 'num_groups' captains and assign one to each group
    selected_captains = captains[:num_groups]
    remaining_captains = captains[num_groups:]
    
    # Assign one captain to each group
    for i in range(num_groups):
        groups[i].append(selected_captains[i])
    
    # Distribute members among the groups in a round-robin fashion
    for i, member in enumerate(members):
        groups[i % num_groups].append(member)
    
    # Distribute any remaining captains to groups with fewer members
    for captain in remaining_captains:
        smallest_group = min(groups, key=len)
        smallest_group.append(captain)
    
    return groups

# Function to print the groups in a formatted table
def print_groups(groups):
    print("=" * 66)
    print(f"{'Group No':<12} | {'Captain':<12} | Members")
    print("=" * 66)
    
    for i, group in enumerate(groups):
        captain = group[0]
        members = ", ".join(group[1:])
        print(f"{i + 1:<12} | {captain:<12} | {members}")
        print("=" * 66)

# Main function to read files, assign groups, and print the results
def main():
    captains_file = 'captains.txt'
    group_members_file = 'group_members.txt'
    
    captains = read_names_from_file(captains_file)
    group_members = read_names_from_file(group_members_file)
    
    groups = assign_groups(group_members, captains)
    
    print_groups(groups)

# Entry point of the script
if __name__ == "__main__":
    main()