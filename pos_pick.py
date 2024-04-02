import pandas as pd
import random


def read_ods(filename):
    """
    Reads an ODS file and returns a pandas DataFrame.
    """
    return pd.read_excel(filename, engine='odf')


def write_ods(filename, df):
    """
    Writes a pandas DataFrame to an ODS file.
    """
    df.to_excel(filename, engine='odf', index=False)



# def update_file1_with_file2(file1_df, file2_df):
#     """
#     Updates the first file data by adding a new column for 2024 with usernames from the second file,
#     ensuring that only usernames present in the second file are assigned a 2024 entry.
#     Additionally, updates contact information (address, city, state, zip) from the second file if different.
#     """
#     file2_usernames = set(file2_df['username'].tolist())
#     assigned_usernames = set()

#     # Create a dictionary for quick access to file2 data by username
#     file2_data_dict = file2_df.set_index('username').to_dict(orient='index')

#     def assign_username_and_update_contact(row):
#         current_username = row['username']
#         if current_username not in file2_usernames:
#             return '', row['name'], row['address'], row['city'], row['state'], row['zip']

#         existing_usernames = {current_username, row.get('2022', ''), row.get('2023', '')}
#         available_usernames = [u for u in file2_usernames if u not in existing_usernames and u not in assigned_usernames]

#         # Assign a new username for 2024 if possible
#         chosen_username = random.choice(available_usernames) if available_usernames else ''
#         if chosen_username:
#             assigned_usernames.add(chosen_username)

#         Update contact info if the user exists in file2
#         if current_username in file2_data_dict:
#             file2_user_info = file2_data_dict[current_username]
#             return (chosen_username,
#                     file2_user_info['name'],
#                     file2_user_info['address'],
#                     file2_user_info['city'],
#                     file2_user_info['state'],
#                     file2_user_info['zip'])
#         else:
#             return chosen_username, row['name'], row['address'], row['city'], row['state'], row['zip']

#     # Apply the function and update the DataFrame
#     update_cols = file1_df.apply(assign_username_and_update_contact, axis=1, result_type='expand')
#     file1_df['name'] = update_cols[0]
#     file1_df['address'] = update_cols[1]
#     file1_df['address2'] = update_cols[2]
#     file1_df['city'] = update_cols[3]
#     file1_df['state'] = update_cols[4]
#     file1_df['zip'] = update_cols[5]
#     file1_df['2024'] = update_cols[6]

#     return file1_df
def update_file1_with_file2(file1_df, file2_df):
    """
    Updates the first file data by adding a new column for 2024 with usernames from the second file,
    ensuring that only usernames present in the second file are assigned a 2024 entry.
    """
    file2_usernames = set(file2_df['username'].tolist())
    assigned_usernames = set()

    # Create a dictionary for quick access to file2 data by username
    file2_data_dict = file2_df.set_index('username').to_dict(orient='index')

    def assign_username(row):
        current_username = row['username']
        if current_username not in file2_usernames:
            return ''
        
        existing_usernames = {current_username, row.get('2022', ''), row.get('2023', '')}
        available_usernames = [u for u in file2_usernames if u not in existing_usernames and u not in assigned_usernames]
        
        # Assign a new username for 2024 if possible
        chosen_username = random.choice(available_usernames) if available_usernames else ''
        if chosen_username:
            assigned_usernames.add(chosen_username)
        
        return chosen_username

    # Apply the function to assign usernames for 2024
    file1_df['2024'] = file1_df.apply(assign_username, axis=1)

    return file1_df


def add_missing_users_from_file2(file1_df, file2_df):
    """
    Adds users from the second file to the first file if they are not already present,
    avoiding SettingWithCopyWarning.
    """
    file1_usernames = set(file1_df['username'])
    file2_usernames = set(file2_df['username'])

    missing_usernames = file2_usernames - file1_usernames
    missing_users_df = file2_df[file2_df['username'].isin(missing_usernames)].copy()  # Use .copy()

    # Initialize columns that exist in file1_df but not in file2_df
    missing_columns = set(file1_df.columns) - set(file2_df.columns)
    for col in missing_columns:
        missing_users_df.loc[:, col] = ''  # Use .loc[] to avoid SettingWithCopyWarning

    # Append missing users to file1_df
    updated_file1_df = pd.concat([file1_df, missing_users_df], ignore_index=True)

    return updated_file1_df


def main():
    file1_path = 'pos.ods'
    file2_path = 'pos_2024.ods'
    
    # Read the ODS files into DataFrames
    file1_df = read_ods(file1_path)
    file2_df = read_ods(file2_path)

    # Update file1 DataFrame with information from file2
    updated_file1_df = update_file1_with_file2(file1_df, file2_df)

    # Assume updated_file1_df is the result from update_file1_with_file2_and_contact_info
    updated_file1_df = add_missing_users_from_file2(updated_file1_df, file2_df)

    # Write the updated DataFrame back to a new ODS file
    output_path = 'pos_updated.ods'
    write_ods(output_path, updated_file1_df)

    print(f"Updated file written to {output_path}")

if __name__ == '__main__':
    main()

