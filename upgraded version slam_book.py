# -*- coding: utf-8 -*-
"""
🎉 ABD'S DIGITAL SLAM BOOK 🎉
Owner: Muhammad Abdullah Ahmad (Abd)
Age: 11 | Zodiac: Libra ♎ | Started: 30th July 2025
"""

def main():
    print("\n" + "="*50)
    print("       🎉 ABD'S DIGITAL SLAM BOOK 🎉")
    print("="*50 + "\n")
    
    # Owner's details
    owner = {
        "Full Name": "Muhammad Abdullah Ahmad",
        "Nickname": "Abd",
        "Birthday": "20 October, 2013",
        "Zodiac Sign": "Libra ♎",
        "Favorite Color": "Black 🖤",
        "Favorite Food": "Biryani 🍛",
        "Hobbies": "Cricket 🏏 + Coding 💻",
        "Dream Job": "Professional Cricketer",
        "Movie": "Fighter ✈️",
        "Song": "8 Bande 🎵",
        "Book": "World War 2 📖",
        "Secret Obsession": "Tech or Cricket? 🤖🏏",
        "Zombie Plan": "Hack a defense system with Python! 💻🧟♂️"
    }
    
    # Friends' entries (sample)
    friends = {
        "Hashir": {
            "How we met": "He was fighting (but not hitting), and I helped him fight! 👊",
            "Funniest Memory": "You changed shoes mid-lesson! 👟➡️👟",
            "Song for Me": "Daku 🎵",
            "One Word": "A (A for Awesome?) 😂"
        }
    }
    
    # Cricket stats tracker (empty at start)
    cricket_stats = {}
    
    while True:
        print("\n" + "-"*50)
        print("MENU:")
        print("1. 👤 View My Profile")
        print("2. 👥 View Friends' Entries")
        print("3. 🏏 Cricket Stats Tracker")
        print("4. ✍️ Add a New Friend")
        print("5. ❌ Exit")
        choice = input("\nChoose (1-5): ")
        
        # 1. Display owner profile
        if choice == "1":
            print("\n" + "="*20 + " 👤 MY PROFILE " + "="*20)
            for key, value in owner.items():
                print(f"{key.upper()}: {value}")
            print("="*50)
        
        # 2. View friends' entries
        elif choice == "2":
            print("\n" + "="*20 + " 👥 FRIENDS' SLAMS " + "="*20)
            if not friends:
                print("No friends added yet! Use option 4 to add one.")
            else:
                for friend, details in friends.items():
                    print(f"\n❤️ FRIEND: {friend.upper()}")
                    for key, value in details.items():
                        print(f"- {key}: {value}")
            print("="*50)
        
        # 3. Cricket Stats Tracker
        elif choice == "3":
            print("\n" + "="*20 + " 🏏 CRICKET STATS TRACKER " + "="*20)
            while True:
                print("\n1. Add Player Stats")
                print("2. View All Stats")
                print("3. Back to Main Menu")
                sub_choice = input("\nChoose (1-3): ")
                
                if sub_choice == "1":
                    name = input("Player Name: ")
                    runs = int(input("Runs Scored: "))
                    wickets = int(input("Wickets Taken: "))
                    cricket_stats[name] = {"Runs": runs, "Wickets": wickets}
                    print(f"{name} added! ✅")
                
                elif sub_choice == "2":
                    if not cricket_stats:
                        print("No stats yet! Add players first.")
                    else:
                        print("\n--- PLAYER STATS ---")
                        for player, stats in cricket_stats.items():
                            print(f"{player}: Runs - {stats['Runs']}, Wickets - {stats['Wickets']}")
                
                elif sub_choice == "3":
                    break
                
                else:
                    print("Invalid choice!")
        
        # 4. Add a new friend
        elif choice == "4":
            print("\n" + "="*20 + " ✍️ ADD A FRIEND " + "="*20)
            name = input("Friend's Name: ")
            friends[name] = {
                "How we met": input("How did you meet? "),
                "Funniest Memory": input("Funniest memory with you: "),
                "Song for Me": input("Song that reminds them of you: "),
                "One Word": input("One word to describe you: ")
            }
            print(f"\n{name}'s entry added! ✅")
        
        # 5. Exit
        elif choice == "5":
            print("\nExiting... Keep shining, Abd! ✨")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()