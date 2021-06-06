how to wrap python function to make a component

import glob
import pandas as pd
import tarfile
import urllib.request
    
def download_and_merge_csv(url: str, output_csv: str):
  with urllib.request.urlopen(url) as res:
    tarfile.open(fileobj=res, mode="r|gz").extractall('data')
  df = pd.concat(
      [pd.read_csv(csv_file, header=None) 
       for csv_file in glob.glob('data/*.csv')])
  df.to_csv(output_csv, index=False, header=False)


after transform to a component

  @component(
    packages_to_install=['pandas==1.1.4'],
    output_component_file='component.yaml'
)
def merge_csv(tar_data: Input[Artifact], output_csv: Output[Dataset]):
  import glob
  import pandas as pd
  import tarfile

  tarfile.open(name=tar_data.path, mode="r|gz").extractall('data')
  df = pd.concat(
      [pd.read_csv(csv_file, header=None) 
       for csv_file in glob.glob('data/*.csv')])
  df.to_csv(output_csv.path, index=False, header=False)




