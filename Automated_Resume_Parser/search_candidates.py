from db import search_candidates


keyword = input("Enter a skill, name, email, or education to search: ")

results = search_candidates(keyword)


if results:

    print("\n========== SEARCH RESULTS ==========")

    for candidate in results:

        print("\nID:", candidate["id"])
        print("Name:", candidate["name"])
        print("Email:", candidate["email"])
        print("Phone:", candidate["phone"])
        print("Skills:", candidate["skills"])
        print("Education:", candidate["education"])

    print("\n====================================")

else:

    print("\nNo matching candidates found.")