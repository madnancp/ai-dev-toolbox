

Usage
```bash
python main.py --prompt "what is the chemical form of Water?"

```

> [!NOTE]
> When running for the first time, this take a while to load the model.

```bash
model loading from HF hub, please wait ....
llama_context: n_ctx_per_seq (512) < n_ctx_train (2048) -- the full capacity of the model will not be utilized
model loading completed!
Inference params:
temperature=0.8
top_p=0.96
top_k=50
max_new_tokens=512
Assistant : The chemical form of water is H2O, which stands for hydrogen (H) and oxygen (O). Hydrogen and oxygen are the two atoms that make up water molecules.
```

Args

- --prompt = str | required
- --temperature = float | default (0.8)
- --top_k = int | default (50)
- --top_p = float | default (0.96)


