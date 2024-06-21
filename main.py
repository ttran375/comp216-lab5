import socket
import ssl
import dns.resolver


# Function to get IPv4 and IPv6 addresses
def get_ip_addresses(domain):
    ipv4_addresses = []
    ipv6_addresses = []
    try:
        ipv4_answers = dns.resolver.resolve(domain, "A")
        ipv4_addresses = [answer.to_text() for answer in ipv4_answers]
    except dns.resolver.NoAnswer:
        print(f"No IPv4 address found for {domain}")

    try:
        ipv6_answers = dns.resolver.resolve(domain, "AAAA")
        ipv6_addresses = [answer.to_text() for answer in ipv6_answers]
    except dns.resolver.NoAnswer:
        print(f"No IPv6 address found for {domain}")

    return ipv4_addresses, ipv6_addresses


# Function to get nameservers
def get_nameservers(domain):
    nameservers = []
    try:
        ns_answers = dns.resolver.resolve(domain, "NS")
        nameservers = [answer.to_text() for answer in ns_answers]
    except dns.resolver.NoAnswer:
        print(f"No nameservers found for {domain}")

    return nameservers


# Function to get mail servers
def get_mail_servers(domain):
    mail_servers = []
    try:
        mx_answers = dns.resolver.resolve(domain, "MX")
        mail_servers = [answer.to_text() for answer in mx_answers]
    except dns.resolver.NoAnswer:
        print(f"No mail servers found for {domain}")

    return mail_servers


# Function to get TLS/SSL certificate issuers
def get_ssl_certificate_issuers(domain):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
    conn.settimeout(5.0)
    conn.connect((domain, 443))
    ssl_info = conn.getpeercert()
    conn.close()

    issuer = dict(x[0] for x in ssl_info["issuer"])
    return issuer.get("organizationName")


# Main function
def main():
    domain = "github.com"

    print(f"Getting information for {domain}...")

    ipv4_addresses, ipv6_addresses = get_ip_addresses(domain)
    print("IPv4 Addresses:", ipv4_addresses)
    print("IPv6 Addresses:", ipv6_addresses)

    nameservers = get_nameservers(domain)
    print("Nameservers:", nameservers)

    mail_servers = get_mail_servers(domain)
    print("Mail Servers:", mail_servers)

    ssl_certificate_issuer = get_ssl_certificate_issuers(domain)
    print("TLS/SSL Certificate Issuer:", ssl_certificate_issuer)


if __name__ == "__main__":
    main()
