# Damn Vulnerable Application Scanner (DVAS)

This repository contains a collection of web-based (vulnerable) security scanners,
including (but not limited to) the vulnerabilities from "Never Trust Your Victim: Weaponizing Vulnerabilities in Security Scanners" [3].
DVAS also contains a simulation of [CVE-2020-7354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-7354) and]
[CVE-2020-7355](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-7355) for Metasploit Pro [2].

## Getting Started

DVAS comes with 2 main components:
1. **Scanner** acts as a normal security scanner, gathering information from the selected target.
2. **Attacker** acts as a malicious target that answers with an attack payload. NOTE: you do not need to use this component, you can build your own if  you want.

This repository includes multiple deploy options.

### Docker Compose

1. `git clone https://github.com/AvalZ/DVAS.git` OR `git clone git@github.com:AvalZ/DVAS.git`
2. `cd DVAS`
3. `docker-compose up`

Scanner is now available at http://localhost:8080, while Attacker is available at http://localhost:8081.

### Docker

(*TODO*)

### Manual

Prerequisites:
- Nmap
- PHP 7.2+

(*TODO*)

## References

1. [A. Valenza, G. Costa, A. Armando. "Never Trust Your Victim: Weaponizing Vulnerabilities in Security Scanners"](https://www.researchgate.net/publication/344642774_Never_Trust_Your_Victim_Weaponizing_Vulnerabilities_in_Security_Scanners)
2. [Attacking the Attackers](https://avalz.it/research/metasploit-pro-xss-to-rce/)
