from argparse import ArgumentParser
from infer import LLMInference


llm_infer = LLMInference()
parser = ArgumentParser(description="an llm inference script, used in CLI.")

parser.add_argument(
    "--prompt", help="enter your prompt to ask LLM.", required=True, type=str
)
parser.add_argument(
    "--temperature", help="`temperature` param.", default=0.8, type=float
)
parser.add_argument("--top_k", help="`top_k` param.", default=50, type=int)
parser.add_argument("--top_p", help="`top_p` param.", default=0.96, type=float)

get_args = parser.parse_args()

llm_infer.get_output(
    prompt=get_args.prompt,
    temperature=get_args.temperature,
    top_p=get_args.top_p,
    top_k=get_args.top_k,
)
