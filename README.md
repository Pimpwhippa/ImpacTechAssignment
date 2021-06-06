# ImpacTechAssignment

Iris Classification Infrastructure

General Information
To demonstrate experience with machine learning infrastructure will need to solve the Iris
classification problem. The goal is to create pipelines for data extraction, transformation, training,
and inference on a Kubernetes cluster.

Problem
Iris classification is a classic problem for data science: you can find additional information here. As a
reference, we will use a working example from the official Tensorflow guide
(https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough).

Requirements
1. Need to deploy Kubernetes cluster. For simplicity, you can use minikube, kind, or microk8s.
2. Need to have 2 separated solutions - training pipeline and inference pipeline
3. Need to configure a remote storage, that will be available from the cluster( it can be
mounted to the containers as volume)
4. Need to configure resources monitoring (Prometheus + Grafana). According to your
judgment include the most important and relevant metrics from the underlying Kubernetes
nodes and pods.
5. Need to “wrap” the code from the TensorFlow guide into docker containers for the following
tasks: download, training, optimize, evaluation, and prediction
