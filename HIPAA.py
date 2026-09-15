names_input = input("Enter patient names to redact (separated by commas or spaces): ")

real_names = set()
for name in names_input.replace(",", " ").split():
    clean_name = name.strip(".,!?:;()[]\"'").lower()
    if clean_name != "":
        real_names.add(clean_name)

audit_pref = input("Show audit summary after scrubbing? (y/n): ").strip().lower()
show_audit = audit_pref == "y" or audit_pref == "yes"

fake_name = "####"
PUNCTUATION = ".,!?:;()[]\"'"

print("\n--- (Type 'quit' to exit) ---\n")

while True:
    clinical_note = input("Enter clinical note: ")

    if clinical_note.strip().lower() == "quit":
        print("\nExiting scrubber. Stay HIPAA compliant!")
        break

    names_replaced = 0
    ssns_redacted = 0
    phones_redacted = 0
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

        #Check for patient name
        if normalized_word in real_names:
            replacement = fake_name
            names_replaced += 1

        #Check for SSN with dashes
        elif (
            len(clean_word) == 11
            and clean_word[3] == "-"
            and clean_word[6] == "-"
            and clean_word.replace("-", "").isdigit()
        ):
            replacement = "[REDACTED_SSN]"
            ssns_redacted += 1

        #Check for 9 digit SSN
        elif len(clean_word) == 9 and clean_word.isdigit():
            replacement = "[REDACTED_SSN]"
            ssns_redacted += 1

        #Check for phone number
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

    if show_audit:
        print("\n--- Audit Summary ---")
        print("Names redacted: " + str(names_replaced))
        print("SSNs redacted: " + str(ssns_redacted))
        print("Phone numbers redacted: " + str(phones_redacted))

    print("=" * 40 + "\n")