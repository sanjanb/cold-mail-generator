# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do not** open a public issue
2. Send an email to: [your-email@domain.com] (replace with actual email)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Release**: Within 30 days (for confirmed vulnerabilities)

## Security Best Practices

When using this application:

1. **Environment Variables**: Never commit `.env` files to version control
2. **API Keys**: Keep your Groq API key secure and rotate regularly
3. **Dependencies**: Regularly update dependencies to latest secure versions
4. **Input Validation**: Be cautious with URLs from untrusted sources
5. **Local Deployment**: For sensitive use cases, consider local deployment

## Security Features

- Environment variable protection for API keys
- Input sanitization for web scraping
- Error handling to prevent information disclosure
- Dependencies with known security track records

## Acknowledgments

We appreciate security researchers who responsibly disclose vulnerabilities to help keep our users safe.
