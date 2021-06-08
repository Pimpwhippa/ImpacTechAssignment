# Define a pipeline and create a task from a component:
@dsl.pipeline(
    name='my-pipeline',
    # You can optionally specify your own pipeline_root
    # pipeline_root='gs://my-pipeline-root/example-pipeline',
)
def my_pipeline(url: str):
  web_downloader_task = web_downloader_op(url=url)
  merge_csv_task = merge_csv(tar_data=web_downloader_task.outputs['data'])
  # The outputs of the merge_csv_task can be referenced using the
  # merge_csv_task.outputs dictionary: merge_csv_task.outputs['output_csv']
