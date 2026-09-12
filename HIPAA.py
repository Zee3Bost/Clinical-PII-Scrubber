clinical_note = input("Enter the clinical note to scrub: ")

real_names = {"symere", "woods", "victoria", "walker"}
fake_name = "####"

names_replaced = 0
ssns_redacted = 0
phones_redacted = 0

PUNCTUATION = ".,!?:;()[]\"'"

words = clinical_note.split()
scrubbed_words = []

for word in words:
    prefix = ""
    if word.lower().startswith("ssn:"):
        prefix = word[:4] + " "
        word = word[4:]
    elif word.lower().startswith("ssn#"):
        prefix = word[:4] + " "
        word = word[4:]

    leading_punct = ""
    trailing_punct = ""

    if word and word[0] in PUNCTUATION:
        leading_punct = word[0]
    if word and word[-1] in PUNCTUATION:
        trailing_punct = word[-1]

    clean_word = word.strip(PUNCTUATION).replace("–", "-").replace("—", "-")
    normalized_word = clean_word.lower()


    if normalized_word in real_names:
        replacement = fake_name
        names_replaced += 1

    elif (
        len(clean_word) == 11
        and clean_word[3] == "-"
        and clean_word[6] == "-"
        and clean_word.replace("-", "").isdigit()
    ):
        replacement = "[REDACTED_SSN]"
        ssns_redacted += 1

    elif len(clean_word) == 9 and clean_word.isdigit():
        replacement = "[REDACTED_SSN]"
        ssns_redacted += 1

    elif (
        len(clean_word) == 8
        and clean_word[3] == "-"
        and clean_word.replace("-", "").isdigit()
    ):
        replacement = "[REDACTED_PHONE]"
        phones_redacted += 1

    
    else:
        replacement = clean_word

    scrubbed_words.append(prefix + leading_punct + replacement + trailing_punct)

final = " ".join(scrubbed_words)

print("\nOriginal:")
print(clinical_note)
print("\nScrubbed:")
print(final)

print("\n--- Audit Summary ---")
print("Names redacted: " + str(names_replaced))
print("SSNs redacted: " + str(ssns_redacted))
print("Phone numbers redacted: " + str(phones_redacted))