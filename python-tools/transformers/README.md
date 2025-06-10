# `transformers`

- It is a python library created by `Hugging Face`.

- Hugging-face store all kind models like ML, DL, NLP, LLMS, it will open source or closed source or gated.

- Hugging face and transformers are 2 sides of a coin
	- `Hugging Face` : is a platform were developers push pre-trained Machine learning Models, its like GitHub.
	- Were, `transformers`: is a python package that used to play with it.

- In HF, in a common pre-trained model repo contains, 
	- `configuration files`
	- `pre-trained weights/params`
	- `voccabulary`

## What is the use of transformers library.

- we know to reuse a pre-trained ML model we need the model skelton code and its trained weight.

- In here, the skelton stored in `transformers` and the trained weight stored on `HF`.

- So, when load a model from HF using transformers it fetch the configuration files and trained weight, and fetch the skelton class for the model and append the weight into it.

- We can also fine-tune models with transformers & PyTorch.
