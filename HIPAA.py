
clinical_note = input("Enter the clinical note to scrub: ")

real_names = ["Symere", "Woods", "Victoria", "Walker"]
fake_names = ["####"]

words = clinical_note.split()
scrubbed_words = []

for word in words:
    clean_word = word.strip(".,!?")
    if clean_word in real_names:

        scrubbed_words.append("####")

    elif len(clean_word) == 11 and clean_word[3] == "-" and clean_word[6] == "-":
        scrubbed_words.append("[REDACTED_SSN]")
    elif len(clean_word) == 8 and clean_word[3] == "-":
        scrubbed_words.append("REDACTED_PHONE")
    else:
        scrubbed_words.append(word)
final = " ".join(scrubbed_words)

print("Original:")
print(clinical_note)
print("\nScrubbed:")
print(final)