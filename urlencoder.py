import argparse
import urllib.parse

def encode_url(url):
    parsed_url = urllib.parse.urlparse(url)
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = urllib.parse.quote(parsed_url.path)
    params = urllib.parse.quote(parsed_url.params)
    query = urllib.parse.quote(parsed_url.query)
    fragment = urllib.parse.quote(parsed_url.fragment)

    encoded_url = urllib.parse.urlunparse((scheme, netloc, path, params, query, fragment))
    return encoded_url

def main():
    parser = argparse.ArgumentParser(description="URL encoder tool")
    parser.add_argument("url", help="URL to be encoded")
    args = parser.parse_args()

    encoded_url = encode_url(args.url)
    print(encoded_url)

if __name__ == "__main__":
    main()