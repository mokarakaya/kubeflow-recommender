import kfp.dsl as dsl
import kfp.components as comp
from collections import OrderedDict
from kubernetes import client as k8s_client


def clone(rok_workspace_recommender_kale_rurabvcwa_url: str, rok_recommender_data_qezwm7gn4_url: str):

    import os
    import shutil
    from kale.utils import pod_utils
    from kale.marshal import resource_save as _kale_resource_save
    from kale.marshal import resource_load as _kale_resource_load

    _kale_data_directory = "/home/jovyan/.Untitled1.ipynb.kale.marshal.dir"

    if not os.path.isdir(_kale_data_directory):
        os.makedirs(_kale_data_directory, exist_ok=True)

    pod_utils.snapshot_pipeline_step("rec-kale-euklz",
                                     "clone",
                                     "/home/jovyan/Untitled1.ipynb")

    import subprocess
    subprocess.check_output(
        ['git', 'clone', 'https://github.com/mokarakaya/kubeflow-recommender.git'])

    # -----------------------DATA SAVING START---------------------------------
    if "subprocess" in locals():
        _kale_resource_save(subprocess, os.path.join(
            _kale_data_directory, "subprocess"))
    else:
        print("_kale_resource_save: `subprocess` not found.")
    # -----------------------DATA SAVING END-----------------------------------


def checkout(rok_workspace_recommender_kale_rurabvcwa_url: str, rok_recommender_data_qezwm7gn4_url: str):

    import os
    import shutil
    from kale.utils import pod_utils
    from kale.marshal import resource_save as _kale_resource_save
    from kale.marshal import resource_load as _kale_resource_load

    _kale_data_directory = "/home/jovyan/.Untitled1.ipynb.kale.marshal.dir"

    if not os.path.isdir(_kale_data_directory):
        os.makedirs(_kale_data_directory, exist_ok=True)

    pod_utils.snapshot_pipeline_step("rec-kale-euklz",
                                     "checkout",
                                     "/home/jovyan/Untitled1.ipynb")

    # -----------------------DATA LOADING START--------------------------------
    _kale_directory_file_names = [
        os.path.splitext(f)[0]
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f))
    ]

    if "subprocess" not in _kale_directory_file_names:
        raise ValueError("subprocess" + " does not exists in directory")

    _kale_load_file_name = [
        f
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f)) and
        os.path.splitext(f)[0] == "subprocess"
    ]
    if len(_kale_load_file_name) > 1:
        raise ValueError("Found multiple files with name " +
                         "subprocess" + ": " + str(_kale_load_file_name))
    _kale_load_file_name = _kale_load_file_name[0]
    subprocess = _kale_resource_load(os.path.join(
        _kale_data_directory, _kale_load_file_name))
    # -----------------------DATA LOADING END----------------------------------

    subprocess.check_output(
        ['git', 'checkout', 'minikf-setup'], cwd='kubeflow-recommender')
    subprocess.check_output(['git', 'pull'], cwd='kubeflow-recommender')

    # -----------------------DATA SAVING START---------------------------------
    if "subprocess" in locals():
        _kale_resource_save(subprocess, os.path.join(
            _kale_data_directory, "subprocess"))
    else:
        print("_kale_resource_save: `subprocess` not found.")
    # -----------------------DATA SAVING END-----------------------------------


def install(rok_workspace_recommender_kale_rurabvcwa_url: str, rok_recommender_data_qezwm7gn4_url: str):

    import os
    import shutil
    from kale.utils import pod_utils
    from kale.marshal import resource_save as _kale_resource_save
    from kale.marshal import resource_load as _kale_resource_load

    _kale_data_directory = "/home/jovyan/.Untitled1.ipynb.kale.marshal.dir"

    if not os.path.isdir(_kale_data_directory):
        os.makedirs(_kale_data_directory, exist_ok=True)

    pod_utils.snapshot_pipeline_step("rec-kale-euklz",
                                     "install",
                                     "/home/jovyan/Untitled1.ipynb")

    # -----------------------DATA LOADING START--------------------------------
    _kale_directory_file_names = [
        os.path.splitext(f)[0]
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f))
    ]

    if "subprocess" not in _kale_directory_file_names:
        raise ValueError("subprocess" + " does not exists in directory")

    _kale_load_file_name = [
        f
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f)) and
        os.path.splitext(f)[0] == "subprocess"
    ]
    if len(_kale_load_file_name) > 1:
        raise ValueError("Found multiple files with name " +
                         "subprocess" + ": " + str(_kale_load_file_name))
    _kale_load_file_name = _kale_load_file_name[0]
    subprocess = _kale_resource_load(os.path.join(
        _kale_data_directory, _kale_load_file_name))
    # -----------------------DATA LOADING END----------------------------------

    subprocess.check_output(
        ['pip', 'install', '-r', 'requirements.txt', '--user'], cwd='kubeflow-recommender')
    subprocess.check_output(
        ['python', 'setup.py', 'build'], cwd='kubeflow-recommender')
    subprocess.check_output(
        ['python', 'setup.py', 'install', '--user'], cwd='kubeflow-recommender')

    # -----------------------DATA SAVING START---------------------------------
    if "subprocess" in locals():
        _kale_resource_save(subprocess, os.path.join(
            _kale_data_directory, "subprocess"))
    else:
        print("_kale_resource_save: `subprocess` not found.")
    # -----------------------DATA SAVING END-----------------------------------


def preprocess(rok_workspace_recommender_kale_rurabvcwa_url: str, rok_recommender_data_qezwm7gn4_url: str):

    import os
    import shutil
    from kale.utils import pod_utils
    from kale.marshal import resource_save as _kale_resource_save
    from kale.marshal import resource_load as _kale_resource_load

    _kale_data_directory = "/home/jovyan/.Untitled1.ipynb.kale.marshal.dir"

    if not os.path.isdir(_kale_data_directory):
        os.makedirs(_kale_data_directory, exist_ok=True)

    pod_utils.snapshot_pipeline_step("rec-kale-euklz",
                                     "preprocess",
                                     "/home/jovyan/Untitled1.ipynb")

    # -----------------------DATA LOADING START--------------------------------
    _kale_directory_file_names = [
        os.path.splitext(f)[0]
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f))
    ]

    if "subprocess" not in _kale_directory_file_names:
        raise ValueError("subprocess" + " does not exists in directory")

    _kale_load_file_name = [
        f
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f)) and
        os.path.splitext(f)[0] == "subprocess"
    ]
    if len(_kale_load_file_name) > 1:
        raise ValueError("Found multiple files with name " +
                         "subprocess" + ": " + str(_kale_load_file_name))
    _kale_load_file_name = _kale_load_file_name[0]
    subprocess = _kale_resource_load(os.path.join(
        _kale_data_directory, _kale_load_file_name))
    # -----------------------DATA LOADING END----------------------------------

    subprocess.check_output(
        ['python', 'steps/preprocess_step/preprocess.py'], cwd='kubeflow-recommender')

    # -----------------------DATA SAVING START---------------------------------
    if "subprocess" in locals():
        _kale_resource_save(subprocess, os.path.join(
            _kale_data_directory, "subprocess"))
    else:
        print("_kale_resource_save: `subprocess` not found.")
    # -----------------------DATA SAVING END-----------------------------------


def buildmodel(rok_workspace_recommender_kale_rurabvcwa_url: str, rok_recommender_data_qezwm7gn4_url: str):

    import os
    import shutil
    from kale.utils import pod_utils
    from kale.marshal import resource_save as _kale_resource_save
    from kale.marshal import resource_load as _kale_resource_load

    _kale_data_directory = "/home/jovyan/.Untitled1.ipynb.kale.marshal.dir"

    if not os.path.isdir(_kale_data_directory):
        os.makedirs(_kale_data_directory, exist_ok=True)

    pod_utils.snapshot_pipeline_step("rec-kale-euklz",
                                     "buildmodel",
                                     "/home/jovyan/Untitled1.ipynb")

    # -----------------------DATA LOADING START--------------------------------
    _kale_directory_file_names = [
        os.path.splitext(f)[0]
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f))
    ]

    if "subprocess" not in _kale_directory_file_names:
        raise ValueError("subprocess" + " does not exists in directory")

    _kale_load_file_name = [
        f
        for f in os.listdir(_kale_data_directory)
        if os.path.isfile(os.path.join(_kale_data_directory, f)) and
        os.path.splitext(f)[0] == "subprocess"
    ]
    if len(_kale_load_file_name) > 1:
        raise ValueError("Found multiple files with name " +
                         "subprocess" + ": " + str(_kale_load_file_name))
    _kale_load_file_name = _kale_load_file_name[0]
    subprocess = _kale_resource_load(os.path.join(
        _kale_data_directory, _kale_load_file_name))
    # -----------------------DATA LOADING END----------------------------------

    subprocess.check_output(
        ['python', 'steps/build_model_step/build_model.py'], cwd='kubeflow-recommender')


def final_auto_snapshot(rok_workspace_recommender_kale_rurabvcwa_url: str, rok_recommender_data_qezwm7gn4_url: str):

    import os
    import shutil
    from kale.utils import pod_utils
    from kale.marshal import resource_save as _kale_resource_save
    from kale.marshal import resource_load as _kale_resource_load

    _kale_data_directory = "/home/jovyan/.Untitled1.ipynb.kale.marshal.dir"

    if not os.path.isdir(_kale_data_directory):
        os.makedirs(_kale_data_directory, exist_ok=True)

    pod_utils.snapshot_pipeline_step("rec-kale-euklz",
                                     "final_auto_snapshot",
                                     "/home/jovyan/Untitled1.ipynb")


clone_op = comp.func_to_container_op(
    clone, base_image='gcr.io/arrikto-public/tensorflow-1.14.0-notebook-cpu:kubecon-workshop')


checkout_op = comp.func_to_container_op(
    checkout, base_image='gcr.io/arrikto-public/tensorflow-1.14.0-notebook-cpu:kubecon-workshop')


install_op = comp.func_to_container_op(
    install, base_image='gcr.io/arrikto-public/tensorflow-1.14.0-notebook-cpu:kubecon-workshop')


preprocess_op = comp.func_to_container_op(
    preprocess, base_image='gcr.io/arrikto-public/tensorflow-1.14.0-notebook-cpu:kubecon-workshop')


buildmodel_op = comp.func_to_container_op(
    buildmodel, base_image='gcr.io/arrikto-public/tensorflow-1.14.0-notebook-cpu:kubecon-workshop')


final_auto_snapshot_op = comp.func_to_container_op(
    final_auto_snapshot, base_image='gcr.io/arrikto-public/tensorflow-1.14.0-notebook-cpu:kubecon-workshop')


@dsl.pipeline(
    name='rec-kale-euklz',
    description='rec-kale'
)
def auto_generated_pipeline(rok_workspace_recommender_kale_rurabvcwa_url='http://rok.rok.svc.cluster.local/swift/v1/fbd42bc9-ad82-4e0c-9a01-b1a622d1b013/notebooks/recommender-kale-0_workspace-recommender-kale-rurabvcwa?version=5609fcf8-3a52-4b3b-b153-f076298cc2a1', rok_recommender_data_qezwm7gn4_url='http://rok.rok.svc.cluster.local/swift/v1/fbd42bc9-ad82-4e0c-9a01-b1a622d1b013/notebooks/recommender-kale-0_recommender-data-qezwm7gn4?version=2f748f17-cf80-4650-b778-8076aec79153'):
    pvolumes_dict = OrderedDict()

    annotations = {'rok/origin': 'http://rok.rok.svc.cluster.local/swift/v1/fbd42bc9-ad82-4e0c-9a01-b1a622d1b013/notebooks/recommender-kale-0_workspace-recommender-kale-rurabvcwa?version=5609fcf8-3a52-4b3b-b153-f076298cc2a1'}

    annotations['rok/origin'] = rok_workspace_recommender_kale_rurabvcwa_url

    vop1 = dsl.VolumeOp(
        name='create-volume-1',
        resource_name='workspace-recommender-kale-rurabvcwa',
        annotations=annotations,
        size='5Gi'
    )
    volume = vop1.volume

    pvolumes_dict['/home/jovyan'] = volume

    annotations = {'rok/origin': 'http://rok.rok.svc.cluster.local/swift/v1/fbd42bc9-ad82-4e0c-9a01-b1a622d1b013/notebooks/recommender-kale-0_recommender-data-qezwm7gn4?version=2f748f17-cf80-4650-b778-8076aec79153'}

    annotations['rok/origin'] = rok_recommender_data_qezwm7gn4_url

    vop2 = dsl.VolumeOp(
        name='create-volume-2',
        resource_name='recommender-data-qezwm7gn4',
        annotations=annotations,
        size='5Gi'
    )
    volume = vop2.volume

    pvolumes_dict['/home/jovyan/recommender-data'] = volume

    clone_task = clone_op(rok_workspace_recommender_kale_rurabvcwa_url, rok_recommender_data_qezwm7gn4_url)\
        .add_pvolumes(pvolumes_dict)\
        .after()
    clone_task.container.working_dir = "/home/jovyan"
    clone_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    mlpipeline_ui_metadata = {
        'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    clone_task.output_artifact_paths.update(mlpipeline_ui_metadata)

    checkout_task = checkout_op(rok_workspace_recommender_kale_rurabvcwa_url, rok_recommender_data_qezwm7gn4_url)\
        .add_pvolumes(pvolumes_dict)\
        .after(clone_task)
    checkout_task.container.working_dir = "/home/jovyan"
    checkout_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    mlpipeline_ui_metadata = {
        'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    checkout_task.output_artifact_paths.update(mlpipeline_ui_metadata)

    install_task = install_op(rok_workspace_recommender_kale_rurabvcwa_url, rok_recommender_data_qezwm7gn4_url)\
        .add_pvolumes(pvolumes_dict)\
        .after(checkout_task)
    install_task.container.working_dir = "/home/jovyan"
    install_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    mlpipeline_ui_metadata = {
        'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    install_task.output_artifact_paths.update(mlpipeline_ui_metadata)

    preprocess_task = preprocess_op(rok_workspace_recommender_kale_rurabvcwa_url, rok_recommender_data_qezwm7gn4_url)\
        .add_pvolumes(pvolumes_dict)\
        .after(install_task)
    preprocess_task.container.working_dir = "/home/jovyan"
    preprocess_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    mlpipeline_ui_metadata = {
        'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    preprocess_task.output_artifact_paths.update(mlpipeline_ui_metadata)

    buildmodel_task = buildmodel_op(rok_workspace_recommender_kale_rurabvcwa_url, rok_recommender_data_qezwm7gn4_url)\
        .add_pvolumes(pvolumes_dict)\
        .after(preprocess_task)
    buildmodel_task.container.working_dir = "/home/jovyan"
    buildmodel_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    mlpipeline_ui_metadata = {
        'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    buildmodel_task.output_artifact_paths.update(mlpipeline_ui_metadata)

    final_auto_snapshot_task = final_auto_snapshot_op(rok_workspace_recommender_kale_rurabvcwa_url, rok_recommender_data_qezwm7gn4_url)\
        .add_pvolumes(pvolumes_dict)\
        .after(buildmodel_task)
    final_auto_snapshot_task.container.working_dir = "/home/jovyan"
    final_auto_snapshot_task.container.set_security_context(
        k8s_client.V1SecurityContext(run_as_user=0))
    mlpipeline_ui_metadata = {
        'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    final_auto_snapshot_task.output_artifact_paths.update(
        mlpipeline_ui_metadata)


if __name__ == "__main__":
    pipeline_func = auto_generated_pipeline
    pipeline_filename = pipeline_func.__name__ + '.pipeline.tar.gz'
    import kfp.compiler as compiler
    compiler.Compiler().compile(pipeline_func, pipeline_filename)

    # Get or create an experiment and submit a pipeline run
    import kfp
    client = kfp.Client()
    experiment = client.create_experiment('rec-kale')

    # Submit a pipeline run
    run_name = 'rec-kale-euklz_run'
    run_result = client.run_pipeline(
        experiment.id, run_name, pipeline_filename, {})
