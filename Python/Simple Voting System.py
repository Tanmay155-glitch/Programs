def vote(candidate_votes):
    print("\nCandidates:")
    for i, candidate in enumerate(candidate_votes, start=1):
        print(f"{i}. {candidate}")

    choice = int(input("Vote for candidate number (1/2/3...): "))
    if 1 <= choice <= len(candidate_votes):
        candidate_votes[choice - 1] += 1
    else:
        print("Invalid choice.")

def main():
    candidate_votes = [0, 0, 0]  # Assume 3 candidates
    candidates = ["Alice", "Bob", "Charlie"]
    
    while True:
        print("\nVoting System")
        print("1. Vote")
        print("2. View results")
        print("3. Exit")
        
        option = input("Choose an option (1/2/3): ")
        
        if option == '1':
            vote(candidate_votes)
        elif option == '2':
            for candidate, votes in zip(candidates, candidate_votes):
                print(f"{candidate}: {votes} votes")
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
