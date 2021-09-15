MAKEFILE := $(lastword $(MAKEFILE_LIST))
PWD := $(patsubst %/,%,$(dir $(abspath $(MAKEFILE))))

DASHBOARD_TEMPLATE_NAME = quickstart-cloudwatch-dashboard.yaml
DASHBOARD_CONFIG_NAME = cloudwatch_dashboard_config.json

DASHBOARD_CONFIG_FILE := $(PWD)/config/$(DASHBOARD_CONFIG_NAME)
DASHBOARD_TEMPLATE_FILE := $(PWD)/config/$(DASHBOARD_TEMPLATE_NAME).template
DASHBOARD_TEMPLATE := $(PWD)/templates/$(DASHBOARD_TEMPLATE_NAME)


define prettyecho
        $(if $(TERM),
                @tput setaf $2
                @echo $1
                @tput sgr0,
                @echo $1)
endef

create_dashboard_template:
		@echo
		$(call prettyecho, "Reading contents of - $(DASHBOARD_CONFIG_FILE) and replacing marker in $(DASHBOARD_TEMPLATE_FILE)", 13)
		# The following command replaces the text 'DASHBOAD_CONFIG' in the template file 
		# with content present in the cloudwatch dashboad configurartion file
		# and writes the output to the cloudwatch template under templates/ directory
		cat $(DASHBOARD_TEMPLATE_FILE) | sed -e s~DASHBOARD_CONFIG~'$(shell cat $(DASHBOARD_CONFIG_FILE) | tr -s "[:space:]" | tr -d "\t" | tr -d "\n")'~g > $(DASHBOARD_TEMPLATE)
		$(call prettyecho, "Template created at - $(DASHBOARD_TEMPLATE). Contents are -", 13)
		cat $(DASHBOARD_TEMPLATE)
		@echo

verify_dashboard_checksum:
	@echo
	$(eval GENERATED_MD5 := $(shell cat $(DASHBOARD_TEMPLATE_FILE) | sed -e s~DASHBOARD_CONFIG~'$(shell cat $(DASHBOARD_CONFIG_FILE) | tr -s "[:space:]" | tr -d "\t" | tr -d "\n")'~g | md5))
	$(eval ACTUAL_MD5 := $(shell cat $(DASHBOARD_TEMPLATE) | md5))
	@if [ "$(GENERATED_MD5)" == "$(ACTUAL_MD5)" ]; then echo "MD5 matches"; else echo "MD5 Mismatch!! Throwing error" && exit -2; fi;
	@echo

