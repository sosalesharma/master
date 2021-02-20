import lib.GitUtil as git
import variableFile
import json
import time
import os
import uuid


repo_path = variableFile.repo_path
git_branch = variableFile.git_branch
git_branch_re = variableFile.git_branch_re
git_pull_success_status = variableFile.git_pull_success_status
template_dir = variableFile.template_dir
level1_abs_path = variableFile.level1_abs_path
device_model_type = variableFile.device_model_type
jira_ticket = variableFile.jira_ticket


class AddL1SupportDeviceModelType:
    def __init__(self):
        print("Addressing the Level 1 support for Device Model Type and Device View Model ticket %s" % jira_ticket)

    def sync_local_to_remote_repo(self):
        global repo_path, git_branch, git_branch_re, git_pull_success_status
        self.flag = False
        try:
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

    def add_level1_sup_files(self):
        global template_dir, level1_abs_path, device_model_type
        prop_device_model_type = '_%s_' % device_model_type
        self.model_type_flag = False

        try:
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

        except Exception as err:
            print("Creation of Level 1 support Device Model Type files failed %s" % err)

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