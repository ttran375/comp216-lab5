import dns.resolver


def get_canonical_name(domain):
    try:
        cname_answers = dns.resolver.resolve(domain, "CNAME")
        canonical_name = cname_answers[0].to_text()
        return canonical_name
    except dns.resolver.NoAnswer:
        return None


def main():
    domain = "www.github.com"
    canonical_name = get_canonical_name(domain)
    if canonical_name:
        print(f"The canonical domain name for {domain} is {canonical_name}")
    else:
        print(f"No CNAME record found for {domain}")


if __name__ == "__main__":
    main()
