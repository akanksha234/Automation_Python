import os
import shutil
import time
import pytest

#In case, if we have a fear of any error we can define a default value for our parameter.
#In case if the user does not provides any value to the function, there will be a default value whoch will
#be assigned to the parameter
folders_list = ['Music', 'fun', 'parliament']

@pytest.fixture(scope='module')
def delete_folder():
  yield
  time.sleep(20)
  for folder in folders_list:
    shutil.rmtree(folder, ignore_errors=True)

@pytest.mark.parametrize("folders_list", [folders_list])
def test_make_folders(delete_folder, folders_list, nest= False):
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = "."
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        print(path_to_new_folder)
        os.makedirs("./" + path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)
        assert (os.path.exists(folder))
      except FileExistsError:
        continue


