clinical_note = "Patient Symere Woods called 555-0199 today. Symere reported fever and gave SSN 123-45-6789."
#clinical_note2 = "Patient Victoria Walker called 888-1400 today. Victoria reported abdomen pain and gave SSN 987-65-4321."

real_names = ["Symere", "Woods", "Victoria", "Walker"]
fake_names = ["Alex", "Taylor", "Jordan", "Doe"]

words = clinical_note.split()
scrubbed_words = []

for word in words:
    clean_word = word.strip(".,!?")
    if clean_word in real_names:
        scrubbed_words.append("Alex")
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