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

The Quick Starts for [Jira](https://fwd.aws/kRapJ), [Confluence](https://fwd.aws/JAEM9), 
[Bitbucket](https://fwd.aws/BBeJW), and  [Crowd](https://fwd.aws/QXEDE) all require the ASI.

For architectural details, best practices, step-by-step instructions, and
customization options, see the [deployment guide](https://fwd.aws/xYyYy).

## Deploying for production

For production deployments, avoid launching the ASI Quick Start from the AWS Quick Start interface. If you do, any changes made to the Quick Start templates will propagate directly to your deployment. These updates sometimes introduce unexpected changes that could break your deployment.

Instead, clone the ASI Quick Start templates to a custom Amazon Simple Storage Service (Amazon S3) bucket. Then, launch the templates directly from the S3 bucket. This practice lets you control when to apply the latest changes to your environment. See the [deployment guide](https://fwd.aws/xYyYy) for more details.

## Development notes

For pre-commit hooks, we recommend that you install them under `scripts/hooks/`. This will ensure that the metadata tags in the templates are automatically updated on commit. The simplest method of doing this is:

    git config --add core.hooksPath scripts/hooks/

## Atlassian support

This Quick Start's CloudFormation templates were developed by Atlassian, in collaboration with AWS. To report an issue or request a feature, you can [contact Atlassian directly](https://support.atlassian.com/contact/#/).
