from scrub import Scrub


def main():
    scrubber = Scrub()
    input_text = "My name is John Doe and my email address is john.doe@email.com, and my phone number is 123-456-7890"
    scrubbed_text = scrubber.scrub(input_text)
    print(scrubbed_text)


if __name__ == "__main__":
    main()
