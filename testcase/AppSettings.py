import lib.CommonUtil as utility
import logging as logger
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
file_path = variableFile.file_path

def add_app_setting(app_setting_name, app_api_name, app_setting_file):
    try:
        with open(app_setting_file) as app_file:
            init_data = json.load(app_file)

        for items in init_data:
            if app_setting_name == items['App Settings'] and app_api_name == items['API']:
                print("App setting with the App name already exist. Aborting the operation")
                break
        else:
            print("Creating the json entry for app setting")
            new_app_set_entry = utility.generate_app_setting_schema(app_set_name, app_api, env_value_all=env_value_all,
                                                                    env_value=env_value, env_dv2=dv2, env_dv3=dv3,
                                                                    env_ve2=ve2, env_hqe=hqe, env_qe3=qe3,
                                                                    env_pre_e=pre_e, env_pre_w=pre_w, env_prd_e=prd_e,
                                                                    env_prd_w=prd_w)
            result = utility.append_app_settings(file_path=app_setting_file,
                                                 add_content=new_app_set_entry,
                                                 app_api=app_api_name)
        if result:
            print("Adding new App settings to the file is successful")



  # if app_setting_name and app_api_name in open(app_setting_file).read():
  #   print("App setting with the App name already exist. Aborting the operation")
  #   else:
  #       result = utility.append_app_settings(file_path=app_setting_file,
  #                                            add_content=new_app_setting_entry,
  #                                            app_api=app_api_name)
  #   if result:
  #     print("Adding new App settings to the file is successful")
  #
    except Exception as err:
        print("Adding new App settings to the file failed ")


add_app_setting(app_setting_name=app_set_name,
                app_api_name=app_api,
                app_setting_file=file_path)




