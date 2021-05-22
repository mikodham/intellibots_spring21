# intellibots_spring21

## Building Baseline Code
## Load Data
## Pre-process Data
1. pos_tag
2. word_embedding

## LSTM


## CNN



## Future Direction
1. Adding more features
2. Tuning Hyperparameters https://www.tensorflow.org/tensorboard/hyperparameter_tuning_with_hparams
3. Combine LSTM, CNN methods, and average the results => Build our own models

## References:
1. https://github.com/shaoxiongji/sw-detection -> keras, use LSTM and RNN, features:LICW, POS_TAG, tf_idf, basic features
2. https://github.com/viniciosfaustino/suicide-detection -> fastai, use RNN, features: NOT-given
3. https://github.com/BarnesLab/Identification-of-Imminent-Suicide-Risk-Among-Young-Adults-using-Text-Messages -> use tf.keras and keras, simple DNN, features: text_cleaner (ignore emoticons), tf_idf 
4. https://github.com/M-Ibtihaj/Suicidal-ideation-detection -> use scikit learn, logistic regression, features: using a lot of NLP features such as repetition, negative/positive words clustering, text cleaner(stopwords, punctuation)
5. https://github.com/cyash12/Depression-and-Suicidal-behvior-detection-on-Twitter-using-Machine-Learning
