from random import choice, randint
import string
import pandas as pd

# Make sure the 'updateddata.csv' path is correct. It should be in the same directory where the script is running or provide the full path.
data = pd.read_csv('updateddata.csv')

# Function to generate synthetic email content
def generate_email_content(category):
    if category == "Customer Support":
        issues = ["trouble logging in", "password reset issue", "account recovery help needed", "difficulty updating profile information", "problem with account verification"]
        issue = choice(issues)
        return f"I am experiencing {issue}. Can you assist me?"

    elif category == "Transaction Alert":
        actions = ["transfer", "payment", "withdrawal", "deposit"]
        amounts = [str(randint(10, 1000)) for _ in range(5)]
        recipients = [''.join(choice(string.ascii_letters) for _ in range(5)) for _ in range(5)]  # Generate random names
        action = choice(actions)
        amount = choice(amounts)
        recipient = choice(recipients)
        return f"Your recent {action} of ${amount} to {recipient} was successful."

    elif category == "Promotional Email":
        offers = ["limited-time offer", "exclusive deal", "special discount", "one-time promotion", "holiday sale"]
        actions = ["Sign up now", "Subscribe today", "Join us", "Get started", "Take advantage now"]
        offer = choice(offers)
        action = choice(actions)
        return f"Don't miss out on our {offer}! {action}."

    elif category == "Fraudulent Alert":
        activities = ["suspicious activity", "unusual login attempts", "potentially fraudulent transactions", "irregular account movements", "unexpected changes to your account"]
        activity = choice(activities)
        return f"Warning: We detected {activity} on your account. Please review your recent activities."

    elif category == "Account Update":
        updates = ["updated our privacy policy", "changed our terms of service", "modified our user agreement", "updated our account policies", "revised our subscription terms"]
        action = choice(updates)
        return f"We have {action}. Please review the changes."

# Categories present in the dataset
categories = ["Customer Support", "Transaction Alert", "Promotional Email", "Fraudulent Alert", "Account Update"]

# Generate synthetic data
new_rows = []
for _ in range(470):  # Generate 470 new rows
    category = choice(categories)
    email_content = generate_email_content(category)
    new_rows.append([email_content, category])

# Convert the new rows into a DataFrame
new_data = pd.DataFrame(new_rows, columns=['Email_Content', 'Category'])

# Combine the new data with the original dataset
combined_data = pd.concat([data, new_data], ignore_index=True)

# Display information about the updated dataset
combined_data.info()

# Additional categories observed from the uploaded image
additional_categories = ["Spam", "Newsletter Subscription"]

# Update the categories to include the new ones
all_categories = categories + additional_categories

# Function to generate synthetic email content, updated to handle new categories
def generate_email_content_v2(category):
    # Existing categories
    if category == "Customer Support":
        issues = ["trouble logging in", "password reset issue", "account recovery help needed", "difficulty updating profile information", "problem with account verification"]
        issue = choice(issues)
        return f"I am experiencing {issue}. Can you assist me?"

    elif category == "Transaction Alert":
        actions = ["transfer", "payment", "withdrawal", "deposit"]
        amounts = [str(randint(10, 1000)) for _ in range(5)]
        recipients = [''.join(choice(string.ascii_letters) for _ in range(5)) for _ in range(5)]  # Generate random names
        action = choice(actions)
        amount = choice(amounts)
        recipient = choice(recipients)
        return f"Your recent {action} of ${amount} to {recipient} was successful."

    elif category == "Promotional Email":
        offers = ["limited-time offer", "exclusive deal", "special discount", "one-time promotion", "holiday sale"]
        actions = ["Sign up now", "Subscribe today", "Join us", "Get started", "Take advantage now"]
        offer = choice(offers)
        action = choice(actions)
        return f"Don't miss out on our {offer}! {action}."

    elif category == "Fraudulent Alert":
        activities = ["suspicious activity", "unusual login attempts", "potentially fraudulent transactions", "irregular account movements", "unexpected changes to your account"]
        activity = choice(activities)
        return f"Warning: We detected {activity} on your account. Please review your recent activities."

    elif category == "Account Update":
        updates = ["updated our privacy policy", "changed our terms of service", "modified our user agreement", "updated our account policies", "revised our subscription terms"]
        action = choice(updates)
        return f"We have {action}. Please review the changes."

    # New categories from the uploaded image
    elif category == "Spam":
        products = ["winning a lottery", "inheritance claims", "quick money schemes", "miracle cures", "unbelievable discounts"]
        product = choice(products)
        return f"Congratulations! You have been selected for {product}. This is a once in a lifetime opportunity!"

    elif category == "Newsletter Subscription":
        topics = ["health tips", "investment strategies", "travel guides", "technology updates", "fashion trends"]
        topic = choice(topics)
        frequency = choice(["daily", "weekly", "monthly"])
        return f"Stay up to date with our {frequency} newsletter on {topic}. Don't miss any updates!"

data = pd.read_csv('updateddata.csv')

# Categories present in the dataset
categories = ["Customer Support", "Transaction Alert", "Promotional Email", "Fraudulent Alert", "Account Update"]
additional_categories = ["Spam", "Newsletter Subscription"]

# Update the categories to include the new ones
all_categories = categories + additional_categories

# Generate synthetic data for the original categories
new_rows = []
for _ in range(470):  # Generate 470 new rows
    category = choice(categories)
    email_content = generate_email_content(category)
    new_rows.append([email_content, category])

# Convert the new rows into a DataFrame
new_data = pd.DataFrame(new_rows, columns=['Email_Content', 'Category'])

# Combine the new data with the original dataset
combined_data = pd.concat([data, new_data], ignore_index=True)

# Generate synthetic data for all categories
additional_data = []
for _ in range(470):  # Generate additional 470 new rows
    category = choice(all_categories)
    email_content = generate_email_content_v2(category)
    additional_data.append([email_content, category])

# Convert the additional new rows into a DataFrame
additional_data_df = pd.DataFrame(additional_data, columns=['Email_Content', 'Category'])

# Combine the additional new data with the previously combined dataset
full_combined_data = pd.concat([combined_data, additional_data_df], ignore_index=True)

# Save the full combined dataset to a CSV file
full_combined_data.to_csv("C:/Users/Charvi Jain/Desktop/new_data.csv", index=False)

# Display information about the updated dataset
full_combined_data.info()
