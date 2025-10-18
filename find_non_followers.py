import json
import pandas as pd

def load_usernames(filepath, key, nested_key=None):
    """
    Loads usernames from Instagram JSON files (followers/following).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        usernames = set()

        if isinstance(data, dict) and key in data:
            # Structure: {"relationships_following": [{...}, {...}]}
            items = data[key]
            for item in items:
                if 'title' in item:
                    if not item['title'].startswith('__deleted__'):
                        usernames.add(item['title'])
                elif 'string_list_data' in item and item['string_list_data']:
                    username_data = item['string_list_data'][0]
                    if nested_key in username_data:
                        usernames.add(username_data[nested_key])

        elif isinstance(data, list):
            # Structure: [{"string_list_data": [{...}]}, {...}] for followers_1.json
            for item in data:
                if 'string_list_data' in item and item['string_list_data']:
                    username_data = item['string_list_data'][0]
                    if 'value' in username_data:
                        usernames.add(username_data['value'])

        return usernames

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return set()
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
        return set()
    except Exception as e:
        print(f"An unexpected error occurred while processing {filepath}: {e}")
        return set()

def main():
    """
    Find users you follow who don't follow you back and export to Excel.
    """
    # 🔹 Set your file paths (either relative or full path)
    following_filepath = 'following.json'
    followers_filepath = 'followers_1.json'

    print("--- Instagram Non-Follower Analyzer ---")

    following_list = load_usernames(following_filepath, 'relationships_following')
    followers_list = load_usernames(followers_filepath, 'relationships_followers', nested_key='value')

    if not following_list and not followers_list:
        print("\n❌ Could not load data from both files. Check file names and location.")
        return

    # 🔹 Find non-followers
    non_followers = sorted(list(following_list - followers_list))

    print(f"\nTotal following: {len(following_list)}")
    print(f"Total followers: {len(followers_list)}")
    print(f"People you follow but don’t follow you back: {len(non_followers)}")

    if non_followers:
        # 🔹 Create DataFrame with 2 columns
        df = pd.DataFrame({
            "S.No": range(1, len(non_followers) + 1),
            "Username": non_followers
        })

        output_file = "non_followers_list.xlsx"
        df.to_excel(output_file, index=False)

        print(f"\n✅ Exported successfully to '{output_file}'")
    else:
        print("\n🎉 Everyone you follow follows you back!")

if __name__ == "__main__":
    main()
