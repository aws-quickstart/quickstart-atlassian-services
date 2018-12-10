# quickstart-atlassian-services

## VPC for Atlassian Data Center service on AWS Cloud

This Quick Start sets up a highly available, secure AWS Virtual Private Cloud
(VPC) to host [Atlassian Data Center][data-center] products. This VPC differs
slightly from the standard [AWS VPC configuration][aws-vpc] to enable multiple
products under the same VPC for cross-application integration.

You should deploy this Quick Start VPC, or configure your own VPC before you 
deploy the other Atlassian Product Quick Starts.

### Example deployed VPC (with Jira Data Center)

![Example deployed VPC (with Jira Data Center)][vpc-img]

[data-center]: https://www.atlassian.com/enterprise/data-center
[aws-vpc]: https://github.com/aws-quickstart/quickstart-aws-vpc
[vpc-img]: https://github.com/tarka/quickstart-atlassian-services/raw/master/docs/vpc-with-jira.png
