# Security checklist

Check every file against each rule. Name the rule in the report.

## Application code

- **Hard-coded secrets**: passwords, API keys, tokens or connection strings in code or config.
- **Injection**: SQL built with string formatting, shell commands built from input (`shell=True`, `os.system`).
- **Unsafe deserialisation**: `pickle`, `yaml.load` without a safe loader, or similar on data from outside.
- **Debug exposure**: debug mode on, stack traces or secrets in responses or logs.
- **Weak crypto**: MD5 or SHA-1 for passwords, home-made encryption, disabled certificate checks.

## Infrastructure as code

- **Public exposure**: public network access, firewall rules open to `0.0.0.0/0`, public storage containers.
- **Transport security**: TLS older than 1.2, HTTP allowed where HTTPS is possible.
- **Secrets in IaC**: passwords or keys in variables, defaults or outputs.
- **Missing protection**: no encryption, soft delete or backup on resources that hold data.

## Severity

- **High**: exploitable from outside, or leaks credentials.
- **Medium**: exploitable with some access or under specific conditions.
- **Low**: hardening and hygiene.
