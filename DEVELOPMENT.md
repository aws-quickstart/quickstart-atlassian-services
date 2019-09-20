## Developing `quickstart-atlassian-services`
This repository contains templates that are used to provide shared infrastructure components for [atlassian quickstart templates](https://aws.amazon.com/quickstart/?quickstart-all.sort-by=item.additionalFields.updateDate&quickstart-all.sort-order=desc&quickstart-all.q=atlassian&quickstart-all.q_operator=AND)

Additionally, this repository uses `git submodules` to reference other shared infrastructure templates.

### Getting started

Most templates within the `templates` directory (except for `quickstart-cloudwatch-dashboard.yaml`), can be directly edited, tested (using `cfn-lint`) and deployed to AWS.

##### CloudWatch template
The CloudWatch template (`templates/quickstart-cloudwatch-dashboard.yaml`) creates a simple CloudWatch dashboard to visualize a few common metrics and logs. The purpose of this template is to provide a starting point for customers to view necessary metrics and logs that are relevant to their deployment. When a developer wants to update the `CloudWatch` dashboard, the following steps have to be executed in this order -

1. The Dashboard config (`templates/config/dashboard_config.json`) is a JSON file describing the CloudWatch dashboard configuration. This file has to be updated with a valid dashboard configuration JSON document. See [this page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html) for the correct structure and syntax.
2. If desired, the template definition `quickstart-cloudwatch-dashboard.yaml.template` may be updated to define/edit/remove resources, conditions, parameters, outputs and other cloudformation primitives. 
`Note: The template defines a marker string called DASHBOARD_CONFIG which will be replaced by the contents of the dashboard configuration JSON in the next step` 
3. Run `make create_dashboard_template` from the project root directory. This command updates the template (`templates/quickstart-cloudwatch-dashboard.yaml`) using the dashboard configuration and the template definition.
4. Lint & test the generated template with `cfn-lint templates/<template_name>`
5. If successful, commit all 3 files - the config, template definition and the generated template.   





