class Solution:
    def add_subdomains(domain: str, subdomain_visit_count:dict, count: int):
        subdomain_visit_count[domain] += count
        for i in range(len(domain)):
            if domain[i] == ".":
                subdomain_visit_count[domain[i + 1:]] += count

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_visit_count = defaultdict(lambda: 0)
        for entry in cpdomains:
            count, domain = entry.split()
            Solution.add_subdomains(domain, subdomain_visit_count, int(count))
        output = []
        for subdomain, count in subdomain_visit_count.items():
            output.append(f"{count} {subdomain}")
        return output
