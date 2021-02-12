import lib.CommonUtil as utility
import lib.GitUtil as git
import variableFile
import json


app_set_name = variableFile.app_setting_name
app_api = variableFile.app_api_name
env_value_all = variableFile.env_value_all
env_value = variableFile.env_value
dv2 = variableFile.env_value_dv2
dv3 = variableFile.env_value_dv3
ve2 = variableFile.env_value_ve2
hqe = variableFile.env_value_hqe
qe3 = variableFile.env_value_qe3
pre_e = variableFile.env_value_pre_e
pre_w = variableFile.env_value_pre_w
prd_e = variableFile.env_value_prd_e
prd_w = variableFile.env_value_prd_w
app_set_file_path = variableFile.app_set_file_path
device_model_type_file = variableFile.device_model_type_file
device_model_type = variableFile.device_model_type
git_branch = variableFile.git_branch
git_branch_re = variableFile.git_branch_re
repo_path = variableFile.repo_path
git_pull_success_status = variableFile.git_pull_success_status
jira_ticket = variableFile.jira_ticket


class AddL1SupportDeviceModelType:
    def __init__(self):
        print("Adding level 1 support for new device models")

    def sync_local_to_remote_repo(self):
        global repo_path, git_branch, git_branch_re, git_pull_success_status
        try:
            print("This is a 'sync_local_to_remote_repo' method")
            self.flag = False
            git_pull_status = git.git_pull_oper(repo_path=repo_path, git_branch=git_branch,
                                                git_branch_re=git_branch_re,
                                                git_pull_success_status=git_pull_success_status)
            if git_pull_status:
                print("Local repo is up to date with the remote repo")
                self.flag = True

            else:
                print("Local repo is unable to sync with the remote repo")

        except Exception as err:
            print("Local repo sync with the remote repo failed %s" % err)

    def add_device_model_type_file(self):
        try:
            if self.flag:
                self.model_type_flag = False
                with open(device_model_type_file) as model_type_file:
                    data = json.load(model_type_file)
                    data['id'] = device_model_type
                    data['modelType'] = device_model_type
                    self.model_type_flag = True

                if self.model_type_flag:
                    with open('devicemodeltypes_%s.json' % device_model_type, 'w') as outfile:
                        json.dump(data, outfile)

