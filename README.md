# quickstart-atlassian-services
## Atlassian Standard Infrastructure on the AWS Cloud

This Quick Start sets up the Atlassian Standard Infrastructure (ASI) in your AWS
account in about 20 minutes. ASI is a highly available, secure virtual private
cloud (VPC) that is specifically customized to host Atlassian Data Center
products.

The ASI includes two public and two private subnets in two Availability Zones in
your AWS account, and contains all the components required for the deployment
and integration of multiple Atlassian Data Center products within the same VPC.

![Quick Start architecture for Atlassian Standard Infrastructure on AWS](https://d0.awsstatic.com/partner-network/QuickStart/datasheets/atlassian-standard-architecture-on-the-aws-cloud.png)

The [Jira](https://fwd.aws/kRapJ), [Confluence](https://fwd.aws/JAEM9), and
[Bitbucket](https://fwd.aws/BBeJW) Quick Starts all require the ASI.

For architectural details, best practices, step-by-step instructions, and
customization options, see the [deployment guide](https://fwd.aws/xYyYy).

### Contributing & issues

Please note that issues are disabled for this repository, because it is a
downstream repository that is not actively supported.
We welcome pull requests, issues, and comments in the **[upstream repository](https://github.com/aws-quickstart/quickstart-atlassian-services/)**.

If you'd like to submit code for this Quick Start, please review the [AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/).

## Development notes

### Pre-commit hook

It is recommended that you install the hooks under `scripts/hooks/`; this will
ensure that the metadata tags in the templates are automatically updated on
commit. The simplest method of doing this is:

    git config --add core.hooksPath scripts/hooks/
