import (
    "strings"
    "strconv"
)

func AddSubdomains(subdomain_visit_count map[string]int, count int, domain string) {
    subdomain_visit_count[domain] += count
    for i := 0; i < len(domain); i++ {
        if domain[i] == '.' {
            subdomain := domain[i + 1:]
            subdomain_visit_count[subdomain] += count
        }
    }
}

func subdomainVisits(cpdomains []string) []string {
    subdomain_visit_count := make(map[string]int)
    for i := 0; i < len(cpdomains); i++ {
        entry := strings.Split(cpdomains[i], " ")
        count, _ := strconv.Atoi(entry[0])
        AddSubdomains(subdomain_visit_count, count, entry[1])
    }
    output := make([]string, 0)
    for subdomain, count := range subdomain_visit_count {
        entry := strconv.Itoa(count) + " " + subdomain
        output = append(output, entry)
    }
    return output
}
