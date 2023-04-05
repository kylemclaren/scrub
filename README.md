<h1 align="center">🫧 scrub 🫧</h1>

**scrub** is a lightweight, extensible Python package designed to remove Personally Identifiable Information (PII) from any text input. It leverages advanced Machine Learning algorithms to detect PII and provides multiple levels of scrubbing to ensure optimal anonymization of sensitive information. safeguarding user privacy.

## Installation

Install the latest version of scrub from [PyPI](https://pypi.org/project/scrubadubdub/):

```bash
pip install scrubadubdub
```

## Key Features

- Advanced PII detection using Machine Learning algorithms.
- Support for a wide range of PII types (names, email addresses, phone numbers, etc.).
- Customizable detection threshold and levels of sanitization.
- Extensible architecture to allow for the addition of new PII types and algorithms.

## Basic Usage

```python
from scrubadubdub import Scrub

scrubber = Scrub()
input_text = "My name is John Doe and my email address is john.doe@email.com, and my phone number is 123-456-7890"
scrubbed_text = scrubber.scrub(input_text)
print(scrubbed_text)
```

```txt
My name is [REDACTED-NAME] and my email address is [REDACTED-EMAIL], and my phone number is [REDACTED-PHONE]
```

<!-- ## Advanced Usage

With scrub, you can customize the detection threshold, sanitization levels, and even integrate additional scrubbing functionalities based on your needs.

```python
# Set custom threshold and level
scrubber.set_threshold(0.9)
scrubber.set_sanitization_level(scrub.SanitizationLevels.MEDIUM)

# Enable additional sanitization features
scrubber.enable_email_sanitization()

# Add custom PII detection function
def custom_detection(text):
    ...

scrubber.add_detection_function(custom_detection)
``` -->

<!-- ## Documentation

More details on setting up and using scrub can be found in the [Documentation](https://scrub.readthedocs.io).

## Contributing

We love contributions! If you'd like to contribute to scrub, please read our [Contributing Guidelines](./CONTRIBUTING.md) for more information on how to get started. -->

## License

scrub is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.