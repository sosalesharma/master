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
git_branch = variableFile.git_branch
git_branch_re = variableFile.git_branch_re
repo_path = variableFile.repo_path
git_pull_success_status = variableFile.git_pull_success_status
jira_ticket = variableFile.jira_ticket

class AppSettings:
    def __init__(self):
        print("This is a init method of a class")

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
            print("Local repo sync with the remote repo failed ")

    def add_app_setting(self):
        global app_set_name, app_api, env_value_all, dv2, dv3, ve2, hqe, qe3, pre_e, pre_w, prd_e, prd_w
        if self.flag:
            try:
                print("This is add_app_setting method")
                self.app_set_status = False
                with open(app_set_file_path) as app_file:
                    init_data = json.load(app_file)

                for items in init_data:
                    if app_set_name == items['App Settings'] and app_api == items['API']:
                        print("App setting with the App name already exist. Aborting the operation")
                        break
                else:
                    print("Creating the json entry for app setting")

                    new_app_set_entry = utility.generate_app_setting_schema(app_set_name=app_set_name, app_api=app_api,
                                                                            env_value_all=env_value_all,
                                                                            env_value=env_value, env_dv2=dv2,
                                                                            env_dv3=dv3, env_ve2=ve2, env_hqe=hqe,
                                                                            env_qe3=qe3, env_pre_e=pre_e,
                                                                            env_pre_w=pre_w, env_prd_e=prd_e,
                                                                            env_prd_w=prd_w)
                    print(new_app_set_entry)

                    result = utility.append_app_settings(file_path=app_set_file_path, add_content=new_app_set_entry,
                                                         app_api=app_api)
                if result:
                    print("Adding new App settings to the file is successful")
                    self.app_set_status = True

            except Exception as err:
                print("Adding new App settings to the file failed ")
                status = False



    def push_files_to_remote_repo(self):
        global repo_path, jira_ticket
        if self.app_set_status:
            try:
                git_push_status = git.git_push_oper(repo_path=repo_path, jira_ticket=jira_ticket)
                if git_push_status:
                    print("App files push to remote repo is successful")

            except Exception as err:
                print("App files push to remote repo is successful failed ")

app_set_test = AppSettings()
app_set_test.sync_local_to_remote_repo()
app_set_test.add_app_setting()
app_set_test.push_files_to_remote_repo()