@component(
    packages_to_install=['tensorflow', 'keras'], <-- what about module?
    output_component_file='model' <--what kind of file is this? it's an object/artifact
    )

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

ชื่อ function ที่จะเอามาเป็นชื่อ component ต้องเป็น object ที่จะเอาไปใส่ใน pipe ได้เลย
#def merge_csv(tar_data: Input[Artifact], output_csv: Output[Dataset]):

def create_keras_model(input:csv, output:[Artifact], param):

Use this method to load your component from a component.yaml path.
create_step_get_lines = comp.load_component_from_text("
                      kfp.components.load_component_from_url:
kfp.components.load_component_from_file:


train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"

train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),
                                           origin=train_dataset_url)

print("Local copy of the dataset file: {}".format(train_dataset_fp))

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

feature_names = column_names[:-1]
label_name = column_names[-1]

batch_size = 32

train_dataset = tf.data.experimental.make_csv_dataset(
    train_dataset_fp,
    batch_size,
    column_names=column_names,
    label_name=label_name,
    num_epochs=1)

features, labels = next(iter(train_dataset))

def pack_features_vector(features, labels):
  """Pack the features into a single array."""
  features = tf.stack(list(features.values()), axis=1)
  return features, labels

train_dataset = train_dataset.map(pack_features_vector)

#how is this used? why in create_keras_model and train_model 
#doesn't have anything to do with train_dataset?? only in optimizer where train_dataset comes in use
#only model.trainable_variables??


model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(4,)),  # input shape required
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(3)
])

#ตรงนี้ได้ output มาแล้วเป็น model แล้วมาเทรนโมเดลต่อ
#def merge_csv(tar_data: Input[Artifact], output_csv: Output[Dataset]):

def train_model(model:Input[Artifact], x, y, training, Output[Artifact]):

    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

def loss(model, x, y, training):
  # training=training is needed only if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  y_ = model(x, training=training)

  return loss_object(y_true=y, y_pred=y_)


l = loss(model, features, labels, training=False)
print("Loss test: {}".format(l))

#model to be delivered is l.model



def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets, training=True)
  return loss_value, tape.gradient(loss_value, model.trainable_variables)