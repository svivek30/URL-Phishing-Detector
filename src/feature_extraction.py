from urllib.parse import urlparse
import re

def extract_features(url):

    features = []

    # 1. Using IP Address
    ip_pattern = re.compile(
        r'(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.){3}([01]?\\d\\d?|2[0-4]\\d|25[0-5])'
    )

    features.append(1 if re.match(ip_pattern, url) else -1)

    # 2. Long URL
    features.append(1 if len(url) > 75 else -1)

    # 3. Short URL
    shortening_services = r"bit.ly|tinyurl|goo.gl|t.co"

    features.append(
        1 if re.search(shortening_services, url) else -1
    )

    # 4. Symbol @
    features.append(1 if "@" in url else -1)

    # 5. Redirecting //
    features.append(
        1 if url.rfind('//') > 7 else -1
    )

    # 6. Prefix Suffix -
    features.append(
        1 if '-' in urlparse(url).netloc else -1
    )

    # 7. Subdomains
    dot_count = urlparse(url).netloc.count('.')

    if dot_count == 1:
        features.append(-1)

    elif dot_count == 2:
        features.append(0)

    else:
        features.append(1)

    # 8. HTTPS
    features.append(
        -1 if url.startswith("https") else 1
    )

    # Remaining dummy features
    while len(features) < 30:
        features.append(-1)

    return features