import kfp.dsl as dsl
import json
import kfp.components as comp
from collections import OrderedDict
from kubernetes import client as k8s_client


def importrec():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "importrec",
        "/home/jovyan/Untitled.ipynb",
        before=True)

    block1 = '''
    import subprocess

    REPOSITORY='kubeflow-recommender'
    def run_sub(command, cwd=None):
        print(subprocess.check_output(command.split(' '), cwd=cwd))

    try:
        run_sub('git clone https://github.com/mokarakaya/kubeflow-recommender.git')
    except:
        print('error while fetching repo')
    run_sub('python3 --version', REPOSITORY)
    '''

    data_saving_block = '''
    # -----------------------DATA SAVING START---------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    _kale_marshal_utils.save(REPOSITORY, "REPOSITORY")
    _kale_marshal_utils.save(run_sub, "run_sub")
    _kale_marshal_utils.save(subprocess, "subprocess")
    # -----------------------DATA SAVING END-----------------------------------
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    blocks = (
        block1,
        data_saving_block)
    html_artifact = _kale_run_code(blocks)
    with open("/importrec.html", "w") as f:
        f.write(html_artifact)
    _kale_update_uimetadata('importrec')

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "importrec",
        "/home/jovyan/Untitled.ipynb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")


def pullrec():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "pullrec",
        "/home/jovyan/Untitled.ipynb",
        before=True)

    data_loading_block = '''
    # -----------------------DATA LOADING START--------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    REPOSITORY = _kale_marshal_utils.load("REPOSITORY")
    run_sub = _kale_marshal_utils.load("run_sub")
    subprocess = _kale_marshal_utils.load("subprocess")
    # -----------------------DATA LOADING END----------------------------------
    '''

    block1 = '''
    run_sub('git checkout minikf-setup', REPOSITORY)
    run_sub('git pull', REPOSITORY)
    '''

    data_saving_block = '''
    # -----------------------DATA SAVING START---------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    _kale_marshal_utils.save(REPOSITORY, "REPOSITORY")
    _kale_marshal_utils.save(run_sub, "run_sub")
    _kale_marshal_utils.save(subprocess, "subprocess")
    # -----------------------DATA SAVING END-----------------------------------
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    blocks = (data_loading_block,
              block1,
              data_saving_block)
    html_artifact = _kale_run_code(blocks)
    with open("/pullrec.html", "w") as f:
        f.write(html_artifact)
    _kale_update_uimetadata('pullrec')

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "pullrec",
        "/home/jovyan/Untitled.ipynb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")


def installrec():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "installrec",
        "/home/jovyan/Untitled.ipynb",
        before=True)

    data_loading_block = '''
    # -----------------------DATA LOADING START--------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    REPOSITORY = _kale_marshal_utils.load("REPOSITORY")
    run_sub = _kale_marshal_utils.load("run_sub")
    subprocess = _kale_marshal_utils.load("subprocess")
    # -----------------------DATA LOADING END----------------------------------
    '''

    block1 = '''
    run_sub('pip3 install -r requirements.txt', REPOSITORY)
    run_sub('python3 setup.py build', REPOSITORY)
    run_sub('python3 setup.py install --user', REPOSITORY)
    '''

    data_saving_block = '''
    # -----------------------DATA SAVING START---------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    _kale_marshal_utils.save(REPOSITORY, "REPOSITORY")
    _kale_marshal_utils.save(run_sub, "run_sub")
    _kale_marshal_utils.save(subprocess, "subprocess")
    # -----------------------DATA SAVING END-----------------------------------
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    blocks = (data_loading_block,
              block1,
              data_saving_block)
    html_artifact = _kale_run_code(blocks)
    with open("/installrec.html", "w") as f:
        f.write(html_artifact)
    _kale_update_uimetadata('installrec')

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "installrec",
        "/home/jovyan/Untitled.ipynb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")


def preprocessrec():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "preprocessrec",
        "/home/jovyan/Untitled.ipynb",
        before=True)

    data_loading_block = '''
    # -----------------------DATA LOADING START--------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    REPOSITORY = _kale_marshal_utils.load("REPOSITORY")
    run_sub = _kale_marshal_utils.load("run_sub")
    subprocess = _kale_marshal_utils.load("subprocess")
    # -----------------------DATA LOADING END----------------------------------
    '''

    block1 = '''
    run_sub('python3 steps/preprocess_step/preprocess.py', REPOSITORY)
    '''

    data_saving_block = '''
    # -----------------------DATA SAVING START---------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    _kale_marshal_utils.save(REPOSITORY, "REPOSITORY")
    _kale_marshal_utils.save(run_sub, "run_sub")
    _kale_marshal_utils.save(subprocess, "subprocess")
    # -----------------------DATA SAVING END-----------------------------------
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    blocks = (data_loading_block,
              block1,
              data_saving_block)
    html_artifact = _kale_run_code(blocks)
    with open("/preprocessrec.html", "w") as f:
        f.write(html_artifact)
    _kale_update_uimetadata('preprocessrec')

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "preprocessrec",
        "/home/jovyan/Untitled.ipynb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")


def buildrec():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "buildrec",
        "/home/jovyan/Untitled.ipynb",
        before=True)

    data_loading_block = '''
    # -----------------------DATA LOADING START--------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    REPOSITORY = _kale_marshal_utils.load("REPOSITORY")
    run_sub = _kale_marshal_utils.load("run_sub")
    subprocess = _kale_marshal_utils.load("subprocess")
    # -----------------------DATA LOADING END----------------------------------
    '''

    block1 = '''
    run_sub('python3 steps/build_model_step/build_model.py', REPOSITORY)
    '''

    data_saving_block = '''
    # -----------------------DATA SAVING START---------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    _kale_marshal_utils.save(REPOSITORY, "REPOSITORY")
    _kale_marshal_utils.save(run_sub, "run_sub")
    _kale_marshal_utils.save(subprocess, "subprocess")
    # -----------------------DATA SAVING END-----------------------------------
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    blocks = (data_loading_block,
              block1,
              data_saving_block)
    html_artifact = _kale_run_code(blocks)
    with open("/buildrec.html", "w") as f:
        f.write(html_artifact)
    _kale_update_uimetadata('buildrec')

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "buildrec",
        "/home/jovyan/Untitled.ipynb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")


def saverec():
    from kale.common import mlmdutils as _kale_mlmdutils
    _kale_mlmdutils.init_metadata()

    from kale.common import podutils as _kale_podutils
    _kale_mlmdutils.call("link_input_rok_artifacts")
    _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "saverec",
        "/home/jovyan/Untitled.ipynb",
        before=True)

    data_loading_block = '''
    # -----------------------DATA LOADING START--------------------------------
    from kale.marshal import utils as _kale_marshal_utils
    _kale_marshal_utils.set_kale_data_directory("/home/jovyan/.Untitled.ipynb.kale.marshal.dir")
    REPOSITORY = _kale_marshal_utils.load("REPOSITORY")
    run_sub = _kale_marshal_utils.load("run_sub")
    subprocess = _kale_marshal_utils.load("subprocess")
    # -----------------------DATA LOADING END----------------------------------
    '''

    block1 = '''
    from datetime import datetime
    now = str(datetime.timestamp(datetime.now()))
    run_sub('gsutil cp lightfm.p gs://mokarakayamodels2/staging/lightfm.p' + now , REPOSITORY)
    '''

    # run the code blocks inside a jupyter kernel
    from kale.common.jputils import run_code as _kale_run_code
    from kale.common.kfputils import \
        update_uimetadata as _kale_update_uimetadata
    blocks = (data_loading_block,
              block1,
              )
    html_artifact = _kale_run_code(blocks)
    with open("/saverec.html", "w") as f:
        f.write(html_artifact)
    _kale_update_uimetadata('saverec')

    _rok_snapshot_task = _kale_podutils.snapshot_pipeline_step(
        "pipeline2-u5c78",
        "saverec",
        "/home/jovyan/Untitled.ipynb",
        before=False)
    _kale_mlmdutils.call("submit_output_rok_artifact", _rok_snapshot_task)

    _kale_mlmdutils.call("mark_execution_complete")


importrec_op = comp.func_to_container_op(
    importrec, base_image='gcr.io/arrikto/jupyter-kale:v0.5.0-47-g2427cc9')


pullrec_op = comp.func_to_container_op(
    pullrec, base_image='gcr.io/arrikto/jupyter-kale:v0.5.0-47-g2427cc9')


installrec_op = comp.func_to_container_op(
    installrec, base_image='gcr.io/arrikto/jupyter-kale:v0.5.0-47-g2427cc9')


preprocessrec_op = comp.func_to_container_op(
    preprocessrec, base_image='gcr.io/arrikto/jupyter-kale:v0.5.0-47-g2427cc9')


buildrec_op = comp.func_to_container_op(
    buildrec, base_image='gcr.io/arrikto/jupyter-kale:v0.5.0-47-g2427cc9')


saverec_op = comp.func_to_container_op(
    saverec, base_image='gcr.io/arrikto/jupyter-kale:v0.5.0-47-g2427cc9')


@dsl.pipeline(
    name='pipeline2-u5c78',
    description='pipeline'
)
def auto_generated_pipeline(rok_jupyter_kale_05_1_vol_1_cqvv2obcc_url='http://rok.rok.svc.cluster.local/swift/v1/kubeflow-user/notebooks/jupyter-kale-05-1-0_jupyter-kale-05-1-vol-1-cqvv2obcc?version=c2fb1679-0f4c-4599-ba8c-a0b815fcd489', rok_workspace_jupyter_kale_05_1_2s0txj2ty_url='http://rok.rok.svc.cluster.local/swift/v1/kubeflow-user/notebooks/jupyter-kale-05-1-0_workspace-jupyter-kale-05-1-2s0txj2ty?version=254b9211-2faa-4f04-b828-29d8ccd76b00'):
    pvolumes_dict = OrderedDict()
    volume_step_names = []
    volume_name_parameters = []

    annotations = {'rok/origin': 'http://rok.rok.svc.cluster.local/swift/v1/kubeflow-user/notebooks/jupyter-kale-05-1-0_workspace-jupyter-kale-05-1-2s0txj2ty?version=254b9211-2faa-4f04-b828-29d8ccd76b00'}

    annotations['rok/origin'] = rok_workspace_jupyter_kale_05_1_2s0txj2ty_url

    vop1 = dsl.VolumeOp(
        name='create-volume-1',
        resource_name='workspace-jupyter-kale-05-1-2s0txj2ty',
        annotations=annotations,
        size='5Gi'
    )
    volume = vop1.volume
    volume_step_names.append(vop1.name)
    volume_name_parameters.append(vop1.outputs["name"].full_name)

    pvolumes_dict['/home/jovyan'] = volume

    annotations = {'rok/origin': 'http://rok.rok.svc.cluster.local/swift/v1/kubeflow-user/notebooks/jupyter-kale-05-1-0_jupyter-kale-05-1-vol-1-cqvv2obcc?version=c2fb1679-0f4c-4599-ba8c-a0b815fcd489'}

    annotations['rok/origin'] = rok_jupyter_kale_05_1_vol_1_cqvv2obcc_url

    vop2 = dsl.VolumeOp(
        name='create-volume-2',
        resource_name='jupyter-kale-05-1-vol-1-cqvv2obcc',
        annotations=annotations,
        size='5Gi'
    )
    volume = vop2.volume
    volume_step_names.append(vop2.name)
    volume_name_parameters.append(vop2.outputs["name"].full_name)

    pvolumes_dict['/home/jovyan/jupyter-kale-05-1-vol-1'] = volume

    volume_step_names.sort()
    volume_name_parameters.sort()

    importrec_task = importrec_op()\
        .add_pvolumes(pvolumes_dict)\
        .after()
    step_labels = {'access-ml-pipeline': 'true', 'access-rok': 'true'}
    for k, v in step_labels.items():
        importrec_task.add_pod_label(k, v)
    importrec_task.container.working_dir = "/home/jovyan"
    importrec_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    output_artifacts = {}
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update({'importrec': '/importrec.html'})
    importrec_task.output_artifact_paths.update(output_artifacts)
    importrec_task.add_pod_label(
        "pipelines.kubeflow.org/metadata_written", "true")
    dep_names = importrec_task.dependent_names + volume_step_names
    importrec_task.add_pod_annotation(
        "kubeflow-kale.org/dependent-templates", json.dumps(dep_names))
    if volume_name_parameters:
        importrec_task.add_pod_annotation(
            "kubeflow-kale.org/volume-name-parameters",
            json.dumps(volume_name_parameters))

    pullrec_task = pullrec_op()\
        .add_pvolumes(pvolumes_dict)\
        .after(importrec_task)
    step_labels = {'access-ml-pipeline': 'true', 'access-rok': 'true'}
    for k, v in step_labels.items():
        pullrec_task.add_pod_label(k, v)
    pullrec_task.container.working_dir = "/home/jovyan"
    pullrec_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    output_artifacts = {}
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update({'pullrec': '/pullrec.html'})
    pullrec_task.output_artifact_paths.update(output_artifacts)
    pullrec_task.add_pod_label(
        "pipelines.kubeflow.org/metadata_written", "true")
    dep_names = pullrec_task.dependent_names + volume_step_names
    pullrec_task.add_pod_annotation(
        "kubeflow-kale.org/dependent-templates", json.dumps(dep_names))
    if volume_name_parameters:
        pullrec_task.add_pod_annotation(
            "kubeflow-kale.org/volume-name-parameters",
            json.dumps(volume_name_parameters))

    installrec_task = installrec_op()\
        .add_pvolumes(pvolumes_dict)\
        .after(pullrec_task)
    step_labels = {'access-ml-pipeline': 'true', 'access-rok': 'true'}
    for k, v in step_labels.items():
        installrec_task.add_pod_label(k, v)
    installrec_task.container.working_dir = "/home/jovyan"
    installrec_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    output_artifacts = {}
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update({'installrec': '/installrec.html'})
    installrec_task.output_artifact_paths.update(output_artifacts)
    installrec_task.add_pod_label(
        "pipelines.kubeflow.org/metadata_written", "true")
    dep_names = installrec_task.dependent_names + volume_step_names
    installrec_task.add_pod_annotation(
        "kubeflow-kale.org/dependent-templates", json.dumps(dep_names))
    if volume_name_parameters:
        installrec_task.add_pod_annotation(
            "kubeflow-kale.org/volume-name-parameters",
            json.dumps(volume_name_parameters))

    preprocessrec_task = preprocessrec_op()\
        .add_pvolumes(pvolumes_dict)\
        .after(installrec_task)
    step_labels = {'access-ml-pipeline': 'true', 'access-rok': 'true'}
    for k, v in step_labels.items():
        preprocessrec_task.add_pod_label(k, v)
    preprocessrec_task.container.working_dir = "/home/jovyan"
    preprocessrec_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    output_artifacts = {}
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update({'preprocessrec': '/preprocessrec.html'})
    preprocessrec_task.output_artifact_paths.update(output_artifacts)
    preprocessrec_task.add_pod_label(
        "pipelines.kubeflow.org/metadata_written", "true")
    dep_names = preprocessrec_task.dependent_names + volume_step_names
    preprocessrec_task.add_pod_annotation(
        "kubeflow-kale.org/dependent-templates", json.dumps(dep_names))
    if volume_name_parameters:
        preprocessrec_task.add_pod_annotation(
            "kubeflow-kale.org/volume-name-parameters",
            json.dumps(volume_name_parameters))

    buildrec_task = buildrec_op()\
        .add_pvolumes(pvolumes_dict)\
        .after(preprocessrec_task)
    step_labels = {'access-ml-pipeline': 'true', 'access-rok': 'true'}
    for k, v in step_labels.items():
        buildrec_task.add_pod_label(k, v)
    buildrec_task.container.working_dir = "/home/jovyan"
    buildrec_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    output_artifacts = {}
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update({'buildrec': '/buildrec.html'})
    buildrec_task.output_artifact_paths.update(output_artifacts)
    buildrec_task.add_pod_label(
        "pipelines.kubeflow.org/metadata_written", "true")
    dep_names = buildrec_task.dependent_names + volume_step_names
    buildrec_task.add_pod_annotation(
        "kubeflow-kale.org/dependent-templates", json.dumps(dep_names))
    if volume_name_parameters:
        buildrec_task.add_pod_annotation(
            "kubeflow-kale.org/volume-name-parameters",
            json.dumps(volume_name_parameters))

    saverec_task = saverec_op()\
        .add_pvolumes(pvolumes_dict)\
        .after(buildrec_task)
    step_labels = {'access-ml-pipeline': 'true', 'access-rok': 'true'}
    for k, v in step_labels.items():
        saverec_task.add_pod_label(k, v)
    saverec_task.container.working_dir = "/home/jovyan"
    saverec_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    output_artifacts = {}
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update(
        {'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})
    output_artifacts.update({'saverec': '/saverec.html'})
    saverec_task.output_artifact_paths.update(output_artifacts)
    saverec_task.add_pod_label(
        "pipelines.kubeflow.org/metadata_written", "true")
    dep_names = saverec_task.dependent_names + volume_step_names
    saverec_task.add_pod_annotation(
        "kubeflow-kale.org/dependent-templates", json.dumps(dep_names))
    if volume_name_parameters:
        saverec_task.add_pod_annotation(
            "kubeflow-kale.org/volume-name-parameters",
            json.dumps(volume_name_parameters))


if __name__ == "__main__":
    pipeline_func = auto_generated_pipeline
    pipeline_filename = pipeline_func.__name__ + '.pipeline.tar.gz'
    import kfp.compiler as compiler
    compiler.Compiler().compile(pipeline_func, pipeline_filename)

    # Get or create an experiment and submit a pipeline run
    import kfp
    client = kfp.Client()
    experiment = client.create_experiment('experiment2')

    # Submit a pipeline run
    from kale.common.kfputils import generate_run_name
    run_name = generate_run_name('pipeline2-u5c78')
    run_result = client.run_pipeline(
        experiment.id, run_name, pipeline_filename, {})
