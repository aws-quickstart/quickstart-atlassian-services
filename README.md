# Getting Started

This Quick Start sets up a highly available, secure AWS Virtual Private Cloud
(VPC) to host [Atlassian Data Center][data-center] products. This VPC differs
slightly from the standard [AWS VPC configuration][aws-vpc] to enable multiple
products under the same VPC for cross-application integration.

You should deploy this Quick Start VPC, or configure your own VPC before you 
deploy the other Atlassian Product Quick Starts.

### Example deployed VPC (with Jira Data Center installed)

Once you deploy his Atlassian Services VPC, you will have two (2) public subnets, one per availability zone selected along with two (2) private subnets. These are matched to ensure that your Atlassian products that are deployed, can be provisioned securely.

Select this provisioned VPC when using the additional Atlassian Quick Start guides.

![Example deployed VPC (with Jira Data Center)][vpc-img]


## Next Steps

See our individual product Quick Starts, at:

Quick Start for [Confluence Data Center](https://confluence.atlassian.com/doc/running-confluence-data-center-in-aws-879956085.html#RunningConfluenceDataCenterinAWS-DeployingConfluenceDataCenterusingtheAWSQuickStart)

Quick Start for [Jira Data Center](https://confluence.atlassian.com/adminjiraserver/getting-started-with-jira-data-center-on-aws-938846966.html)

Quick Start for [Bitbucket Data Center](https://confluence.atlassian.com/bitbucketserver/getting-started-with-bitbucket-server-and-aws-776640193.html)

[data-center]: https://www.atlassian.com/enterprise/data-center
[aws-vpc]: https://github.com/aws-quickstart/quickstart-aws-vpc
[vpc-img]: https://github.com/tarka/quickstart-atlassian-services/raw/master/docs/vpc-with-jira.png