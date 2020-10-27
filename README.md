# kubeflow-recommender
Pipeline in Google AI Platform with Kubeflow

- Steps will be explained in more detail.

# Preprocessing
- dsl-compile --py pipeline.py --output pipeline.yaml

# Build Model

# Deployment
python setup.py sdist --formats=gztar 
gsutil cp dist/svd_model-0.1.tar.gz gs://mokarakayamodels/staging
gcloud ai-platform models create svdmodel --regions us-central1


python setup.py sdist --formats=gztar 
gsutil cp dist/lightfm_model-0.1.tar.gz gs://mokarakayamodels/staging
gsutil cp lightfm.p gs://mokarakayamodels/staging
gcloud ai-platform models create lightfmmodelwithlogs --regions us-central1
    --enable-logging \
    --enable-console-logging
 
gcloud beta ai-platform versions create v0_0_1  \
  --model lightfmmodelwithlogs \
  --runtime-version 2.2 \
  --python-version 3.7 \
  --origin gs://mokarakayamodels/staging \
  --package-uris gs://mokarakayamodels/staging/lightfm_model-0.1.tar.gz \
  --prediction-class lightfm_predictor.MyPredictor \
  --enable-logging

- See runtime-version-list for Google AI platform at; https://cloud.google.com/ai-platform/training/docs/runtime-version-list