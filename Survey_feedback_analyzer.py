# PYTHON PROJECT: SURVEY FEEDBACK ANALYZER

# STEP 1: PRELOADED FEEDBACK DATA
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],
    'Feedback': [
        'Very GOOD Service!!!',
        'poor support,    not happy   ',
        'GREAT experience! will come again.',
        'okay   okay....',
        'not    BAD',
        'Excellent care, excellent staff!!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# STEP 2: ADD MORE FEEDBACKS
print("===== SURVEY FEEDBACK ANALYZER =====")

number = int(input("How many more feedbacks do you want to add? "))

for i in range(number):
    print(f"\nEnter details for feedback {i + 1}")

    name = input("Enter name: ")
    feedback = input("Enter written feedback: ")

    while True:
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# STEP 3: TEXT CLEANING
punctuation = [',', '.', '!', '?']

for i in range(len(feedback_data['Feedback'])):
    text = feedback_data['Feedback'][i]

    for mark in punctuation:
        text = text.replace(mark, '')

    text = ' '.join(text.split())
    text = text.lower()

    feedback_data['Feedback'][i] = text


# STEP 4: WORD COUNT INSIGHTS
def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


print("\n===== WORD COUNT INSIGHTS =====")
print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))


# STEP 5: FINAL SUMMARY AND INSIGHTS
print("\n===== FINAL CLEANED FEEDBACK DATA =====")
print(feedback_data)

average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage rating:", round(average_rating, 2))


# FIND THE LONGEST FEEDBACK
longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda feedback: len(feedback.split())
)

print("\nLongest feedback:")
print(longest_feedback)
print("Word count:", len(longest_feedback.split()))


# LIST OF UNIQUE WORDS
unique_words = set()

for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        unique_words.add(word)

print("\nUnique words used across all feedbacks:")
print(sorted(unique_words))


# OPTIONAL: SORT FEEDBACKS BY RATING
sorted_feedbacks = sorted(
    zip(
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda item: item[2],
    reverse=True
)

print("\n===== FEEDBACKS SORTED BY RATING =====")

for name, feedback, rating in sorted_feedbacks:
    print(f"Name: {name} | Rating: {rating} | Feedback: {feedback}")