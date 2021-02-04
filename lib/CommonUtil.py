import json
import sys
import logging as logger
import git
from git import Repo
from git import RemoteProgress

'''
def append_app_settings(file_path, add_content,app_api):
    try:
        print("Open App Setting JSON file and append with the new API entry")
        with open(file_path) as f:
            init_data = json.load(f)
            data = init_data
            if app_api == 'All' or app_api == 'all':
                data.insert(0, add_content)
            else:
                data.append(add_content)
        print("Appending with the new API entry is successful")

        print("Write the new content to the App Setting file")
        f1 = open(file_path, 'w+')
        json.dump(obj=data, fp=f1, indent=2)
        f1.close()
        return True
    except Exception as err:
        file_data = open(file_path, 'w+')
        json.dump(obj=init_data, fp=file_data, indent=2)
        print("File is replaced with initial data %s", err)
        return False


def generate_app_setting_schema(app_set_name, app_api, env_value_all=None, env_value=None, env_dv2=None, env_dv3=None,
                                env_ve2=None, env_hqe=None, env_qe3=None, env_pre_e=None, env_pre_w=None,
                                env_prd_e=None, env_prd_w=None):
    # if env_value_all != None:
    #     dv2 = dv3 = ve2 = hqe = qe3 = pre_e = pre_w = prd_e = prd_w = env_value_all
    if env_dv2 != None:
        dv2 = env_dv2
    else:
        dv2 = env_value_all
    if env_dv3 != None:
        dv3 = env_dv3
    else:
        dv3 = env_value_all
    if env_ve2 != None:
        ve2 = env_ve2
    else:
        ve2 = env_value_all
    if env_hqe != None:
        hqe = env_hqe
    else:
        hqe = env_value_all
    if env_qe3 != None:
        qe3 = env_qe3
    else:
        qe3 = env_value_all
    if env_pre_e != None:
        pre_e = env_pre_e
    else:
        pre_e = env_value_all
    if env_pre_w != None:
        pre_w = env_pre_w
    else:
        pre_w = env_value_all
    if env_prd_e != None:
        prd_e = env_prd_e
    else:
        prd_e = env_value_all
    if env_prd_w != None:
        prd_w = env_prd_w
    else:
        prd_w = env_value_all
    if env_value == 'dynamic':
        pass # write a method to get app id from azure portal for each envi
    append_content = {
        "App Settings": app_set_name,
        "API": app_api,
        "DV2USE": dv2,
        "DV3USE": dv3,
        "VE2USE": ve2,
        "HQEUSE": hqe,
        "QE3USE": qe3,
        "PREUSE": pre_e,
        "PREUSW": pre_w,
        "PRDUSE": prd_e,
        "PRDUSW": prd_w
    }
    return append_content
'''

repo_path = 'C:\\Users\\psharma\\Source\\Repos\\CrestronEngineering\\XIOCLOUD'
def verify_git_status():
    git_repo = git.Repo(repo_path)
    #print(git_repo.git.status())
    #print(git_repo.git.pull())
    print(git_repo.git.checkout('XIOCloud_1.20')) # Your branch is up to date with 'origin/XIOCloud_1.20'.
    # git_ref = git.cmd.Git(repo_path)
    # git_status = git_ref.pull()
    git_repo.git.add('somefile')
    git_repo.git.commit(m='commit message')


verify_git_status()