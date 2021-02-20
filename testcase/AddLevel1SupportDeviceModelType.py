import lib.CommonUtil as utility
import lib.GitUtil as git
import variableFile
import json
import time
import os
import uuid


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
level1_abs_path = variableFile.level1_abs_path
template_dir = variableFile.template_dir
device_view_model_file = variableFile.device_view_model_file
device_model_type = variableFile.device_model_type
git_branch = variableFile.git_branch
git_branch_re = variableFile.git_branch_re
repo_path = variableFile.repo_path
git_pull_success_status = variableFile.git_pull_success_status
jira_ticket = variableFile.jira_ticket


class AddL1SupportDeviceModelType:
    def __init__(self):
        print("Addressing the Level 1 support for Device Model Type and Device View Model ticket %s" % jira_ticket)

    def sync_local_to_remote_repo(self):
        global repo_path, git_branch, git_branch_re, git_pull_success_status
        try:
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
    '''
    def add_device_model_type_file(self):
        try:
            self.model_type_flag = False
            if self.flag:
                with open(device_model_type_file) as model_type_file:
                    data = json.load(model_type_file)
                    data['id'] = device_model_type
                    data['modelType'] = device_model_type
                    print("Data for model type file is created successfully")
                    self.model_type_flag = True

                if self.model_type_flag:
                    with open(os.path.join(level1_abs_path, 'devicemodeltypes_%s.json' % device_model_type),
                                           'w') as outfile:
                    # with open('devicemodeltypes_%s.json' % device_model_type, 'w') as outfile:
                        json.dump(obj=data, fp=outfile, indent=2)
                        outfile.close()
                        time.sleep(2)
                        print("Creation of Device Model Type file is successful")
                else:
                    print("Creation of Device Model Type file is failed")
            else:
                print("Git repo is out of sync, please do fix it")
        except Exception as err:
            print("Adding Device Model Type file failed with exception %s" % err)

    def add_device_view_model_file(self):
        try:
            self.view_model_flag = False
            if self.flag:
                with open(device_view_model_file) as view_model_file:
                    data = json.load(view_model_file)
                    data['id'] = device_model_type
                    print("Data for model type file is created successfully")
                    self.view_model_flag = True

                if self.view_model_flag:
                    with open(os.path.join(level1_abs_path, 'deviceviewmodels_%s.json' % device_model_type),
                                           'w') as outfile:
                    # with open('deviceviewmodels_%s.json' % device_model_type, 'w') as outfile:
                        json.dump(obj=data, fp=outfile, indent=2)
                        outfile.close()
                        time.sleep(2)
                        print("Creation of Device View Model file is successful")
                else:
                    print("Creation of Device View Model file is failed")
            else:
                print("Git repo is out of sync, please do fix it")
        except Exception as err:
            print("Adding Device View Model file failed with exception %s" % err)
    '''

    def add_level1_sup_files(self):
        global template_dir, level1_abs_path, device_model_type
        prop_device_model_type = '_%s_' % device_model_type
        self.model_type_flag = False
        for files in os.listdir(template_dir):
            if 'devicemodeltype' in files or 'deviceviewmodel' in files:
                print('devicemodeltype - %s' % files)

                with open(os.path.join(template_dir, files)) as model_type_file:
                    data = json.load(model_type_file)
                    data['id'] = device_model_type
                    if 'devicemodeltype' in files:
                        data['modelType'] = device_model_type
                    print("Data for model type/view file is created successfully")

            elif 'PropertyValues' in files:
                with open(os.path.join(template_dir, files)) as prop_value_file:
                    data = json.load(prop_value_file)
                    data['DeviceModel'] = device_model_type
                    data['id'] = str(uuid.uuid4())
                    print("Data for property value file is created successfully")
            else:
                break

            if 'devicemodeltype' in files:
                file_name = 'devicemodeltypes_%s.json' % device_model_type
            elif 'deviceviewmodel' in files:
                file_name = 'deviceviewmodel_%s.json' % device_model_type
            elif 'PropertyValues' in files:
                file_name = prop_device_model_type.join(files.split('_'))
            else:
                break

            with open(os.path.join(level1_abs_path, file_name),
                      'w') as outfile:
                json.dump(obj=data, fp=outfile, indent=2)
                outfile.close()
                time.sleep(2)
                self.model_type_flag = True
        print("Creation of Level 1 support Device Model Type files are successful")

    def push_files_to_remote_repo(self):
        global repo_path, jira_ticket
        try:
            if self.model_type_flag:
                git_push_status = git.git_push_oper(repo_path=repo_path, jira_ticket=jira_ticket)
                if git_push_status:
                    print("Level 1 support Device Model Type files push to remote repo is successful")

        except Exception as err:
            print("Level 1 support Device Model Type files push to remote repo is failed %s" % err)





level1_support = AddL1SupportDeviceModelType()
level1_support.sync_local_to_remote_repo()
level1_support.add_level1_sup_files()
level1_support.push_files_to_remote_repo()