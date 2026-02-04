import json
import re
import os


def sanitize_all_hars():
    # Setup paths
    folder_path = os.getcwd()
    output_folder = os.path.join(folder_path, "Sanitized_Uploads")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Patterns and Sensitive Headers
    EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    SENSITIVE_HEADERS = ['authorization', 'cookie', 'set-cookie', 'x-client-data']

    # Process every .har file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".har"):
            print(f"🧹 Processing: {filename}...")

            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for entry in data['log']['entries']:
                # Redact Headers
                entry['request']['headers'] = [h for h in entry['request']['headers'] if
                                               h['name'].lower() not in SENSITIVE_HEADERS]
                entry['response']['headers'] = [h for h in entry['response']['headers'] if
                                                h['name'].lower() not in SENSITIVE_HEADERS]

                # Redact Emails in URL
                entry['request']['url'] = re.sub(EMAIL_REGEX, "[REDACTED]", entry['request']['url'])

            # Save to the new folder
            output_path = os.path.join(output_folder, f"CLEAN_{filename}")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

    print(f"\n✅ Success! All clean files are in the 'Sanitized_Uploads' folder.")


if __name__ == "__main__":
    sanitize_all_hars()