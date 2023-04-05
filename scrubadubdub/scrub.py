import re


# Detection Engine
class DetectionEngine:
    def __init__(self):
        self.name_regex = re.compile(r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b")
        self.email_regex = re.compile(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        )
        self.phone_regex = re.compile(r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b")

    def detect_names(self, text):
        return self.name_regex.findall(text)

    def detect_emails(self, text):
        return self.email_regex.findall(text)

    def detect_phone_numbers(self, text):
        return self.phone_regex.findall(text)


# Scrubbing Engine
class ScrubbingEngine:
    def __init__(self):
        self.name_replacement = "[REDACTED-NAME]"
        self.email_replacement = "[REDACTED-EMAIL]"
        self.phone_replacement = "[REDACTED-PHONE]"

    def scrub_names(self, text, names):
        for name in names:
            text = text.replace(name, self.name_replacement)
        return text

    def scrub_emails(self, text, emails):
        for email in emails:
            text = text.replace(email, self.email_replacement)
        return text

    def scrub_phone_numbers(self, text, phone_numbers):
        for phone in phone_numbers:
            text = text.replace(phone, self.phone_replacement)
        return text


# Scrub Class
class Scrub:
    def __init__(self):
        self.detection_engine = DetectionEngine()
        self.scrubbing_engine = ScrubbingEngine()

    def scrub(self, text):
        names = self.detection_engine.detect_names(text)
        emails = self.detection_engine.detect_emails(text)
        phone_numbers = self.detection_engine.detect_phone_numbers(text)

        text = self.scrubbing_engine.scrub_names(text, names)
        text = self.scrubbing_engine.scrub_emails(text, emails)
        text = self.scrubbing_engine.scrub_phone_numbers(text, phone_numbers)

        return text
